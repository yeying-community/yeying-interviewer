import yeying.api.user.user_pb2 as user_pb2
from interviewer.domain.model.user import User, UserState


def convertUserRoleTo(role):
    return user_pb2.UserRoleEnum.Name(role)


def convertUserRoleFrom(s):
    return user_pb2.UserRoleEnum.Value(s)


def convertUserStatusTo(status):
    return user_pb2.UserStatusEnum.Name(status)


def convertUserStatusFrom(s):
    return user_pb2.UserStatusEnum.Value(s)


def listUserRole():
    return [r for r in user_pb2.UserRoleEnum if r > 0]


def convertUserRoleTo(role):
    return user_pb2.UserRoleEnum.Name(role)


def convertUserRoleFrom(s):
    return user_pb2.UserRoleEnum.Value(s)


def convertUserFrom(u: User) -> user_pb2.UserMetadata:
    if u is None:
        return None

    return user_pb2.UserMetadata(
        did=u.did,
        name=u.name,
        avatar=u.avatar,
        createdAt=u.createdAt,
        updatedAt=u.updatedAt,
        signature=u.signature,
    )


def convertUserTo(u: user_pb2.UserMetadata) -> User:
    if u is None:
        return None

    return User(
        did=u.did,
        name=u.name,
        avatar=u.avatar,
        createdAt=u.createdAt,
        updatedAt=u.updatedAt,
        signature=u.signature,
    )


def convertUserStateFrom(u: UserState) -> user_pb2.UserState:
    if u is None:
        return None

    return user_pb2.UserState(
        owner=u.owner,
        did=u.did,
        status=user_pb2.UserStatusEnum.Value(u.status),
        role=user_pb2.UserRoleEnum.Value(u.role),
        createdAt=u.createdAt,
        updatedAt=u.updatedAt,
        signature=u.signature,
    )


def convertUserStateTo(u: user_pb2.UserState) -> UserState:
    if u is None:
        return None

    return UserState(
        owner=u.owner,
        did=u.did,
        status=user_pb2.UserStatusEnum.Name(u.status),
        role=user_pb2.UserRoleEnum.Name(u.role),
        createdAt=u.createdAt,
        updatedAt=u.updatedAt,
        signature=u.signature,
    )
