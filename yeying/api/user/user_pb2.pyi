from google.protobuf import wrappers_pb2 as _wrappers_pb2
from yeying.api.common import message_pb2 as _message_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UserStatusEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    USER_STATUS_UNKNOWN: _ClassVar[UserStatusEnum]
    USER_STATUS_ACTIVE: _ClassVar[UserStatusEnum]
    USER_STATUS_OFFLINE: _ClassVar[UserStatusEnum]
    USER_STATUS_DISABLE: _ClassVar[UserStatusEnum]
    USER_STATUS_LOCK: _ClassVar[UserStatusEnum]
    USER_STATUS_UNVERIFIED: _ClassVar[UserStatusEnum]
    USER_STATUS_DELETED: _ClassVar[UserStatusEnum]
    USER_STATUS_DORMANT: _ClassVar[UserStatusEnum]
    USER_STATUS_FREEZE: _ClassVar[UserStatusEnum]
    USER_STATUS_AUDIT: _ClassVar[UserStatusEnum]
    USER_STATUS_REFUSED: _ClassVar[UserStatusEnum]

class UserRoleEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    USER_ROLE_UNKNOWN: _ClassVar[UserRoleEnum]
    USER_ROLE_OWNER: _ClassVar[UserRoleEnum]
    USER_ROLE_NORMAL: _ClassVar[UserRoleEnum]
USER_STATUS_UNKNOWN: UserStatusEnum
USER_STATUS_ACTIVE: UserStatusEnum
USER_STATUS_OFFLINE: UserStatusEnum
USER_STATUS_DISABLE: UserStatusEnum
USER_STATUS_LOCK: UserStatusEnum
USER_STATUS_UNVERIFIED: UserStatusEnum
USER_STATUS_DELETED: UserStatusEnum
USER_STATUS_DORMANT: UserStatusEnum
USER_STATUS_FREEZE: UserStatusEnum
USER_STATUS_AUDIT: UserStatusEnum
USER_STATUS_REFUSED: UserStatusEnum
USER_ROLE_UNKNOWN: UserRoleEnum
USER_ROLE_OWNER: UserRoleEnum
USER_ROLE_NORMAL: UserRoleEnum

class UpdateStatusRequest(_message.Message):
    __slots__ = ["header", "body"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: UpdateStatusRequestBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[UpdateStatusRequestBody, _Mapping]] = ...) -> None: ...

class UpdateStatusRequestBody(_message.Message):
    __slots__ = ["did", "status"]
    DID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    did: str
    status: UserStatusEnum
    def __init__(self, did: _Optional[str] = ..., status: _Optional[_Union[UserStatusEnum, str]] = ...) -> None: ...

class UpdateStatusResponse(_message.Message):
    __slots__ = ["header", "body"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: UpdateStatusResponseBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[UpdateStatusResponseBody, _Mapping]] = ...) -> None: ...

class UpdateStatusResponseBody(_message.Message):
    __slots__ = ["status"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: _message_pb2.ResponseStatus
    def __init__(self, status: _Optional[_Union[_message_pb2.ResponseStatus, _Mapping]] = ...) -> None: ...

class UserListRequest(_message.Message):
    __slots__ = ["header", "body"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: UserListRequestBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[UserListRequestBody, _Mapping]] = ...) -> None: ...

class UserListRequestBody(_message.Message):
    __slots__ = ["pageIndex", "pageSize"]
    PAGEINDEX_FIELD_NUMBER: _ClassVar[int]
    PAGESIZE_FIELD_NUMBER: _ClassVar[int]
    pageIndex: _wrappers_pb2.Int32Value
    pageSize: _wrappers_pb2.Int32Value
    def __init__(self, pageIndex: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., pageSize: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ...) -> None: ...

class UserListResponse(_message.Message):
    __slots__ = ["header", "body"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: UserListResponseBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[UserListResponseBody, _Mapping]] = ...) -> None: ...

class UserListResponseBody(_message.Message):
    __slots__ = ["status", "list", "total"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    LIST_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    status: _message_pb2.ResponseStatus
    list: _containers.RepeatedCompositeFieldContainer[UserDetail]
    total: int
    def __init__(self, status: _Optional[_Union[_message_pb2.ResponseStatus, _Mapping]] = ..., list: _Optional[_Iterable[_Union[UserDetail, _Mapping]]] = ..., total: _Optional[int] = ...) -> None: ...

class UserMetadata(_message.Message):
    __slots__ = ["did", "name", "avatar", "createdAt", "updatedAt", "signature", "telephone", "email"]
    DID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    AVATAR_FIELD_NUMBER: _ClassVar[int]
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    UPDATEDAT_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    TELEPHONE_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    did: str
    name: str
    avatar: str
    createdAt: str
    updatedAt: str
    signature: str
    telephone: str
    email: str
    def __init__(self, did: _Optional[str] = ..., name: _Optional[str] = ..., avatar: _Optional[str] = ..., createdAt: _Optional[str] = ..., updatedAt: _Optional[str] = ..., signature: _Optional[str] = ..., telephone: _Optional[str] = ..., email: _Optional[str] = ...) -> None: ...

class UserState(_message.Message):
    __slots__ = ["owner", "did", "role", "status", "createdAt", "updatedAt", "signature"]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    DID_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    UPDATEDAT_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    owner: str
    did: str
    role: UserRoleEnum
    status: UserStatusEnum
    createdAt: str
    updatedAt: str
    signature: str
    def __init__(self, owner: _Optional[str] = ..., did: _Optional[str] = ..., role: _Optional[_Union[UserRoleEnum, str]] = ..., status: _Optional[_Union[UserStatusEnum, str]] = ..., createdAt: _Optional[str] = ..., updatedAt: _Optional[str] = ..., signature: _Optional[str] = ...) -> None: ...

class AddUserRequest(_message.Message):
    __slots__ = ["header", "body"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: AddUserRequestBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[AddUserRequestBody, _Mapping]] = ...) -> None: ...

class AddUserRequestBody(_message.Message):
    __slots__ = ["user"]
    USER_FIELD_NUMBER: _ClassVar[int]
    user: UserMetadata
    def __init__(self, user: _Optional[_Union[UserMetadata, _Mapping]] = ...) -> None: ...

class AddUserResponse(_message.Message):
    __slots__ = ["header", "body"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: AddUserResponseBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[AddUserResponseBody, _Mapping]] = ...) -> None: ...

class AddUserResponseBody(_message.Message):
    __slots__ = ["status", "user"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    status: _message_pb2.ResponseStatus
    user: UserMetadata
    def __init__(self, status: _Optional[_Union[_message_pb2.ResponseStatus, _Mapping]] = ..., user: _Optional[_Union[UserMetadata, _Mapping]] = ...) -> None: ...

class UpdateUserRequest(_message.Message):
    __slots__ = ["header", "body"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: UpdateUserRequestBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[UpdateUserRequestBody, _Mapping]] = ...) -> None: ...

class UpdateUserRequestBody(_message.Message):
    __slots__ = ["user"]
    USER_FIELD_NUMBER: _ClassVar[int]
    user: UserMetadata
    def __init__(self, user: _Optional[_Union[UserMetadata, _Mapping]] = ...) -> None: ...

class UpdateUserResponse(_message.Message):
    __slots__ = ["header", "body"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: UpdateUserResponseBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[UpdateUserResponseBody, _Mapping]] = ...) -> None: ...

class UpdateUserResponseBody(_message.Message):
    __slots__ = ["status", "user"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    status: _message_pb2.ResponseStatus
    user: UserMetadata
    def __init__(self, status: _Optional[_Union[_message_pb2.ResponseStatus, _Mapping]] = ..., user: _Optional[_Union[UserMetadata, _Mapping]] = ...) -> None: ...

class DeleteUserRequest(_message.Message):
    __slots__ = ["header"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ...) -> None: ...

class DeleteUserResponse(_message.Message):
    __slots__ = ["header", "body"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: DeleteUserResponseBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[DeleteUserResponseBody, _Mapping]] = ...) -> None: ...

class DeleteUserResponseBody(_message.Message):
    __slots__ = ["status"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: _message_pb2.ResponseStatus
    def __init__(self, status: _Optional[_Union[_message_pb2.ResponseStatus, _Mapping]] = ...) -> None: ...

class UserDetailRequest(_message.Message):
    __slots__ = ["header"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ...) -> None: ...

class UserDetailResponse(_message.Message):
    __slots__ = ["header", "body"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: UserDetailResponseBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[UserDetailResponseBody, _Mapping]] = ...) -> None: ...

class UserDetailResponseBody(_message.Message):
    __slots__ = ["status", "detail"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DETAIL_FIELD_NUMBER: _ClassVar[int]
    status: _message_pb2.ResponseStatus
    detail: UserDetail
    def __init__(self, status: _Optional[_Union[_message_pb2.ResponseStatus, _Mapping]] = ..., detail: _Optional[_Union[UserDetail, _Mapping]] = ...) -> None: ...

class UserDetail(_message.Message):
    __slots__ = ["user", "state"]
    USER_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    user: UserMetadata
    state: UserState
    def __init__(self, user: _Optional[_Union[UserMetadata, _Mapping]] = ..., state: _Optional[_Union[UserState, _Mapping]] = ...) -> None: ...
