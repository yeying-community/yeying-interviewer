"""
面试间数据访问层
文件：interviewer/infrastructure/repository/room_repository.py
"""

from typing import Optional, List, Tuple
from interviewer.domain.model.room import Room
from interviewer.domain.mapper.entities import InterviewRoomDO
from interviewer.infrastructure.db.instance import Instance


class RoomRepository:
    """面试间数据访问层"""

    def __init__(self, db_instance: Instance):
        self.db_instance = db_instance

    def add(self, room: Room) -> None:
        """添加面试间"""
        room_do = self._to_do(room)
        try:
            with self.db_instance.database.atomic():
                room_do.save(force_insert=True)
        except Exception as e:
            raise RuntimeError(f"添加面试间失败: {str(e)}")

    def get_by_id(self, did: str, room_id: str) -> Optional[Room]:
        """根据ID获取面试间"""
        try:
            room_do = InterviewRoomDO.get(
                (InterviewRoomDO.roomId == room_id) &
                (InterviewRoomDO.did == did)
            )
            return self._to_domain(room_do)
        except InterviewRoomDO.DoesNotExist:
            return None

    def get_by_did(self, did: str) -> List[Room]:
        """获取用户的所有面试间"""
        room_dos = InterviewRoomDO.select().where(InterviewRoomDO.did == did)
        return [self._to_domain(room_do) for room_do in room_dos]

    def list_by_did(self, did: str, page: int, page_size: int) -> Tuple[List[Room], int]:
        """分页获取用户的面试间"""
        # 获取总数
        total = InterviewRoomDO.select().where(InterviewRoomDO.did == did).count()

        # 分页查询
        offset = (page - 1) * page_size
        room_dos = (InterviewRoomDO
                    .select()
                    .where(InterviewRoomDO.did == did)
                    .order_by(InterviewRoomDO.createdAt.desc())
                    .offset(offset)
                    .limit(page_size))

        rooms = [self._to_domain(room_do) for room_do in room_dos]
        return rooms, total

    def update(self, room: Room) -> None:
        """更新面试间"""
        try:
            with self.db_instance.database.atomic():
                # 先查询确保记录存在且属于该用户
                existing = InterviewRoomDO.get(
                    (InterviewRoomDO.roomId == room.roomId) &
                    (InterviewRoomDO.did == room.did)
                )

                # 更新字段
                update_fields = {
                    'roomName': room.roomName,
                    'jobInfoId': room.jobInfoId,
                    'contextId': room.contextId,
                    'experienceId': room.experienceId,
                    'knowledgeId': room.knowledgeId,
                    'updatedAt': room.updatedAt,
                    'signature': room.signature
                }

                # 执行更新
                InterviewRoomDO.update(**update_fields).where(
                    (InterviewRoomDO.roomId == room.roomId) &
                    (InterviewRoomDO.did == room.did)
                ).execute()

        except InterviewRoomDO.DoesNotExist:
            raise ValueError(f"面试间不存在或无权限访问: {room.roomId}")
        except Exception as e:
            raise RuntimeError(f"更新面试间失败: {str(e)}")

    def delete(self, did: str, room_id: str) -> bool:
        """删除面试间"""
        try:
            with self.db_instance.database.atomic():
                deleted_count = InterviewRoomDO.delete().where(
                    (InterviewRoomDO.roomId == room_id) &
                    (InterviewRoomDO.did == did)
                ).execute()
                return deleted_count > 0
        except Exception as e:
            raise RuntimeError(f"删除面试间失败: {str(e)}")

    def _to_domain(self, room_do: InterviewRoomDO) -> Room:
        """DO实体转换为领域模型"""
        return Room(
            roomId=room_do.roomId,
            did=room_do.did,
            roomName=room_do.roomName,
            resumeId=room_do.resumeId,
            jobInfoId=room_do.jobInfoId,
            contextId=room_do.contextId,
            experienceId=room_do.experienceId,
            knowledgeId=room_do.knowledgeId,
            createdAt=room_do.createdAt,
            updatedAt=room_do.updatedAt,
            signature=room_do.signature
        )

    def _to_do(self, room: Room) -> InterviewRoomDO:
        """领域模型转换为DO实体"""
        return InterviewRoomDO(
            roomId=room.roomId,
            did=room.did,
            roomName=room.roomName,
            resumeId=room.resumeId,
            jobInfoId=room.jobInfoId,
            contextId=room.contextId,
            experienceId=room.experienceId,
            knowledgeId=room.knowledgeId,
            createdAt=room.createdAt,
            updatedAt=room.updatedAt,
            signature=room.signature
        )