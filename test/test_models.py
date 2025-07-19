import pytest
import uuid
from datetime import datetime
from interviewr.domain.models import (
    SchemaMigrationDO, JobInfoDO, InterviewRoomDO, ALL_MODELS
)
from interviewr.infrastructure.database.instance import (
    DatabaseConfig, create_database, database_proxy
)


class TestModels:
    """领域模型测试类"""
    
    @pytest.fixture(scope='class')
    def setup_database(self):
        """设置内存数据库用于测试"""
        # 创建内存数据库配置
        config = DatabaseConfig(type='sqlite', name=':memory:')
        
        # 创建数据库连接
        db = create_database(config)
        
        # 创建表
        db.create_tables(ALL_MODELS)
        
        yield db
        
        # 关闭数据库连接
        db.close()
    
    def test_schema_migration_model(self, setup_database):
        """测试架构迁移模型"""
        # 创建架构迁移记录
        version = '2023-01-01'
        migration = SchemaMigrationDO.create(version=version)
        
        # 验证记录是否正确创建
        assert migration.version == version
        assert isinstance(migration.created_at, datetime)
        
        # 查询记录
        queried = SchemaMigrationDO.get(SchemaMigrationDO.version == version)
        assert queried.version == version
    
    def test_job_info_model(self, setup_database):
        """测试职位信息模型"""
        # 创建职位信息
        job = JobInfoDO.create(
            company='测试公司',
            job_title='测试职位',
            job_description='这是一个测试职位描述'
        )
        
        # 验证记录是否正确创建
        assert isinstance(job.job_info_id, uuid.UUID)
        assert job.company == '测试公司'
        assert job.job_title == '测试职位'
        assert job.job_description == '这是一个测试职位描述'
        assert isinstance(job.created_at, datetime)
        assert isinstance(job.updated_at, datetime)
        
        # 查询记录
        queried = JobInfoDO.get(JobInfoDO.job_info_id == job.job_info_id)
        assert queried.company == '测试公司'
    
    def test_interview_room_model(self, setup_database):
        """测试面试间模型"""
        # 创建职位信息
        job = JobInfoDO.create(
            company='面试公司',
            job_title='面试职位'
        )
        
        # 创建面试间
        room = InterviewRoomDO.create(
            did='test-did-123',
            resume_id='test-resume-123',
            collection_id='test-collection-123',
            name='测试面试间',
            job_info=job
        )
        
        # 验证记录是否正确创建
        assert isinstance(room.room_id, uuid.UUID)
        assert room.did == 'test-did-123'
        assert room.resume_id == 'test-resume-123'
        assert room.collection_id == 'test-collection-123'
        assert room.name == '测试面试间'
        assert room.job_info.job_info_id == job.job_info_id
        assert isinstance(room.created_at, datetime)
        assert isinstance(room.updated_at, datetime)
        
        # 查询记录
        queried = InterviewRoomDO.get(InterviewRoomDO.room_id == room.room_id)
        assert queried.name == '测试面试间'
        
        # 测试反向关系
        assert job.interview_rooms.count() == 1
        assert job.interview_rooms[0].room_id == room.room_id