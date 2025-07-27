from interviewer.domain.mapper.entities import UserDO, UserStateDO, database_proxy
from interviewer.domain.model.user import User, UserState


def queryUser(did: str) -> User | None:
    do = UserDO.get_or_none(UserDO.did == did)
    return User.from_orm(do) if do else None


def saveUser(user: User):
    return UserDO.create(**user.dict())


def updateUser(user: User):
    user = UserDO(**user.dict())
    return user.save()


def deleteUser(did) -> int:
    with database_proxy.atomic():
        sql = UserDO.delete().where(UserDO.did == did)
        count = sql.execute()
        sql = UserStateDO.delete().where(UserStateDO.did == did)
        sql.execute()
    return count


def queryState(did: str):
    do = UserStateDO.get_or_none(UserStateDO.did == did)
    return UserState.from_orm(do) if do else None


def updateState(state: UserState):
    state = UserStateDO(**state.dict())
    return state.save()


def saveState(state: UserState):
    return UserStateDO.create(**state.dict())