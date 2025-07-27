import unittest

from interviewer.domain.manager.user import saveUser, queryUser, deleteUser, queryState, saveState, updateUser, updateState
from interviewer.domain.mapper.entities import UserDO, UserStateDO
from interviewer.domain.model.user import User, UserState
from interviewer.tool.date import getCurrentUtcString
from tests.yeying.common.test_config import setup_test_database, setup_test_logging


def newUser(did: str):
    return User(
        name="name1",
        did=did,
        avatar="avatar1",
        createdAt=getCurrentUtcString(),
        updatedAt=getCurrentUtcString(),
        signature="signature1"
    )


def newUserState(did: str):
    return UserState(
        owner="owner1",
        did=did,
        status="status1",
        role="role1",
        createdAt=getCurrentUtcString(),
        updatedAt=getCurrentUtcString(),
        signature="signature1"
    )


class UsageTestCase(unittest.TestCase):
    setup_test_database([UserDO, UserStateDO])

    @classmethod
    def setUpClass(cls):
        setup_test_logging()

    def test_crud(self):
        did = "did1"

        # 新增
        user = newUser(did=did)
        saveUser(user)
        userState = newUserState(did=did)
        saveState(userState)

        # 查询
        record = queryUser(did=did)
        self.assertEqual(user, record)
        record = queryState(did=did)
        self.assertEqual(userState, record)

        # 更新
        user.name = "name2"
        count = updateUser(user=user)
        self.assertEqual(count, 1)

        userState.status = "status2"
        count = updateState(state=userState)
        self.assertEqual(count, 1)

        record = queryUser(did=did)
        self.assertEqual(user, record)
        self.assertEqual(record.name, "name2")
        record = queryState(did=did)
        self.assertEqual(userState, record)
        self.assertEqual(record.status, "status2")

        # 删除
        count = deleteUser(did=did)
        self.assertEqual(count, 1)

        # 查询
        record = queryUser(did=did)
        self.assertIsNone(record)
        record = queryState(did=did)
        self.assertIsNone(record)


if __name__ == '__main__':
    unittest.main()