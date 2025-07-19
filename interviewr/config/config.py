import logging
import logging.handlers
import os
import toml
from pydantic import BaseModel
from typing import Optional

# 导入数据库配置类
from interviewr.infrastructure.database.instance import DatabaseConfig


# =================配置模型类=================
class LogConfig(BaseModel):
    """日志配置模型类"""
    filename: str = "log/interviewer.log"    # 日志文件路径
    level: str = "INFO"                      # 日志级别
    # 日志格式：时间戳 [模块名][进程ID] 日志级别: 消息内容
    format: str = "%(asctime)s [%(name)s][%(process)5d] %(levelname)s: %(message)s"
    maxBytes: int = 536870912                # 单个日志文件最大字节数（512MB）
    backupCount: int = 15                    # 保留的备份文件数量


class CredentialConfig(BaseModel):
    """认证/凭证配置模型类"""
    enable: bool = False        # 是否启用认证功能
    certDir: str = "cert"       # 证书文件存放目录


class ServerConfig(BaseModel):
    """服务器配置模型类"""
    grpc_port: int = 9401      # gRPC服务器监听端口
    http_port: int = 8741      # HTTP服务器监听端口
    cacheDir: str = "cache"    # 缓存文件存放目录


# =================主配置管理器类=================
class Config:
    """面试官应用的配置管理器"""
    def __init__(self, config_file: str):
        """
        初始化配置管理器
        Args:
            config_file: 配置文件路径
        """
        self.config_file = config_file  # 保存配置文件路径
        self.config_data = self._load_config()  # 加载配置数据

        # 初始化各个配置部分，使用Pydantic模型进行数据验证
        # 如果配置文件中没有对应section，则使用空字典，会应用默认值
        self.log_config = LogConfig(**self.config_data.get('log', {}))
        self.credential_config = CredentialConfig(**self.config_data.get('credential', {}))
        self.server_config = ServerConfig(**self.config_data.get('server', {}))
        self.database_config = DatabaseConfig(**self.config_data.get('database', {}))

    def _load_config(self) -> dict:
        """
        从TOML文件加载配置
        Returns:
            dict: 配置数据字典
        Raises:
            FileNotFoundError: 配置文件不存在
        """
        # 检查配置文件是否存在
        if not os.path.exists(self.config_file):
            raise FileNotFoundError(f"Configuration file not found: {self.config_file}")

        # 读取并解析TOML配置文件
        with open(self.config_file, 'r', encoding='utf-8') as f:
            return toml.load(f)

    # =================配置获取方法=================
    def get_log(self) -> LogConfig:
        """获取日志配置"""
        return self.log_config

    def get_credential(self) -> CredentialConfig:
        """获取认证配置"""
        return self.credential_config

    def get_server(self) -> ServerConfig:
        """获取服务器配置"""
        return self.server_config

    def get_database(self) -> DatabaseConfig:
        """获取数据库配置"""
        return self.database_config

    # =================配置更新方法=================
    def update_grpc_port(self, port: str):
        """
        更新gRPC服务器端口
        Args:
            port: 端口号字符串
        """
        # 检查端口是否有效且不为'0'
        if port and port != '0':
            self.server_config.grpc_port = int(port)

    def update_http_port(self, port: str):
        """
        更新HTTP服务器端口
        Args:
            port: 端口号字符串
        """
        # 检查端口是否有效且不为'0'
        if port and port != '0':
            self.server_config.http_port = int(port)

    def update_cert_dir(self, cert_dir: str):
        """
        更新证书目录
        Args:
            cert_dir: 证书目录路径
        """
        if cert_dir:
            self.credential_config.certDir = cert_dir

    # =================日志配置方法=================
    def config_log(self):
        """根据配置设置日志系统"""
        log_config = self.get_log()

        # 确保日志目录存在
        log_dir = os.path.dirname(log_config.filename)
        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir, exist_ok=True)

        # 获取根日志记录器
        logger = logging.getLogger()
        # 设置日志级别（将字符串转换为logging模块的常量）
        logger.setLevel(getattr(logging, log_config.level.upper()))

        # 移除现有的处理器，避免重复配置
        for handler in logger.handlers[:]:
            logger.removeHandler(handler)

        # 添加轮转文件处理器
        # RotatingFileHandler：当文件达到maxBytes时自动轮转，保留backupCount个备份
        file_handler = logging.handlers.RotatingFileHandler(
            log_config.filename,  # 日志文件路径
            maxBytes=log_config.maxBytes,  # 最大文件大小
            backupCount=log_config.backupCount,  # 备份文件数量
            encoding='utf-8'  # 文件编码
        )
        # 设置文件处理器的格式
        file_handler.setFormatter(logging.Formatter(log_config.format))
        logger.addHandler(file_handler)

        # 添加控制台处理器（用于开发调试）
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(logging.Formatter(log_config.format))
        logger.addHandler(console_handler)

        # 记录配置成功的信息
        logging.info("Logging configured successfully")