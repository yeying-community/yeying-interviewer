from yeying.api.common import message_pb2 as _message_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RoomMetadata(_message.Message):
    __slots__ = ("roomId", "did", "roomName", "resumeId", "jobInfoId", "contextId", "experienceId", "knowledgeId", "createdAt", "updatedAt", "signature")
    ROOMID_FIELD_NUMBER: _ClassVar[int]
    DID_FIELD_NUMBER: _ClassVar[int]
    ROOMNAME_FIELD_NUMBER: _ClassVar[int]
    RESUMEID_FIELD_NUMBER: _ClassVar[int]
    JOBINFOID_FIELD_NUMBER: _ClassVar[int]
    CONTEXTID_FIELD_NUMBER: _ClassVar[int]
    EXPERIENCEID_FIELD_NUMBER: _ClassVar[int]
    KNOWLEDGEID_FIELD_NUMBER: _ClassVar[int]
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    UPDATEDAT_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    roomId: str
    did: str
    roomName: str
    resumeId: str
    jobInfoId: str
    contextId: str
    experienceId: str
    knowledgeId: str
    createdAt: str
    updatedAt: str
    signature: str
    def __init__(self, roomId: _Optional[str] = ..., did: _Optional[str] = ..., roomName: _Optional[str] = ..., resumeId: _Optional[str] = ..., jobInfoId: _Optional[str] = ..., contextId: _Optional[str] = ..., experienceId: _Optional[str] = ..., knowledgeId: _Optional[str] = ..., createdAt: _Optional[str] = ..., updatedAt: _Optional[str] = ..., signature: _Optional[str] = ...) -> None: ...

class CreateRoomRequest(_message.Message):
    __slots__ = ("header", "body")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: CreateRoomRequestBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[CreateRoomRequestBody, _Mapping]] = ...) -> None: ...

class CreateRoomRequestBody(_message.Message):
    __slots__ = ("room",)
    ROOM_FIELD_NUMBER: _ClassVar[int]
    room: RoomMetadata
    def __init__(self, room: _Optional[_Union[RoomMetadata, _Mapping]] = ...) -> None: ...

class CreateRoomResponse(_message.Message):
    __slots__ = ("header", "body")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: CreateRoomResponseBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[CreateRoomResponseBody, _Mapping]] = ...) -> None: ...

class CreateRoomResponseBody(_message.Message):
    __slots__ = ("status", "room")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ROOM_FIELD_NUMBER: _ClassVar[int]
    status: _message_pb2.ResponseStatus
    room: RoomMetadata
    def __init__(self, status: _Optional[_Union[_message_pb2.ResponseStatus, _Mapping]] = ..., room: _Optional[_Union[RoomMetadata, _Mapping]] = ...) -> None: ...

class GetRoomRequest(_message.Message):
    __slots__ = ("header", "body")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: GetRoomRequestBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[GetRoomRequestBody, _Mapping]] = ...) -> None: ...

class GetRoomRequestBody(_message.Message):
    __slots__ = ("roomId", "did")
    ROOMID_FIELD_NUMBER: _ClassVar[int]
    DID_FIELD_NUMBER: _ClassVar[int]
    roomId: str
    did: str
    def __init__(self, roomId: _Optional[str] = ..., did: _Optional[str] = ...) -> None: ...

class GetRoomResponse(_message.Message):
    __slots__ = ("header", "body")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: GetRoomResponseBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[GetRoomResponseBody, _Mapping]] = ...) -> None: ...

class GetRoomResponseBody(_message.Message):
    __slots__ = ("status", "room")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ROOM_FIELD_NUMBER: _ClassVar[int]
    status: _message_pb2.ResponseStatus
    room: RoomMetadata
    def __init__(self, status: _Optional[_Union[_message_pb2.ResponseStatus, _Mapping]] = ..., room: _Optional[_Union[RoomMetadata, _Mapping]] = ...) -> None: ...

class UpdateRoomRequest(_message.Message):
    __slots__ = ("header", "body")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: UpdateRoomRequestBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[UpdateRoomRequestBody, _Mapping]] = ...) -> None: ...

class UpdateRoomRequestBody(_message.Message):
    __slots__ = ("roomId", "did", "roomName", "jobInfoId", "contextId", "experienceId", "knowledgeId")
    ROOMID_FIELD_NUMBER: _ClassVar[int]
    DID_FIELD_NUMBER: _ClassVar[int]
    ROOMNAME_FIELD_NUMBER: _ClassVar[int]
    JOBINFOID_FIELD_NUMBER: _ClassVar[int]
    CONTEXTID_FIELD_NUMBER: _ClassVar[int]
    EXPERIENCEID_FIELD_NUMBER: _ClassVar[int]
    KNOWLEDGEID_FIELD_NUMBER: _ClassVar[int]
    roomId: str
    did: str
    roomName: str
    jobInfoId: str
    contextId: str
    experienceId: str
    knowledgeId: str
    def __init__(self, roomId: _Optional[str] = ..., did: _Optional[str] = ..., roomName: _Optional[str] = ..., jobInfoId: _Optional[str] = ..., contextId: _Optional[str] = ..., experienceId: _Optional[str] = ..., knowledgeId: _Optional[str] = ...) -> None: ...

class UpdateRoomResponse(_message.Message):
    __slots__ = ("header", "body")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: UpdateRoomResponseBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[UpdateRoomResponseBody, _Mapping]] = ...) -> None: ...

class UpdateRoomResponseBody(_message.Message):
    __slots__ = ("status", "room")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ROOM_FIELD_NUMBER: _ClassVar[int]
    status: _message_pb2.ResponseStatus
    room: RoomMetadata
    def __init__(self, status: _Optional[_Union[_message_pb2.ResponseStatus, _Mapping]] = ..., room: _Optional[_Union[RoomMetadata, _Mapping]] = ...) -> None: ...

class DeleteRoomRequest(_message.Message):
    __slots__ = ("header", "body")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: DeleteRoomRequestBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[DeleteRoomRequestBody, _Mapping]] = ...) -> None: ...

class DeleteRoomRequestBody(_message.Message):
    __slots__ = ("roomId", "did")
    ROOMID_FIELD_NUMBER: _ClassVar[int]
    DID_FIELD_NUMBER: _ClassVar[int]
    roomId: str
    did: str
    def __init__(self, roomId: _Optional[str] = ..., did: _Optional[str] = ...) -> None: ...

class DeleteRoomResponse(_message.Message):
    __slots__ = ("header", "body")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: DeleteRoomResponseBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[DeleteRoomResponseBody, _Mapping]] = ...) -> None: ...

class DeleteRoomResponseBody(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: _message_pb2.ResponseStatus
    def __init__(self, status: _Optional[_Union[_message_pb2.ResponseStatus, _Mapping]] = ...) -> None: ...

class ListRoomsRequest(_message.Message):
    __slots__ = ("header", "body")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: ListRoomsRequestBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[ListRoomsRequestBody, _Mapping]] = ...) -> None: ...

class ListRoomsRequestBody(_message.Message):
    __slots__ = ("did", "page", "pageSize")
    DID_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    PAGESIZE_FIELD_NUMBER: _ClassVar[int]
    did: str
    page: int
    pageSize: int
    def __init__(self, did: _Optional[str] = ..., page: _Optional[int] = ..., pageSize: _Optional[int] = ...) -> None: ...

class ListRoomsResponse(_message.Message):
    __slots__ = ("header", "body")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: ListRoomsResponseBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[ListRoomsResponseBody, _Mapping]] = ...) -> None: ...

class ListRoomsResponseBody(_message.Message):
    __slots__ = ("status", "rooms", "total", "page", "pageSize")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ROOMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    PAGESIZE_FIELD_NUMBER: _ClassVar[int]
    status: _message_pb2.ResponseStatus
    rooms: _containers.RepeatedCompositeFieldContainer[RoomMetadata]
    total: int
    page: int
    pageSize: int
    def __init__(self, status: _Optional[_Union[_message_pb2.ResponseStatus, _Mapping]] = ..., rooms: _Optional[_Iterable[_Union[RoomMetadata, _Mapping]]] = ..., total: _Optional[int] = ..., page: _Optional[int] = ..., pageSize: _Optional[int] = ...) -> None: ...
