from peewee import CharField, Database, Proxy, Model, TextField, BooleanField, BigIntegerField, DateTimeField, \
    ForeignKeyField, IntegerField
from datetime import datetime

database_proxy: Database = Proxy()


class DbModel(Model):
    class Meta:
        database = database_proxy


class SchemaMigration(DbModel):
    version = CharField()


# 用户模型
class UserDO(DbModel):
    class Meta:
        table_name = 'users'

    did = CharField(primary_key=True, max_length=128)
    name = CharField(null=False, max_length=128)
    avatar = TextField(null=True)
    createdAt = CharField(null=False, column_name="created_at", max_length=64)
    updatedAt = CharField(null=False, column_name="updated_at", max_length=64)
    signature = CharField(null=False, max_length=192)


class UserStateDO(DbModel):
    class Meta:
        table_name = 'user_state'

    owner = CharField(null=False, max_length=128)
    did = CharField(primary_key=True, max_length=128)
    role = CharField(null=False, max_length=64)
    status = CharField(null=False, max_length=64)
    createdAt = CharField(null=False, column_name="created_at", max_length=64)
    updatedAt = CharField(null=False, column_name="updated_at", max_length=64)
    signature = CharField(null=False, max_length=192)


# === 面试官的数据模型 ===

class ResumeDO(DbModel):
    """简历表"""

    class Meta:
        table_name = 'Resume'

    resume_id = CharField(primary_key=True, max_length=36)  # UUID
    did = CharField(null=False, max_length=255)  # 用户DID
    resume_name = CharField(null=False, max_length=100)  # 简历名称
    version = CharField(null=True, max_length=32, default='v1.0')  # 版本号
    file_url = CharField(null=False, max_length=500)  # 文件URL
    prompt_type = CharField(null=True, max_length=64)  # prompt类型
    created_at = DateTimeField(default=datetime.now)  # 创建时间
    updated_at = DateTimeField(default=datetime.now)  # 更新时间


class JobInfoDO(DbModel):
    """职位信息表"""

    class Meta:
        table_name = 'JobInfo'

    job_info_id = CharField(primary_key=True, max_length=36)  # UUID
    company = CharField(null=False, max_length=255)  # 公司名称
    job_title = CharField(null=False, max_length=255)  # 职位名称
    job_description = TextField(null=True)  # 职位描述
    created_at = DateTimeField(default=datetime.now)  # 创建时间
    updated_at = DateTimeField(default=datetime.now)  # 更新时间


class InterviewRoomDO(DbModel):
    """面试间表"""

    class Meta:
        table_name = 'InterviewRoom'

    room_id = CharField(primary_key=True, max_length=36)  # UUID
    did = CharField(null=False, max_length=255)  # 用户DID
    room_name = CharField(null=False, max_length=100)  # 面试间名称

    # 三个知识库ID
    context_id = CharField(null=True, max_length=36)  # 上下文知识库ID
    experience_id = CharField(null=True, max_length=36)  # 用户知识库ID
    knowledge_id = CharField(null=True, max_length=36)  # 应用知识库ID

    created_at = DateTimeField(default=datetime.now)  # 创建时间
    updated_at = DateTimeField(default=datetime.now)  # 更新时间

    # 外键关系
    resume = ForeignKeyField(ResumeDO, field=ResumeDO.resume_id, null=False, backref='interview_rooms')
    job_info = ForeignKeyField(JobInfoDO, field=JobInfoDO.job_info_id, null=True, backref='interview_rooms')


class InterviewSessionDO(DbModel):
    """面试会话表"""

    class Meta:
        table_name = 'InterviewSession'

    session_id = CharField(primary_key=True, max_length=36)  # UUID
    session_name = CharField(null=False, max_length=100)  # 会话名称
    created_at = DateTimeField(default=datetime.now)  # 创建时间
    updated_at = DateTimeField(default=datetime.now)  # 更新时间

    # 外键关系
    room = ForeignKeyField(InterviewRoomDO, field=InterviewRoomDO.room_id, null=False, backref='sessions')


class InterviewSessionRoundDO(DbModel):
    """面试会话轮次表"""

    class Meta:
        table_name = 'InterviewSessionRound'

    round_id = CharField(primary_key=True, max_length=36)  # UUID
    round = IntegerField(null=False)  # 轮次编号
    qa_json_url = CharField(null=True, max_length=255)  # 问答JSON URL
    created_at = DateTimeField(default=datetime.now)  # 创建时间
    updated_at = DateTimeField(default=datetime.now)  # 更新时间

    # 外键关系
    session = ForeignKeyField(InterviewSessionDO, field=InterviewSessionDO.session_id, null=False, backref='rounds')


class InterviewReportDO(DbModel):
    """面试报告表"""

    class Meta:
        table_name = 'InterviewReport'

    report_id = CharField(primary_key=True, max_length=36)  # UUID
    report_name = CharField(null=False, max_length=100)  # 报告名称
    report_json_url = CharField(null=True, max_length=255)  # 报告JSON URL
    summary = TextField(null=True)  # 面试总结
    created_at = DateTimeField(default=datetime.now)  # 创建时间
    updated_at = DateTimeField(default=datetime.now)  # 更新时间

    # 外键关系
    session_round = ForeignKeyField(InterviewSessionRoundDO, field=InterviewSessionRoundDO.round_id, null=False, backref='reports')


class TaskDO(DbModel):
    """任务表"""

    class Meta:
        table_name = 'Task'

    task_id = CharField(primary_key=True, max_length=36)  # UUID
    task_type = CharField(null=True, max_length=64)  # 任务类型
    related_id = CharField(null=True, max_length=36)  # 关联ID
    status = CharField(null=False, max_length=20, default='pending')  # 任务状态
    result_url = CharField(null=True, max_length=255)  # 结果URL
    log = TextField(null=True)  # 日志
    created_at = DateTimeField(default=datetime.now)  # 创建时间
    updated_at = DateTimeField(default=datetime.now)  # 更新时间
