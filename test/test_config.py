import os
import tempfile
import pytest
import toml
from interviewr.config.config import Config, LogConfig, ServerConfig, CredentialConfig


class TestConfig:
    """配置管理器测试类"""
    
    @pytest.fixture
    def sample_config_data(self):
        """创建示例配置数据"""
        return {
            'log': {
                'filename': 'test_log.log',
                'level': 'DEBUG',
                'maxBytes': 1024,
                'backupCount': 3
            },
            'server': {
                'grpc_port': 8080,
                'http_port': 8081,
                'cacheDir': 'test_cache'
            },
            'credential': {
                'enable': True,
                'certDir': 'test_cert'
            },
            'database': {
                'type': 'sqlite',
                'name': 'test_db.db'
            }
        }
    
    @pytest.fixture
    def config_file(self, sample_config_data):
        """创建临时配置文件"""
        # 创建临时文件
        fd, path = tempfile.mkstemp(suffix='.toml')
        with os.fdopen(fd, 'w') as f:
            toml.dump(sample_config_data, f)
        
        # 返回文件路径，测试结束后删除
        yield path
        os.unlink(path)
    
    def test_load_config(self, config_file, sample_config_data):
        """测试配置加载功能"""
        # 创建配置管理器实例
        config = Config(config_file)
        
        # 验证配置数据是否正确加载
        assert config.config_data == sample_config_data
        
        # 验证各个配置部分是否正确初始化
        assert config.log_config.filename == sample_config_data['log']['filename']
        assert config.log_config.level == sample_config_data['log']['level']
        assert config.server_config.grpc_port == sample_config_data['server']['grpc_port']
        assert config.server_config.http_port == sample_config_data['server']['http_port']
        assert config.credential_config.enable == sample_config_data['credential']['enable']
        assert config.database_config.type == sample_config_data['database']['type']
    
    def test_file_not_found(self):
        """测试配置文件不存在的情况"""
        with pytest.raises(FileNotFoundError):
            Config('non_existent_file.toml')
    
    def test_get_methods(self, config_file):
        """测试配置获取方法"""
        config = Config(config_file)
        
        # 测试各个get方法
        assert isinstance(config.get_log(), LogConfig)
        assert isinstance(config.get_server(), ServerConfig)
        assert isinstance(config.get_credential(), CredentialConfig)
        assert config.get_database().type == 'sqlite'
    
    def test_update_methods(self, config_file):
        """测试配置更新方法"""
        config = Config(config_file)
        
        # 测试更新gRPC端口
        config.update_grpc_port('9000')
        assert config.server_config.grpc_port == 9000
        
        # 测试更新HTTP端口
        config.update_http_port('8000')
        assert config.server_config.http_port == 8000
        
        # 测试无效端口
        config.update_grpc_port('0')
        assert config.server_config.grpc_port == 9000  # 不应该更改
        
        # 测试更新证书目录
        config.update_cert_dir('new_cert_dir')
        assert config.credential_config.certDir == 'new_cert_dir'