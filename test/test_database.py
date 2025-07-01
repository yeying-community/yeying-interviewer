import os
import tempfile
import pytest
from peewee import SqliteDatabase
from interviewr.infrastructure.database.instance import (
    DatabaseConfig, DatabaseInstance, create_database,
    ensure_parent_dirs_exist, database_proxy
)


class TestDatabaseInstance:
    """数据库实例测试类"""
    
    @pytest.fixture
    def temp_db_path(self):
        """创建临时数据库路径"""
        # 创建临时目录
        temp_dir = os.path.join(tempfile.gettempdir(), 'test_db_dir')
        os.makedirs(temp_dir, exist_ok=True)
        
        # 返回临时数据库路径
        db_path = os.path.join(temp_dir, 'test.db')
        yield db_path
        
        # 清理
        if os.path.exists(db_path):
            os.unlink(db_path)
        os.rmdir(temp_dir)
    
    @pytest.fixture
    def db_config(self, temp_db_path):
        """创建数据库配置"""
        return DatabaseConfig(
            type='sqlite',
            name=temp_db_path
        )
    
    def test_ensure_parent_dirs_exist(self, temp_db_path):
        """测试确保父目录存在的功能"""
        # 创建嵌套路径
        nested_path = os.path.join(os.path.dirname(temp_db_path), 'nested', 'path', 'file.db')
        
        # 确保父目录存在
        result = ensure_parent_dirs_exist(nested_path)
        
        # 验证结果
        assert result == nested_path
        assert os.path.exists(os.path.dirname(nested_path))
        
        # 清理
        os.rmdir(os.path.join(os.path.dirname(temp_db_path), 'nested', 'path'))
        os.rmdir(os.path.join(os.path.dirname(temp_db_path), 'nested'))
    
    def test_create_database_sqlite(self, db_config):
        """测试创建SQLite数据库"""
        # 创建数据库
        db = create_database(db_config)
        
        # 验证数据库类型和连接状态
        assert isinstance(db, SqliteDatabase)
        assert not db.is_closed()
        
        # 验证代理是否已初始化
        assert database_proxy.obj is not None
        
        # 关闭数据库连接
        db.close()
    
    def test_database_instance_init(self, db_config):
        """测试数据库实例初始化"""
        # 创建数据库实例
        instance = DatabaseInstance(db_config)
        
        # 验证实例属性
        assert instance.config == db_config
        assert instance.database is not None
        assert not instance.database.is_closed()
        
        # 关闭数据库连接
        instance.close()
    
    def test_database_instance_transaction(self, db_config):
        """测试数据库事务"""
        # 创建数据库实例
        instance = DatabaseInstance(db_config)
        
        # 测试事务上下文管理器
        with instance.transaction() as db:
            assert db is instance.database
            assert not db.is_closed()
        
        # 关闭数据库连接
        instance.close()
    
    def test_database_instance_no_config(self):
        """测试无配置初始化数据库实例"""
        # 创建无配置的数据库实例
        instance = DatabaseInstance()
        
        # 验证实例属性
        assert instance.config is None
        assert instance.database is None
        
        # 测试事务上下文管理器应该抛出异常
        with pytest.raises(RuntimeError):
            with instance.transaction():
                pass