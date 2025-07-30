"""
面试间领域模型
文件：interviewer/domain/model/room.py
"""

from dataclasses import dataclass
from typing import Optional
import uuid


@dataclass
class Room:
    """面试间领域模型"""

    roomId: str
    did: str
    roomName: str
    resumeId: str
    contextId: str
    experienceId: str
    knowledgeId: str
    jobInfoId: Optional[str] = None
    createdAt: Optional[str] = None
    updatedAt: Optional[str] = None
    signature: Optional[str] = None

    def validate(self) -> None:
        """验证房间数据的有效性"""
        errors = []

        # 验证必填字段
        if not self.roomId or not self.roomId.strip():
            errors.append("roomId不能为空")

        if not self.did or not self.did.strip():
            errors.append("did不能为空")

        if not self.roomName or not self.roomName.strip():
            errors.append("roomName不能为空")

        if not self.resumeId or not self.resumeId.strip():
            errors.append("resumeId不能为空")

        # 验证必填的知识库ID
        if not self.contextId or not self.contextId.strip():
            errors.append("contextId不能为空")

        if not self.experienceId or not self.experienceId.strip():
            errors.append("experienceId不能为空")

        if not self.knowledgeId or not self.knowledgeId.strip():
            errors.append("knowledgeId不能为空")

        # 验证ID格式（UUID）
        try:
            uuid.UUID(self.roomId)
        except ValueError:
            errors.append("roomId必须是有效的UUID格式")

        if errors:
            raise ValueError(f"房间数据验证失败: {'; '.join(errors)}")

    def is_owned_by(self, did: str) -> bool:
        """检查房间是否属于指定用户"""
        return self.did == did

    def update_basic_info(self, room_name: str, job_info_id: Optional[str] = None) -> None:
        """更新房间基本信息"""
        if not room_name or not room_name.strip():
            raise ValueError("房间名称不能为空")

        self.roomName = room_name.strip()
        self.jobInfoId = job_info_id

    def update_knowledge_ids(self, context_id: str, experience_id: str, knowledge_id: str) -> None:
        """更新知识库ID"""
        if not context_id or not context_id.strip():
            raise ValueError("contextId不能为空")
        if not experience_id or not experience_id.strip():
            raise ValueError("experienceId不能为空")
        if not knowledge_id or not knowledge_id.strip():
            raise ValueError("knowledgeId不能为空")

        self.contextId = context_id
        self.experienceId = experience_id
        self.knowledgeId = knowledge_id

    def __eq__(self, other) -> bool:
        """比较两个房间是否相等"""
        if not isinstance(other, Room):
            return False
        return (
            self.roomId == other.roomId and
            self.did == other.did and
            self.roomName == other.roomName and
            self.resumeId == other.resumeId and
            self.jobInfoId == other.jobInfoId and
            self.contextId == other.contextId and
            self.experienceId == other.experienceId and
            self.knowledgeId == other.knowledgeId
        )