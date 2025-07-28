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
from interviewer.infrastructure.db.instance import Instance
from interviewer.tool.date import getCurrentUtcString
from tests.yeying.common.test_config import setup_test_database, setup_test_logging


class RoomServiceTestCase(unittest.TestCase):
    instance = Instance(setup_test_database())

    @classmethod
    def setUpClass(cls):
        setup_test_logging()

    def test_room_crud_operations(self):
        """测试 Room 的完整 CRUD 操作"""
        # 准备测试数据
        did1 = "did:example:user1"
        did2 = "did:example:user2"
        room_id1 = str(uuid.uuid4())
        room_id2 = str(uuid.uuid4())
        room_id3 = str(uuid.uuid4())

        # 创建服务实例
        room_service = RoomService(db_instance=self.instance)

        # 清理测试数据
        room_service.deleteRoom(did=did1, room_id=room_id1)
        room_service.deleteRoom(did=did1, room_id=room_id2)
        room_service.deleteRoom(did=did2, room_id=room_id3)

        # 创建房间对象
        room1 = Room(
            roomId=room_id1,
            did=did1,
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

        room2 = Room(
            roomId=room_id2,
            did=did1,
            roomName="Java面试间",
            resumeId="resume-002",
            jobInfoId="job-002",
            createdAt=getCurrentUtcString(),
            updatedAt=getCurrentUtcString(),
            signature="signature2"
        )

        room3 = Room(
            roomId=room_id3,
            did=did2,  # 不同用户
            roomName="Go面试间",
            resumeId="resume-003",
            createdAt=getCurrentUtcString(),
            updatedAt=getCurrentUtcString(),
            signature="signature3"
        )

        # === 测试添加房间 ===
        room_service.addRoom(room1)
        room_service.addRoom(room2)
        room_service.addRoom(room3)

        # === 测试获取单个房间 ===
        retrieved_room = room_service.getRoom(did=did1, room_id=room_id1)
        self.assertEqual(retrieved_room, room1)

        # === 测试获取用户所有房间 ===
        rooms_user1 = room_service.getRoomsByDid(did=did1)
        self.assertEqual(len(rooms_user1), 2)

        rooms_user2 = room_service.getRoomsByDid(did=did2)
        self.assertEqual(len(rooms_user2), 1)
        self.assertEqual(rooms_user2[0], room3)

        # === 测试分页查询 ===
        page1_rooms, total = room_service.listRoomsByDid(did=did1, page=1, page_size=1)
        self.assertEqual(len(page1_rooms), 1)
        self.assertEqual(total, 2)

        page2_rooms, total = room_service.listRoomsByDid(did=did1, page=2, page_size=1)
        self.assertEqual(len(page2_rooms), 1)
        self.assertEqual(total, 2)

        # === 测试更新房间 ===
        updated_room1 = Room(
            roomId=room_id1,
            did=did1,
            roomName="Python高级面试间",  # 更新名称
            resumeId="resume-001-updated",
            jobInfoId="job-001-updated",
            contextId="context-001-updated",
            experienceId="experience-001-updated",
            knowledgeId="knowledge-001-updated",
            createdAt=room1.createdAt,  # 保持创建时间
            updatedAt=getCurrentUtcString(),
            signature="signature1-updated"
        )

        room_service.updateRoom(updated_room1)
        retrieved_updated_room = room_service.getRoom(did=did1, room_id=room_id1)
        self.assertEqual(retrieved_updated_room.roomName, "Python高级面试间")
        self.assertEqual(retrieved_updated_room.resumeId, "resume-001-updated")

        # === 测试权限控制 ===
        # 用户1不能获取用户2的房间
        other_user_room = room_service.getRoom(did=did1, room_id=room_id3)
        self.assertIsNone(other_user_room)

        # === 测试删除房间 ===
        room_service.deleteRoom(did=did1, room_id=room_id1)
        room_service.deleteRoom(did=did1, room_id=room_id2)
        room_service.deleteRoom(did=did2, room_id=room_id3)

        # 验证删除后获取不到
        deleted_room = room_service.getRoom(did=did1, room_id=room_id1)
        self.assertIsNone(deleted_room)

        # 验证用户房间列表为空
        empty_rooms = room_service.getRoomsByDid(did=did1)
        self.assertEqual(len(empty_rooms), 0)

    def test_grpc_interface(self):
        """测试 gRPC 接口"""
        did = "did:example:grpc-test"
        room_id = str(uuid.uuid4())
        request_id = str(uuid.uuid4())

        room_service = RoomService(db_instance=self.instance)

        # 清理测试数据
        room_service.deleteRoom(did=did, room_id=room_id)

        # 创建消息头
        header = message_pb2.MessageHeader(
            requestId=request_id,
            timestamp=str(int(datetime.now().timestamp())),
            version="1.0"
        )

        # === 测试创建房间 gRPC 接口 ===
        room_metadata = room_pb2.RoomMetadata(
            roomId=room_id,
            did=did,
            roomName="gRPC测试房间",
            resumeId="grpc-resume-001",
            jobInfoId="grpc-job-001",
            createdAt=getCurrentUtcString(),
            updatedAt=getCurrentUtcString(),
            signature="grpc-signature"
        )

        create_request = room_pb2.CreateRoomRequest(
            header=header,
            body=room_pb2.CreateRoomRequestBody(room=room_metadata)
        )

        create_response = room_service.Create(create_request, None)
        self.assertEqual(create_response.body.status.code, 200)
        self.assertEqual(create_response.body.room.roomId, room_id)
        self.assertEqual(create_response.body.room.roomName, "gRPC测试房间")

        # === 测试获取房间 gRPC 接口 ===
        get_request = room_pb2.GetRoomRequest(
            header=header,
            body=room_pb2.GetRoomRequestBody(roomId=room_id, did=did)
        )

        get_response = room_service.Get(get_request, None)
        self.assertEqual(get_response.body.status.code, 200)
        self.assertEqual(get_response.body.room.roomId, room_id)
        self.assertEqual(get_response.body.room.roomName, "gRPC测试房间")

        # === 测试更新房间 gRPC 接口 ===
        update_request = room_pb2.UpdateRoomRequest(
            header=header,
            body=room_pb2.UpdateRoomRequestBody(
                roomId=room_id,
                did=did,
                roomName="更新的gRPC房间",
                jobInfoId="updated-job-001"
            )
        )

        update_response = room_service.Update(update_request, None)
        self.assertEqual(update_response.body.status.code, 200)
        self.assertEqual(update_response.body.room.roomName, "更新的gRPC房间")
        self.assertEqual(update_response.body.room.jobInfoId, "updated-job-001")

        # === 测试列出房间 gRPC 接口 ===
        list_request = room_pb2.ListRoomsRequest(
            header=header,
            body=room_pb2.ListRoomsRequestBody(
                did=did,
                page=1,
                pageSize=10
            )
        )

        list_response = room_service.List(list_request, None)
        self.assertEqual(list_response.body.status.code, 200)
        self.assertEqual(len(list_response.body.rooms), 1)
        self.assertEqual(list_response.body.total, 1)
        self.assertEqual(list_response.body.rooms[0].roomId, room_id)

        # === 测试删除房间 gRPC 接口 ===
        delete_request = room_pb2.DeleteRoomRequest(
            header=header,
            body=room_pb2.DeleteRoomRequestBody(roomId=room_id, did=did)
        )

        delete_response = room_service.Delete(delete_request, None)
        self.assertEqual(delete_response.body.status.code, 200)

        # 验证删除后获取不到
        get_after_delete = room_service.Get(get_request, None)
        self.assertEqual(get_after_delete.body.status.code, 404)

    def test_error_scenarios(self):
        """测试错误场景"""
        did = "did:example:error-test"
        room_id = str(uuid.uuid4())

        room_service = RoomService(db_instance=self.instance)

        # === 测试获取不存在的房间 ===
        non_existent_room = room_service.getRoom(did=did, room_id=room_id)
        self.assertIsNone(non_existent_room)

        # === 测试重复创建房间 ===
        room = Room(
            roomId=room_id,
            did=did,
            roomName="重复测试房间",
            resumeId="resume-duplicate",
            createdAt=getCurrentUtcString(),
            updatedAt=getCurrentUtcString(),
            signature="duplicate-signature"
        )

        # 第一次创建成功
        room_service.addRoom(room)

        # 第二次创建相同ID的房间应该抛出异常
        with self.assertRaises((ValueError, RuntimeError)):
            room_service.addRoom(room)

        # === 测试无效数据验证 ===
        invalid_room = Room(
            roomId="",  # 空ID
            did="",  # 空DID
            roomName="",  # 空名称
            resumeId=""  # 空简历ID
        )

        with self.assertRaises(ValueError):
            invalid_room.validate()

        # === 测试权限错误 ===
        # 尝试获取其他用户的房间应该返回None
        other_did = "did:example:other-user"
        unauthorized_room = room_service.getRoom(did=other_did, room_id=room_id)
        self.assertIsNone(unauthorized_room)

        # 清理测试数据
        room_service.deleteRoom(did=did, room_id=room_id)

    def test_room_business_logic(self):
        """测试房间业务逻辑"""
        room_id = str(uuid.uuid4())
        did = "did:example:business-test"

        # === 测试房间验证逻辑 ===
        valid_room = Room(
            roomId=room_id,
            did=did,
            roomName="有效的房间名称",
            resumeId="resume-123"
        )

        # 应该不抛出异常
        valid_room.validate()

        # === 测试所有权检查 ===
        self.assertTrue(valid_room.is_owned_by(did))
        self.assertFalse(valid_room.is_owned_by("other-did"))

        # === 测试更新基本信息 ===
        valid_room.update_basic_info(
            room_name="更新后的房间名称",
            job_info_id="new-job-123"
        )

        self.assertEqual(valid_room.roomName, "更新后的房间名称")
        self.assertEqual(valid_room.jobInfoId, "new-job-123")

        # === 测试更新知识库ID ===
        valid_room.update_knowledge_ids(
            context_id="context-123",
            experience_id="exp-123",
            knowledge_id="knowledge-123"
        )

        self.assertEqual(valid_room.contextId, "context-123")
        self.assertEqual(valid_room.experienceId, "exp-123")
        self.assertEqual(valid_room.knowledgeId, "knowledge-123")

        # === 测试无效数据更新 ===
        with self.assertRaises(ValueError):
            valid_room.update_basic_info(room_name="")  # 空名称

        with self.assertRaises(ValueError):
            valid_room.update_basic_info(room_name="   ")  # 只有空格


if __name__ == '__main__':
    unittest.main()