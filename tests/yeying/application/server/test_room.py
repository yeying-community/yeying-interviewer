"""
面试间服务单元测试
测试文件：tests/yeying/application/server/test_room.py
"""

import unittest
import uuid
from datetime import datetime

import yeying.api.interviewer.room_pb2 as room_pb2
import yeying.api.common.message_pb2 as message_pb2
from interviewer.application.server.room import RoomService
from interviewer.domain.model.room import Room
from interviewer.domain.mapper.entities import InterviewRoomDO
from interviewer.infrastructure.db.instance import Instance
from interviewer.tool.date import getCurrentUtcString
from tests.yeying.common.test_config import setup_test_database, setup_test_logging


class RoomServiceTestCase(unittest.TestCase):
    instance = Instance(setup_test_database([InterviewRoomDO]))

    @classmethod
    def setUpClass(cls):
        setup_test_logging()

    def test_room_crud_operations(self):
        """测试 Room 的完整 CRUD 操作"""
        # 准备测试数据
        did = "did:example:user1"
        room_id = str(uuid.uuid4())

        room_service = RoomService(authenticate=None, db_instance=self.instance)
        room_service.deleteRoom(did=did, room_id=room_id)  # 清理

        # 创建房间
        room = Room(
            roomId=room_id,
            did=did,
            roomName="Python面试间",
            resumeId="resume-001",
            jobInfoId="job-001",
            contextId="context-001",
            experienceId="experience-001",
            knowledgeId="knowledge-001",
            createdAt=getCurrentUtcString(),
            updatedAt=getCurrentUtcString(),
            signature="signature1"
        )

        # 测试添加
        room_service.addRoom(room)

        # 测试获取
        retrieved_room = room_service.getRoom(did=did, room_id=room_id)
        self.assertEqual(retrieved_room.roomName, "Python面试间")
        self.assertEqual(retrieved_room.resumeId, "resume-001")

        # 测试列表
        rooms = room_service.getRoomsByDid(did=did)
        self.assertEqual(len(rooms), 1)

        # 测试分页
        page_rooms, total = room_service.listRoomsByDid(did=did, page=1, page_size=10)
        self.assertEqual(len(page_rooms), 1)
        self.assertEqual(total, 1)

        # 测试更新
        room.roomName = "Python高级面试间"
        room.jobInfoId = "job-002"
        room.updatedAt = getCurrentUtcString()
        room_service.updateRoom(room)

        updated_room = room_service.getRoom(did=did, room_id=room_id)
        self.assertEqual(updated_room.roomName, "Python高级面试间")
        self.assertEqual(updated_room.jobInfoId, "job-002")

        # 测试删除
        room_service.deleteRoom(did=did, room_id=room_id)
        deleted_room = room_service.getRoom(did=did, room_id=room_id)
        self.assertIsNone(deleted_room)

    def test_grpc_interface(self):
        """测试 gRPC 接口"""
        did = "did:example:grpc-test"
        room_id = str(uuid.uuid4())

        room_service = RoomService(authenticate=None, db_instance=self.instance)
        room_service.deleteRoom(did=did, room_id=room_id)  # 清理

        header = message_pb2.MessageHeader()

        # 测试创建
        room_metadata = room_pb2.RoomMetadata(
            roomId=room_id,
            did=did,
            roomName="gRPC测试房间",
            resumeId="resume-001",
            jobInfoId="job-001",
            contextId="context-001",
            experienceId="experience-001",
            knowledgeId="knowledge-001",
            createdAt=getCurrentUtcString(),
            updatedAt=getCurrentUtcString(),
            signature="signature"
        )

        create_request = room_pb2.CreateRoomRequest(
            header=header,
            body=room_pb2.CreateRoomRequestBody(room=room_metadata)
        )

        create_response = room_service.Create(create_request, None)
        self.assertEqual(create_response.body.status.code, 200)
        self.assertEqual(create_response.body.room.roomName, "gRPC测试房间")

        # 测试获取
        get_request = room_pb2.GetRoomRequest(
            header=header,
            body=room_pb2.GetRoomRequestBody(roomId=room_id, did=did)
        )

        get_response = room_service.Get(get_request, None)
        self.assertEqual(get_response.body.status.code, 200)
        self.assertEqual(get_response.body.room.roomId, room_id)

        # 测试更新
        update_request = room_pb2.UpdateRoomRequest(
            header=header,
            body=room_pb2.UpdateRoomRequestBody(
                roomId=room_id,
                did=did,
                roomName="更新的房间",
                jobInfoId="job-002",
                contextId="context-002",
                experienceId="experience-002",
                knowledgeId="knowledge-002"
            )
        )

        update_response = room_service.Update(update_request, None)
        self.assertEqual(update_response.body.status.code, 200)
        self.assertEqual(update_response.body.room.roomName, "更新的房间")

        # 测试列表
        list_request = room_pb2.ListRoomsRequest(
            header=header,
            body=room_pb2.ListRoomsRequestBody(did=did, page=1, pageSize=10)
        )

        list_response = room_service.List(list_request, None)
        self.assertEqual(list_response.body.status.code, 200)
        self.assertEqual(len(list_response.body.rooms), 1)

        # 测试删除
        delete_request = room_pb2.DeleteRoomRequest(
            header=header,
            body=room_pb2.DeleteRoomRequestBody(roomId=room_id, did=did)
        )

        delete_response = room_service.Delete(delete_request, None)
        self.assertEqual(delete_response.body.status.code, 200)

    def test_business_validation(self):
        """测试业务验证"""
        room_id = str(uuid.uuid4())
        did = "did:example:validation-test"

        # 测试有效房间
        valid_room = Room(
            roomId=room_id,
            did=did,
            roomName="有效房间",
            resumeId="resume-001",
            jobInfoId=None,  # 可选字段
            contextId="context-001",
            experienceId="experience-001",
            knowledgeId="knowledge-001"
        )
        valid_room.validate()  # 应该不抛出异常

        # 测试无效房间
        with self.assertRaises(ValueError):
            invalid_room = Room(
                roomId="",  # 空ID
                did="",
                roomName="",
                resumeId="",
                contextId="",  # 必需参数
                experienceId="",  # 必需参数
                knowledgeId=""  # 必需参数
            )
            invalid_room.validate()

        # 测试权限
        self.assertTrue(valid_room.is_owned_by(did))
        self.assertFalse(valid_room.is_owned_by("other-did"))

    def test_error_scenarios(self):
        """测试错误场景"""
        did = "did:example:error-test"
        room_id = str(uuid.uuid4())

        room_service = RoomService(authenticate=None, db_instance=self.instance)

        # 测试获取不存在的房间
        non_existent = room_service.getRoom(did=did, room_id=room_id)
        self.assertIsNone(non_existent)

        # 测试重复创建
        room = Room(
            roomId=room_id,
            did=did,
            roomName="测试房间",
            resumeId="resume-001",
            contextId="context-001",
            experienceId="experience-001",
            knowledgeId="knowledge-001",
            createdAt=getCurrentUtcString(),
            updatedAt=getCurrentUtcString(),
            signature="signature"
        )

        room_service.addRoom(room)
        with self.assertRaises((ValueError, RuntimeError)):
            room_service.addRoom(room)  # 重复创建

        # 测试权限控制
        other_did = "did:example:other-user"
        unauthorized = room_service.getRoom(did=other_did, room_id=room_id)
        self.assertIsNone(unauthorized)

        # 清理
        room_service.deleteRoom(did=did, room_id=room_id)


if __name__ == '__main__':
    unittest.main()