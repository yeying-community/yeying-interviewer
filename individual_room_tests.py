"""
面试间服务完全独立的单个接口测试
每个测试方法完全独立，可以单独运行
测试文件：tests/yeying/application/server/individual_room_tests.py
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


class SingleRoomTest(unittest.TestCase):

    def get_service_and_data(self):
        """获取服务实例和测试数据"""
        instance = Instance(setup_test_database([InterviewRoomDO]))
        did = f"did:example:test-{uuid.uuid4().hex[:8]}"
        room_id = str(uuid.uuid4())
        room_service = RoomService(authenticate=None, db_instance=instance)
        return room_service, did, room_id, instance

    def print_all_rooms(self, room_service, title="数据库状态", current_did=None):
        """打印数据库中所有房间"""
        print(f"\n--- {title} ---")
        try:
            # 方法1：直接查询SQLite数据库获取所有房间
            db_path = '/tmp/test.sqlite'
            all_rooms = []

            import sqlite3
            import os
            if os.path.exists(db_path):
                conn = sqlite3.connect(db_path)
                cursor = conn.cursor()

                # 查询所有房间数据
                cursor.execute("SELECT * FROM interview_rooms")
                rows = cursor.fetchall()

                if rows:
                    print(f"数据库中发现 {len(rows)} 个房间:")
                    # 获取列名
                    cursor.execute("PRAGMA table_info(interview_rooms)")
                    columns = cursor.fetchall()
                    col_names = [col[1] for col in columns]  # col[1] 是列名

                    for row in rows:
                        # 创建一个字典来更好地显示数据
                        room_data = dict(zip(col_names, row))
                        print(f"  - 房间ID: {room_data.get('room_id', 'N/A')}")
                        print(f"    DID: {room_data.get('did', 'N/A')}")
                        print(f"    房间名: {room_data.get('room_name', 'N/A')}")
                        print(f"    创建时间: {room_data.get('created_at', 'N/A')}")
                        print(f"    更新时间: {room_data.get('updated_at', 'N/A')}")
                        print()
                else:
                    print("数据库表中没有房间记录")

                conn.close()
            else:
                print("数据库文件不存在")

            # 方法2：如果提供了当前DID，也通过服务查询验证
            if current_did:
                print(f"通过服务查询当前DID ({current_did}) 的房间:")
                try:
                    rooms = room_service.getRoomsByDid(did=current_did)
                    if rooms:
                        print(f"  服务查询到 {len(rooms)} 个房间:")
                        for room in rooms:
                            print(f"  - {room.roomName} (ID: {room.roomId})")
                    else:
                        print(f"  服务查询：当前DID没有房间")
                except Exception as e:
                    print(f"  服务查询失败: {e}")

        except Exception as e:
            print(f"查询数据库状态出错: {e}")
            import traceback
            traceback.print_exc()
        print("-" * 50)

    def test_01_create_room_only(self):
        """只测试创建房间接口"""
        print(f"\n【测试01】创建房间")

        room_service, did, room_id, instance = self.get_service_and_data()
        print(f"DID: {did}")
        print(f"房间ID: {room_id}")

        self.print_all_rooms(room_service, "创建前数据库状态", did)

        # 创建房间
        room = Room(
            roomId=room_id,
            did=did,
            roomName="测试房间-创建",
            resumeId="resume-001",
            jobInfoId="job-001",
            contextId="context-001",
            experienceId="experience-001",
            knowledgeId="knowledge-001",
            createdAt=getCurrentUtcString(),
            updatedAt=getCurrentUtcString(),
            signature="signature1"
        )

        # 执行创建
        room_service.addRoom(room)
        print("房间创建完成")

        self.print_all_rooms(room_service, "创建后数据库状态", did)

        # 验证创建成功
        retrieved_room = room_service.getRoom(did=did, room_id=room_id)
        self.assertIsNotNone(retrieved_room)
        self.assertEqual(retrieved_room.roomName, "测试房间-创建")

        print("✓ 创建房间测试通过")

    def test_02_get_room_only(self):
        """只测试获取房间接口"""
        print(f"\n【测试02】获取房间")

        room_service, did, room_id, instance = self.get_service_and_data()

        # 先创建一个房间用于测试获取
        room = Room(
            roomId=room_id,
            did=did,
            roomName="测试房间-获取",
            resumeId="resume-002",
            jobInfoId="job-002",
            contextId="context-002",
            experienceId="experience-002",
            knowledgeId="knowledge-002",
            createdAt=getCurrentUtcString(),
            updatedAt=getCurrentUtcString(),
            signature="signature2"
        )
        room_service.addRoom(room)

        self.print_all_rooms(room_service, "获取前数据库状态", did)

        # 测试获取
        retrieved_room = room_service.getRoom(did=did, room_id=room_id)

        print(f"获取到的房间信息:")
        print(f"  房间名: {retrieved_room.roomName}")
        print(f"  简历ID: {retrieved_room.resumeId}")
        print(f"  工作ID: {retrieved_room.jobInfoId}")

        self.assertIsNotNone(retrieved_room)
        self.assertEqual(retrieved_room.roomName, "测试房间-获取")
        self.assertEqual(retrieved_room.resumeId, "resume-002")

        print("✓ 获取房间测试通过")

    def test_03_update_room_only(self):
        """只测试更新房间接口"""
        print(f"\n【测试03】更新房间")

        room_service, did, room_id, instance = self.get_service_and_data()

        # 先创建一个房间用于测试更新
        room = Room(
            roomId=room_id,
            did=did,
            roomName="原始房间名",
            resumeId="resume-003",
            jobInfoId="job-003",
            contextId="context-003",
            experienceId="experience-003",
            knowledgeId="knowledge-003",
            createdAt=getCurrentUtcString(),
            updatedAt=getCurrentUtcString(),
            signature="signature3"
        )
        room_service.addRoom(room)

        self.print_all_rooms(room_service, "更新前数据库状态", did)

        # 更新房间
        room.roomName = "更新后的房间名"
        room.jobInfoId = "job-003-updated"
        room.updatedAt = getCurrentUtcString()

        room_service.updateRoom(room)
        print("房间更新完成")

        self.print_all_rooms(room_service, "更新后数据库状态", did)

        # 验证更新成功
        updated_room = room_service.getRoom(did=did, room_id=room_id)
        self.assertEqual(updated_room.roomName, "更新后的房间名")
        self.assertEqual(updated_room.jobInfoId, "job-003-updated")

        print("✓ 更新房间测试通过")

    def test_04_list_rooms_only(self):
        """只测试房间列表接口"""
        print(f"\n【测试04】获取房间列表")

        room_service, did, room_id, instance = self.get_service_and_data()

        # 创建多个房间用于测试列表
        for i in range(3):
            test_room_id = str(uuid.uuid4())
            room = Room(
                roomId=test_room_id,
                did=did,
                roomName=f"列表测试房间-{i + 1}",
                resumeId=f"resume-00{i + 1}",
                jobInfoId=f"job-00{i + 1}",
                contextId=f"context-00{i + 1}",
                experienceId=f"experience-00{i + 1}",
                knowledgeId=f"knowledge-00{i + 1}",
                createdAt=getCurrentUtcString(),
                updatedAt=getCurrentUtcString(),
                signature=f"signature{i + 1}"
            )
            room_service.addRoom(room)
            print(f"创建房间 {i + 1}: {room.roomName}")

        self.print_all_rooms(room_service, "创建多个房间后数据库状态", did)

        # 测试获取列表
        rooms = room_service.getRoomsByDid(did=did)
        print(f"获取到 {len(rooms)} 个房间")

        # 测试分页列表
        page_rooms, total = room_service.listRoomsByDid(did=did, page=1, page_size=2)
        print(f"分页查询: 第1页，每页2条，总共{total}条")

        for room in page_rooms:
            print(f"  - {room.roomName}")

        self.assertEqual(len(rooms), 3)
        self.assertEqual(total, 3)
        self.assertEqual(len(page_rooms), 2)  # 第一页只有2条

        print("✓ 房间列表测试通过")

    def test_05_delete_room_only(self):
        """只测试删除房间接口"""
        print(f"\n【测试05】删除房间")

        room_service, did, room_id, instance = self.get_service_and_data()

        # 先创建一个房间用于测试删除
        room = Room(
            roomId=room_id,
            did=did,
            roomName="待删除的房间",
            resumeId="resume-005",
            jobInfoId="job-005",
            contextId="context-005",
            experienceId="experience-005",
            knowledgeId="knowledge-005",
            createdAt=getCurrentUtcString(),
            updatedAt=getCurrentUtcString(),
            signature="signature5"
        )
        room_service.addRoom(room)

        self.print_all_rooms(room_service, "删除前数据库状态", did)

        # 执行删除
        room_service.deleteRoom(did=did, room_id=room_id)
        print("房间删除完成")

        self.print_all_rooms(room_service, "删除后数据库状态", did)

        # 验证删除成功
        deleted_room = room_service.getRoom(did=did, room_id=room_id)
        self.assertIsNone(deleted_room)

        print("✓ 删除房间测试通过")

    def test_06_grpc_create_only(self):
        """只测试gRPC创建接口"""
        print(f"\n【测试06】gRPC创建房间")

        room_service, did, room_id, instance = self.get_service_and_data()

        self.print_all_rooms(room_service, "gRPC创建前数据库状态", did)

        header = message_pb2.MessageHeader()
        room_metadata = room_pb2.RoomMetadata(
            roomId=room_id,
            did=did,
            roomName="gRPC创建的房间",
            resumeId="resume-006",
            jobInfoId="job-006",
            contextId="context-006",
            experienceId="experience-006",
            knowledgeId="knowledge-006",
            createdAt=getCurrentUtcString(),
            updatedAt=getCurrentUtcString(),
            signature="signature6"
        )

        create_request = room_pb2.CreateRoomRequest(
            header=header,
            body=room_pb2.CreateRoomRequestBody(room=room_metadata)
        )

        # 执行gRPC创建
        create_response = room_service.Create(create_request, None)
        print(f"gRPC响应状态码: {create_response.body.status.code}")
        print(f"gRPC响应消息: {create_response.body.status.message}")
        print(f"创建的房间名: {create_response.body.room.roomName}")

        self.print_all_rooms(room_service, "gRPC创建后数据库状态", did)

        self.assertEqual(create_response.body.status.code, 200)
        self.assertEqual(create_response.body.room.roomName, "gRPC创建的房间")

        print("✓ gRPC创建房间测试通过")

    def test_07_grpc_get_only(self):
        """只测试gRPC获取接口"""
        print(f"\n【测试07】gRPC获取房间")

        room_service, did, room_id, instance = self.get_service_and_data()

        # 先通过gRPC创建一个房间用于测试获取
        header = message_pb2.MessageHeader()
        room_metadata = room_pb2.RoomMetadata(
            roomId=room_id,
            did=did,
            roomName="gRPC获取测试房间",
            resumeId="resume-007",
            jobInfoId="job-007",
            contextId="context-007",
            experienceId="experience-007",
            knowledgeId="knowledge-007",
            createdAt=getCurrentUtcString(),
            updatedAt=getCurrentUtcString(),
            signature="signature7"
        )

        create_request = room_pb2.CreateRoomRequest(
            header=header,
            body=room_pb2.CreateRoomRequestBody(room=room_metadata)
        )
        room_service.Create(create_request, None)

        self.print_all_rooms(room_service, "gRPC获取前数据库状态", did)

        # 测试gRPC获取
        get_request = room_pb2.GetRoomRequest(
            header=header,
            body=room_pb2.GetRoomRequestBody(roomId=room_id, did=did)
        )

        get_response = room_service.Get(get_request, None)
        print(f"gRPC获取响应状态码: {get_response.body.status.code}")
        print(f"获取到的房间名: {get_response.body.room.roomName}")
        print(f"获取到的房间ID: {get_response.body.room.roomId}")

        self.assertEqual(get_response.body.status.code, 200)
        self.assertEqual(get_response.body.room.roomId, room_id)
        self.assertEqual(get_response.body.room.roomName, "gRPC获取测试房间")

        print("✓ gRPC获取房间测试通过")

    def test_08_grpc_update_only(self):
        """只测试gRPC更新接口"""
        print(f"\n【测试08】gRPC更新房间")

        room_service, did, room_id, instance = self.get_service_and_data()

        # 先创建房间用于测试更新
        header = message_pb2.MessageHeader()
        room_metadata = room_pb2.RoomMetadata(
            roomId=room_id,
            did=did,
            roomName="gRPC更新前的房间",
            resumeId="resume-008",
            jobInfoId="job-008",
            contextId="context-008",
            experienceId="experience-008",
            knowledgeId="knowledge-008",
            createdAt=getCurrentUtcString(),
            updatedAt=getCurrentUtcString(),
            signature="signature8"
        )

        create_request = room_pb2.CreateRoomRequest(
            header=header,
            body=room_pb2.CreateRoomRequestBody(room=room_metadata)
        )
        room_service.Create(create_request, None)

        self.print_all_rooms(room_service, "gRPC更新前数据库状态", did)

        # 测试gRPC更新
        update_request = room_pb2.UpdateRoomRequest(
            header=header,
            body=room_pb2.UpdateRoomRequestBody(
                roomId=room_id,
                did=did,
                roomName="gRPC更新后的房间",
                jobInfoId="job-008-updated",
                contextId="context-008-updated",
                experienceId="experience-008-updated",
                knowledgeId="knowledge-008-updated"
            )
        )

        update_response = room_service.Update(update_request, None)
        print(f"gRPC更新响应状态码: {update_response.body.status.code}")
        print(f"更新后的房间名: {update_response.body.room.roomName}")

        self.print_all_rooms(room_service, "gRPC更新后数据库状态", did)

        self.assertEqual(update_response.body.status.code, 200)
        self.assertEqual(update_response.body.room.roomName, "gRPC更新后的房间")

        print("✓ gRPC更新房间测试通过")

    def test_09_grpc_list_only(self):
        """只测试gRPC列表接口"""
        print(f"\n【测试09】gRPC房间列表")

        room_service, did, room_id, instance = self.get_service_and_data()

        # 创建几个房间用于测试列表
        header = message_pb2.MessageHeader()
        for i in range(2):
            test_room_id = str(uuid.uuid4())
            room_metadata = room_pb2.RoomMetadata(
                roomId=test_room_id,
                did=did,
                roomName=f"gRPC列表房间-{i + 1}",
                resumeId=f"resume-00{i + 9}",
                jobInfoId=f"job-00{i + 9}",
                contextId=f"context-00{i + 9}",
                experienceId=f"experience-00{i + 9}",
                knowledgeId=f"knowledge-00{i + 9}",
                createdAt=getCurrentUtcString(),
                updatedAt=getCurrentUtcString(),
                signature=f"signature{i + 9}"
            )

            create_request = room_pb2.CreateRoomRequest(
                header=header,
                body=room_pb2.CreateRoomRequestBody(room=room_metadata)
            )
            room_service.Create(create_request, None)
            print(f"创建gRPC房间 {i + 1}: gRPC列表房间-{i + 1}")

        self.print_all_rooms(room_service, "gRPC列表查询前数据库状态", did)

        # 测试gRPC列表
        list_request = room_pb2.ListRoomsRequest(
            header=header,
            body=room_pb2.ListRoomsRequestBody(did=did, page=1, pageSize=10)
        )

        list_response = room_service.List(list_request, None)
        print(f"gRPC列表响应状态码: {list_response.body.status.code}")
        print(f"返回房间数量: {len(list_response.body.rooms)}")

        for room in list_response.body.rooms:
            print(f"  - {room.roomName} (ID: {room.roomId})")

        self.assertEqual(list_response.body.status.code, 200)
        self.assertGreaterEqual(len(list_response.body.rooms), 2)

        print("✓ gRPC房间列表测试通过")

    def test_10_grpc_delete_only(self):
        """只测试gRPC删除接口"""
        print(f"\n【测试10】gRPC删除房间")

        room_service, did, room_id, instance = self.get_service_and_data()

        # 先创建房间用于测试删除
        header = message_pb2.MessageHeader()
        room_metadata = room_pb2.RoomMetadata(
            roomId=room_id,
            did=did,
            roomName="gRPC待删除房间",
            resumeId="resume-010",
            jobInfoId="job-010",
            contextId="context-010",
            experienceId="experience-010",
            knowledgeId="knowledge-010",
            createdAt=getCurrentUtcString(),
            updatedAt=getCurrentUtcString(),
            signature="signature10"
        )

        create_request = room_pb2.CreateRoomRequest(
            header=header,
            body=room_pb2.CreateRoomRequestBody(room=room_metadata)
        )
        room_service.Create(create_request, None)

        self.print_all_rooms(room_service, "gRPC删除前数据库状态", did)

        # 测试gRPC删除
        delete_request = room_pb2.DeleteRoomRequest(
            header=header,
            body=room_pb2.DeleteRoomRequestBody(roomId=room_id, did=did)
        )

        delete_response = room_service.Delete(delete_request, None)
        print(f"gRPC删除响应状态码: {delete_response.body.status.code}")

        self.print_all_rooms(room_service, "gRPC删除后数据库状态", did)

        self.assertEqual(delete_response.body.status.code, 200)

        # 验证删除成功
        get_request = room_pb2.GetRoomRequest(
            header=header,
            body=room_pb2.GetRoomRequestBody(roomId=room_id, did=did)
        )

        try:
            get_response = room_service.Get(get_request, None)
            # 如果能获取到，说明删除失败
            if get_response.body.status.code == 200:
                self.fail("房间删除后仍能获取到，删除失败")
        except Exception:
            # 获取不到是正常的
            pass

        print("✓ gRPC删除房间测试通过")

    def test_11_view_database_status(self):
        """单独的数据库状态查看测试"""
        print(f"\n【测试11】查看当前数据库状态")

        room_service, did, room_id, instance = self.get_service_and_data()

        # 创建一个房间，这样数据库就不会是空的
        room = Room(
            roomId=room_id,
            did=did,
            roomName="数据库状态查看房间",
            resumeId="resume-status",
            jobInfoId="job-status",
            contextId="context-status",
            experienceId="experience-status",
            knowledgeId="knowledge-status",
            createdAt=getCurrentUtcString(),
            updatedAt=getCurrentUtcString(),
            signature="signature-status"
        )
        room_service.addRoom(room)
        print("创建了一个示例房间用于展示数据库状态")

        self.print_all_rooms(room_service, "当前数据库完整状态", did)

        print("✓ 数据库状态查看完成")


if __name__ == '__main__':
    unittest.main(verbosity=2)