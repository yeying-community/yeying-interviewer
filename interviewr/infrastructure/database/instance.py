import logging
import os
from contextlib import contextmanager
from typing import List

from peewee import SqliteDatabase, PostgresqlDatabase, MySQLDatabase, OperationalError, Model, Proxy
from playhouse.migrate import SqliteMigrator, PostgresqlMigrator, MySQLMigrator, migrate, SchemaMigrator
from pydantic import BaseModel

# =================全局变量=================
# 全局数据库代理对象，用于延迟初始化数据库连接
database_proxy = Proxy()
# 数据库迁移器，初始化为None
migrator: SchemaMigrator = None

# 当前数据库架构版本
CURRENT_VERSION = "2025-06-28"


# =================配置类=================
class DatabaseConfig(BaseModel):
    """数据库配置类，使用Pydantic进行数据验证"""
    type: str = "sqlite"  # 数据库类型，默认SQLite
    host: str = "localhost"  # 数据库主机地址
    port: int = 5432  # 数据库端口，PostgresSQL默认端口
    user: str = None  # 数据库用户名
    password: str = None  # 数据库密码
    name: str = "data/interviewer.db"  # 数据库名称或文件路径


# =================模型基类=================
class BaseModel(Model):
    """所有数据库模型的基类"""

    class Meta:
        # 使用全局数据库代理，实现延迟绑定
        database = database_proxy


class SchemaMigration(BaseModel):
    """数据库架构迁移跟踪表的模型类"""
    # 该类仅用于迁移检查，实际字段定义在 models.py 中
    
    class Meta:
        # 指定表名
        table_name = 'schema_migrations'


# =================工具函数=================
def ensure_parent_dirs_exist(file_path: str) -> str:
    """
    确保给定文件路径的父目录存在
    Args:
        file_path: 文件路径
    Returns:
        返回原始文件路径
    """
    # 获取文件的父目录路径
    parent_dir = os.path.dirname(file_path)
    # 如果父目录存在且不为空，则创建目录
    if parent_dir and not os.path.exists(parent_dir):
        os.makedirs(parent_dir, exist_ok=True)  # exist_ok=True避免目录已存在时报错
    return file_path


def create_database(config: DatabaseConfig):
    """
    根据配置创建数据库对象
    Args:
        config: 数据库配置对象
    Returns:
        数据库连接对象
    Raises:
        ValueError: 不支持的数据库类型
    """
    global migrator  # 声明使用全局变量

    # 根据数据库类型创建相应的数据库连接和迁移器
    if config.type == 'sqlite':
        # 创建SQLite数据库连接，确保父目录存在
        database = SqliteDatabase(ensure_parent_dirs_exist(config.name))
        database_proxy.initialize(database)  # 初始化数据库代理
        migrator = SqliteMigrator(database)  # 创建SQLite迁移器

    elif config.type == 'postgresql':
        # 创建PostgresSQL数据库连接
        database = PostgresqlDatabase(
            config.name,  # 数据库名
            user=config.user,  # 用户名
            password=config.password,  # 密码
            host=config.host,  # 主机地址
            port=config.port,  # 端口
        )
        database_proxy.initialize(database)
        migrator = PostgresqlMigrator(database)

    elif config.type == 'mysql':
        # 创建MySQL数据库连接
        database = MySQLDatabase(
            config.name,
            user=config.user,
            password=config.password,
            host=config.host,
            port=config.port,
        )
        database_proxy.initialize(database)
        migrator = MySQLMigrator(database)

    else:
        # 不支持的数据库类型
        raise ValueError(f"Unsupported database type: {config.type}")

    # 打开数据库连接
    database.connect()
    
    # 记录日志
    logging.info(f"Database initialized: {config.type}")
    return database


# =================迁移相关函数=================
def alter(schema: SchemaMigration, ops: list, version: str) -> bool:
    """
    执行数据库迁移操作
    Args:
        schema: 架构迁移记录对象
        ops: 迁移操作列表
        version: 目标版本
    Returns:
        bool: 是否还需要继续迁移（当前版本不等于最新版本）
    """
    try:
        # 执行迁移操作
        migrate(*ops)
    except OperationalError as e:
        # 迁移失败，记录错误日志
        logging.error(f"Migration failed: {e}")
        return False

    # 更新版本信息并保存
    schema.version = version
    schema.save()
    logging.info(f"Migrated to version: {version}")

    # 返回是否还需要继续迁移
    return version != CURRENT_VERSION


def perform_migration(schema: SchemaMigration) -> bool:
    """
    执行数据库迁移（如果需要的话）
    Args:
        schema: 架构迁移记录对象
    Returns:
        bool: 迁移是否成功
    """
    # TODO: 在需要时实现具体的迁移逻辑
    logging.info("Migration logic not implemented yet")
    return True


def ensure_migrated(config: DatabaseConfig, tables: List[BaseModel]):
    """
    确保数据库已迁移到最新版本
    Args:
        config: 数据库配置
        tables: 需要创建的表模型列表
    """
    # 创建数据库连接
    database = create_database(config)

    # 检查是否需要创建表
    if not database.table_exists('schema_migrations'):
        # 创建所有表
        database.create_tables(tables)
        # 创建初始的架构迁移记录
        from interviewr.domain.models import SchemaMigrationDO
        SchemaMigrationDO.create(version=CURRENT_VERSION)
        logging.info("Database tables created")

    # 检查是否需要迁移
    try:
        from interviewr.domain.models import SchemaMigrationDO
        # 获取当前的架构版本记录
        schema = SchemaMigrationDO.select().first()
        if schema and schema.version != CURRENT_VERSION:
            # 版本不匹配，执行迁移
            perform_migration(schema)
    except Exception as e:
        # 迁移检查失败，记录警告
        logging.warning(f"Migration check failed: {e}")


# =================数据库实例管理类=================
class DatabaseInstance:
    """数据库实例管理器，用于处理连接和会话"""
    def __init__(self, config: DatabaseConfig = None):
        """
        初始化数据库实例
        Args:
            config: 数据库配置，如果提供则立即初始化数据库
        """
        self.config = config
        self.database = None
        if config:
            # 如果提供了配置，立即创建数据库连接
            self.database = create_database(config)

    @contextmanager
    def transaction(self):
        """
        提供事务上下文管理器，用于包装一系列数据库操作
        Yields:
            database: 数据库连接对象
        Raises:
            RuntimeError: 数据库未初始化
        """
        if not self.database:
            raise RuntimeError("Database not initialized")

        # 使用原子事务包装操作
        with self.database.atomic():
            try:
                yield self.database
            except Exception as e:
                # 事务失败，记录错误并重新抛出异常
                logging.error(f"Database transaction failed: {e}")
                raise

    def close(self):
        """关闭数据库连接"""
        if self.database and not self.database.is_closed():
            self.database.close()
            logging.info("Database connection closed")