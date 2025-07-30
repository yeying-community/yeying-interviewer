"""
面试间DTO转换函数
文件：interviewer/application/model/room_dto.py
"""

from typing import Optional, List
import yeying.api.interviewer.room_pb2 as room_pb2
import yeying.api.common.message_pb2 as message_pb2
from interviewer.domain.model.room import Room


def convertRoomFrom(room: Room) -> room_pb2.RoomMetadata:
    """从领域模型转换为protobuf消息"""
    if room is None:
        return None

    return room_pb2.RoomMetadata(
        roomId=room.roomId,
        did=room.did,
        roomName=room.roomName,
        resumeId=room.resumeId,
        jobInfoId=room.jobInfoId or "",
        contextId=room.contextId,
        experienceId=room.experienceId,
        knowledgeId=room.knowledgeId,
        createdAt=room.createdAt or "",
        updatedAt=room.updatedAt or "",
        signature=room.signature or ""
    )


def convertRoomTo(room_metadata: room_pb2.RoomMetadata) -> Room:
    """从protobuf消息转换为领域模型"""
    if room_metadata is None:
        return None

    return Room(
        roomId=room_metadata.roomId,
        did=room_metadata.did,
        roomName=room_metadata.roomName,
        resumeId=room_metadata.resumeId,
        jobInfoId=room_metadata.jobInfoId if room_metadata.jobInfoId else None,
        contextId=room_metadata.contextId,
        experienceId=room_metadata.experienceId,
        knowledgeId=room_metadata.knowledgeId,
        createdAt=room_metadata.createdAt if room_metadata.createdAt else None,
        updatedAt=room_metadata.updatedAt if room_metadata.updatedAt else None,
        signature=room_metadata.signature if room_metadata.signature else None
    )


def convertRoomListFrom(rooms: List[Room]) -> List[room_pb2.RoomMetadata]:
    """从领域模型列表转换为protobuf消息列表"""
    if rooms is None:
        return []
    return [convertRoomFrom(room) for room in rooms]


def createResponseStatus(code: int, message: str = "") -> message_pb2.ResponseStatus:
    """创建响应状态"""
    return message_pb2.ResponseStatus(code=code, message=message)


def createRoomFromUpdateRequest(request: room_pb2.UpdateRoomRequest) -> Room:
    """从更新请求创建Room对象"""
    body = request.body
    return Room(
        roomId=body.roomId,
        did=body.did,
        roomName=body.roomName,
        resumeId="",  # 更新时不改变resumeId
        jobInfoId=body.jobInfoId if body.jobInfoId else None,
        contextId=body.contextId,
        experienceId=body.experienceId,
        knowledgeId=body.knowledgeId
    )