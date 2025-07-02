import argparse
import asyncio
import logging
import os
from concurrent import futures

import grpc

# TODO: 当protobuf定义准备好时导入
# import yeying.api.interview.interview_pb2_grpc as interview_pb2_grpc
# import yeying.api.rag.rag_pb2_grpc as rag_pb2_grpc

# 导入应用核心模块
from interviewr.config.config import Config  # 配置管理器
from interviewr.infrastructure.database.instance import ensure_migrated  # 数据库迁移
from interviewr.domain.models import ALL_MODELS  # 所有数据模型


# TODO: 当服务实现完成时导入
# from interview.servers.interview_server import InterviewServer
# from interview.servers.rag_server import RAGServer
# from interview.servers.digital_server import DigitalServer


# =================主应用运行器=================
class Runner:
    """主应用程序运行器 - 负责启动和管理gRPC服务"""

    def __init__(self, config: Config):
        """
        初始化运行器
        Args:
            config: 应用配置对象
        """
        self.config = config  # 保存配置引用
        self.server = None  # gRPC服务器实例

    async def serve(self):
        """启动gRPC服务器"""
        # 创建异步gRPC服务器
        self.server = grpc.aio.server(
            # 设置线程池用于数据库迁移等阻塞操作
            migration_thread_pool=futures.ThreadPoolExecutor(max_workers=100),
            # TODO: 当认证实现后添加拦截器
            # interceptors=[SignatureInterceptor(identity=self.identity)],
            # gRPC服务器选项配置
            options=[
                ('grpc.keepalive_time_ms', 30000),  # 30秒发送一次keepalive
                ('grpc.keepalive_timeout_ms', 10000),  # keepalive超时时间10秒
                ('grpc.keepalive_permit_without_calls', 1),  # 允许在没有调用时发送keepalive
            ]
        )

        # 获取服务器配置
        server_config = self.config.get_server()

        # 确保缓存目录存在
        if not os.path.exists(server_config.cacheDir):
            os.makedirs(server_config.cacheDir)

        # TODO: 当认证准备好时初始化认证
        # authenticate = Authenticate(blockAddress=self.blockAddress)

        # TODO: 当服务实现完成时初始化各个服务
        # interview_server = InterviewServer(authenticate=authenticate)     # 面试服务
        # rag_server = RAGServer(authenticate=authenticate)                # RAG检索增强生成服务
        # digital_server = DigitalServer(authenticate=authenticate)        # 数字化服务

        # TODO: 当服务实现完成时添加服务注册
        # interview_pb2_grpc.add_InterviewServicer_to_server(interview_server, self.server)
        # rag_pb2_grpc.add_RAGServicer_to_server(rag_server, self.server)

        # 构建服务监听地址（IPv6格式，监听所有接口）
        endpoint = f'[::]:{server_config.grpc_port}'

        # 根据配置决定是否启用SSL/TLS加密
        if self.config.get_credential().enable:
            logging.info('With credential.')  # 启用凭证模式
            # TODO: 当需要时实现SSL凭证
            # self.server.add_secure_port(endpoint, self.create_credentials())
            # 临时使用非加密端口（开发阶段）
            self.server.add_insecure_port(endpoint)
        else:
            logging.info('Without credential.')  # 非加密模式
            self.server.add_insecure_port(endpoint)

        # 启动服务器
        await self.server.start()
        logging.info(f'The interviewer service has been started successfully at {endpoint}')

        # 等待服务器终止
        await self.server.wait_for_termination()

    def create_credentials(self):
        """
        创建SSL凭证用于安全连接
        Returns:
            SSL凭证对象
        """
        # TODO: 当需要时实现SSL凭证创建
        pass


# =================命令行参数解析=================
def parse_args():
    """
    解析命令行参数
    Returns:
        解析后的参数对象
    """
    parser = argparse.ArgumentParser(description='Loading interviewer service parameters.')

    # 配置文件路径
    parser.add_argument('--config', type=str, default='config/config.toml',
                        help='Please set the interviewer service config.')

    # 运行环境（开发/测试/生产）
    parser.add_argument('--env', type=str, default='dev',
                        help='Please set the runtime environment.')

    # 调试模式开关
    parser.add_argument('--debug', action='store_true',
                        help='Set debug mode.')

    # 服务端口（覆盖配置文件中的端口）
    parser.add_argument('--grpc-port', type=str, default='0',
                        help='Please set the gRPC port of interviewer service.')
    parser.add_argument('--http-port', type=str, default='0',
                        help='Please set the HTTP port of interviewer service.')

    # TODO: 当认证准备好时添加认证参数
    # parser.add_argument('--identityFile', type=str, default='',
    #                    help='Please set identity file for interviewer service.')
    # parser.add_argument('--password', type=str, default='',
    #                    help='Please input password to decrypt the identity file')

    # 证书目录（用于SSL/TLS）
    parser.add_argument('--certDir', type=str, default='',
                        help='Please set cert directory of interviewer service.')

    return parser.parse_args()


# =================主程序入口=================
def run(args):
    """
    应用程序主入口点
    Args:
        args: 命令行参数对象
    """
    # 如果启用调试模式，尝试连接到调试器
    if args.debug:
        try:
            import pydevd  # PyCharm/IntelliJ的远程调试器
            # 连接到本地调试服务器
            pydevd.settrace('localhost', port=54321, stdoutToServer=True,
                            stderrToServer=True, suspend=False)
        except ImportError:
            # 如果pydevd不可用，记录警告但继续运行
            logging.warning("pydevd not available for debugging")

    # 加载配置文件
    config = Config(args.config)
    config.config_log()  # 配置日志系统

    # 使用命令行参数覆盖配置文件中的设置
    if args.certDir:
        config.update_cert_dir(args.certDir)  # 更新证书目录
    if getattr(args, 'grpc_port', '0') != '0':
        config.update_grpc_port(args.grpc_port)  # 更新gRPC端口
    if getattr(args, 'http_port', '0') != '0':
        config.update_http_port(args.http_port)  # 更新HTTP端口

    # TODO: 当认证准备好时处理身份验证
    # identity, blockAddress = deserialize_identity(args.password, args.identityFile)
    # if identity is None:
    #     return

    # 确保数据库已迁移到最新版本
    try:
        ensure_migrated(config.get_database(), ALL_MODELS)
        logging.info("Database migration completed successfully")
    except Exception as e:
        logging.error(f"Database migration failed: {e}")
        return  # 数据库迁移失败，退出程序

    # 创建并启动服务运行器
    runner = Runner(config=config)

    try:
        # 运行异步服务器
        asyncio.run(runner.serve())
    except KeyboardInterrupt:
        # 用户按Ctrl+C停止服务
        logging.info("Server stopped by user")
    except Exception as e:
        # 服务器运行时出现错误
        logging.error(f"Server error: {e}")


# =================程序启动点=================
if __name__ == '__main__':
    # 解析命令行参数并运行主程序
    run(parse_args())