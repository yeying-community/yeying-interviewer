# 导入必要的模块
from datetime import datetime
from peewee import CharField, TextField, DateTimeField, ForeignKeyField, UUIDField
import uuid
from interviewr.infrastructure.database.instance import BaseModel


# =================数据库架构迁移模型=================
class SchemaMigrationDO(BaseModel):
    """数据库架构迁移跟踪表 - 记录数据库版本变更历史"""
    version = CharField(max_length=50, help_text="版本号")  # 数据库架构版本标识
    created_at = DateTimeField(default=datetime.now, help_text="创建时间")  # 迁移执行时间

    class Meta:
        table_name = 'schema_migrations'


# =================用户模型（待实现）=================
# TODO: 用户表
class UserDO(BaseModel):
    """用户数据对象（TODO: 当认证系统准备好时实现）"""
    # TODO: 实现用户表结构
    # 预期字段：
    # - user_id: 用户唯一标识
    # - username: 用户名
    # - email: 邮箱地址
    # - password_hash: 密码哈希
    # - is_active: 是否激活
    # - created_at: 创建时间
    # - updated_at: 更新时间
    pass


# =================简历模型（待实现）=================
# TODO: 简历表
class ResumeDO(BaseModel):
    """简历数据对象（TODO: 实现）"""
    # TODO: 实现简历表结构
    # 预期字段：
    # - resume_id: 简历UUID主键
    # - user_id: 关联用户ID（外键）
    # - name: 简历名称
    # - content: 简历完整内容
    # - skills: 技能标签（JSON格式）
    # - experience: 工作经历（JSON格式）
    # - education: 教育背景（JSON格式）
    # - projects: 项目经历（JSON格式）
    # - created_at: 创建时间
    # - updated_at: 更新时间
    pass


# =================职位信息模型=================
class JobInfoDO(BaseModel):
    """职位信息数据对象 - 存储公司和职位的详细信息"""

    # 主键：使用UUID确保全局唯一性
    job_info_id = UUIDField(primary_key=True, default=uuid.uuid4, help_text="职位信息ID")

    # 公司和职位基本信息
    company = CharField(max_length=255, help_text="公司名称")  # 如"字节跳动"、"阿里巴巴"
    job_title = CharField(max_length=255, help_text="职位名称")  # 如"高级后端工程师"、"前端开发"
    job_description = TextField(null=True, help_text="职位描述")  # 完整的JD（Job Description）

    # 时间戳
    created_at = DateTimeField(default=datetime.now, help_text="创建时间")
    updated_at = DateTimeField(default=datetime.now, help_text="更新时间")

    class Meta:
        table_name = 'job_info'


# =================面试间模型=================
class InterviewRoomDO(BaseModel):
    """面试间数据对象 - 代表一个配置好的面试环境"""

    # 主键：面试间的唯一标识
    room_id = UUIDField(primary_key=True, default=uuid.uuid4, help_text="面试间UUID")

    # 用户关联（当前使用字符串，待UserDO实现后改为外键）
    did = CharField(max_length=36, help_text="用户DID")  # TODO: 改为外键当UserDO实现后
    # DID可能是去中心化标识符（Decentralized Identifier）

    # 简历关联（当前使用字符串，待ResumeDO实现后改为外键）
    resume_id = CharField(max_length=36, help_text="简历ID")  # TODO: 改为外键当ResumeDO实现后

    # RAG系统集成
    collection_id = CharField(
        max_length=36,
        unique=True,
        help_text="RAG返回的集合ID（唯一约束防重复绑定）"
    )
    # collection_id是RAG（检索增强生成）系统中的文档集合标识
    # 唯一约束确保一个集合只能绑定到一个面试间

    # 面试间配置
    name = CharField(
        max_length=100,
        help_text="面试间名称（用户自定义，如'字节跳动-后端终面'）"
    )

    # 职位信息关联（可选外键）
    job_info = ForeignKeyField(
        JobInfoDO,
        null=True,
        backref='interview_rooms',
        help_text="关联职位信息表（可选）"
    )
    # backref='interview_rooms' 允许从JobInfoDO反向访问相关的面试间
    # null=True 表示职位信息是可选的，支持通用面试间

    # 时间戳
    created_at = DateTimeField(default=datetime.now, help_text="创建时间")
    updated_at = DateTimeField(default=datetime.now, help_text="更新时间")

    class Meta:
        table_name = 'interview_room'
        # 创建索引优化查询性能
        indexes = (
            # 按用户DID查询面试间（非唯一索引）
            (('did',), False),  # False表示非唯一索引
            # collection_id唯一索引（防止重复绑定）
            (('collection_id',), True),  # True表示唯一索引
        )


# =================面试会话模型（待实现）=================
# TODO: 面试会话表
class InterviewSessionDO(BaseModel):
    """面试会话数据对象（TODO: 实现）"""
    # TODO: 实现面试会话表结构
    # 预期字段：
    # - session_id: 会话UUID主键
    # - room_id: 关联面试间ID（外键）
    # - session_type: 会话类型（技术面/经验面/HR面）
    # - session_name: 会话名称
    # - status: 会话状态（创建/进行中/暂停/完成/取消）
    # - questions: 问题列表（JSON格式）
    # - answers: 回答记录（JSON格式）
    # - score: 面试评分
    # - feedback: 面试反馈
    # - started_at: 开始时间
    # - completed_at: 完成时间
    # - created_at: 创建时间
    # - updated_at: 更新时间
    pass


# =================模型导出=================
# 导出当前已实现的模型供数据库迁移使用
ALL_MODELS = [
    SchemaMigrationDO,  # 架构迁移表（系统核心）
    JobInfoDO,  # 职位信息表（业务基础）
    InterviewRoomDO,  # 面试间表（业务核心）
]

# TODO: 当其他表实现后，添加到ALL_MODELS中
# 完整的模型列表应该是：
# ALL_MODELS = [
#     SchemaMigrationDO,    # 系统表
#     UserDO,               # 用户管理
#     ResumeDO,             # 简历管理
#     JobInfoDO,            # 职位信息
#     InterviewRoomDO,      # 面试间
#     InterviewSessionDO    # 面试会话
# ]
