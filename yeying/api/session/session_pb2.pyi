from yeying.api.common import message_pb2 as _message_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateSessionRequest(_message.Message):
    __slots__ = ["header", "body"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: CreateSessionRequestBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[CreateSessionRequestBody, _Mapping]] = ...) -> None: ...

class CreateSessionRequestBody(_message.Message):
    __slots__ = ["session"]
    SESSION_FIELD_NUMBER: _ClassVar[int]
    session: SessionMetadata
    def __init__(self, session: _Optional[_Union[SessionMetadata, _Mapping]] = ...) -> None: ...

class CreateSessionResponse(_message.Message):
    __slots__ = ["header", "body"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: CreateSessionResponseBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[CreateSessionResponseBody, _Mapping]] = ...) -> None: ...

class CreateSessionResponseBody(_message.Message):
    __slots__ = ["status", "session"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SESSION_FIELD_NUMBER: _ClassVar[int]
    status: _message_pb2.ResponseStatus
    session: SessionMetadata
    def __init__(self, status: _Optional[_Union[_message_pb2.ResponseStatus, _Mapping]] = ..., session: _Optional[_Union[SessionMetadata, _Mapping]] = ...) -> None: ...

class SessionDetailRequest(_message.Message):
    __slots__ = ["header", "body"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: SessionDetailRequestBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[SessionDetailRequestBody, _Mapping]] = ...) -> None: ...

class SessionDetailRequestBody(_message.Message):
    __slots__ = ["uid"]
    UID_FIELD_NUMBER: _ClassVar[int]
    uid: str
    def __init__(self, uid: _Optional[str] = ...) -> None: ...

class SessionDetailResponse(_message.Message):
    __slots__ = ["header", "body"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: SessionDetailResponseBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[SessionDetailResponseBody, _Mapping]] = ...) -> None: ...

class SessionDetailResponseBody(_message.Message):
    __slots__ = ["status", "detail"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DETAIL_FIELD_NUMBER: _ClassVar[int]
    status: _message_pb2.ResponseStatus
    detail: SessionDetail
    def __init__(self, status: _Optional[_Union[_message_pb2.ResponseStatus, _Mapping]] = ..., detail: _Optional[_Union[SessionDetail, _Mapping]] = ...) -> None: ...

class SessionDetail(_message.Message):
    __slots__ = ["session"]
    SESSION_FIELD_NUMBER: _ClassVar[int]
    session: SessionMetadata
    def __init__(self, session: _Optional[_Union[SessionMetadata, _Mapping]] = ...) -> None: ...

class DeleteSessionRequest(_message.Message):
    __slots__ = ["header", "body"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: DeleteSessionRequestBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[DeleteSessionRequestBody, _Mapping]] = ...) -> None: ...

class DeleteSessionRequestBody(_message.Message):
    __slots__ = ["uid"]
    UID_FIELD_NUMBER: _ClassVar[int]
    uid: str
    def __init__(self, uid: _Optional[str] = ...) -> None: ...

class DeleteSessionResponse(_message.Message):
    __slots__ = ["header", "body"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: DeleteSessionResponseBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[DeleteSessionResponseBody, _Mapping]] = ...) -> None: ...

class DeleteSessionResponseBody(_message.Message):
    __slots__ = ["status"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: _message_pb2.ResponseStatus
    def __init__(self, status: _Optional[_Union[_message_pb2.ResponseStatus, _Mapping]] = ...) -> None: ...

class SearchSessionRequest(_message.Message):
    __slots__ = ["header", "body"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: SearchSessionRequestBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[SearchSessionRequestBody, _Mapping]] = ...) -> None: ...

class SearchSessionRequestBody(_message.Message):
    __slots__ = ["condition", "page"]
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    condition: SearchSessionCondition
    page: _message_pb2.RequestPage
    def __init__(self, condition: _Optional[_Union[SearchSessionCondition, _Mapping]] = ..., page: _Optional[_Union[_message_pb2.RequestPage, _Mapping]] = ...) -> None: ...

class SearchSessionCondition(_message.Message):
    __slots__ = ["name", "uid"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    name: str
    uid: str
    def __init__(self, name: _Optional[str] = ..., uid: _Optional[str] = ...) -> None: ...

class SearchSessionResponse(_message.Message):
    __slots__ = ["header", "body"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: SearchSessionResponseBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[SearchSessionResponseBody, _Mapping]] = ...) -> None: ...

class SearchSessionResponseBody(_message.Message):
    __slots__ = ["status", "sessions"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SESSIONS_FIELD_NUMBER: _ClassVar[int]
    status: _message_pb2.ResponseStatus
    sessions: _containers.RepeatedCompositeFieldContainer[SessionMetadata]
    def __init__(self, status: _Optional[_Union[_message_pb2.ResponseStatus, _Mapping]] = ..., sessions: _Optional[_Iterable[_Union[SessionMetadata, _Mapping]]] = ...) -> None: ...

class UpdateSessionRequest(_message.Message):
    __slots__ = ["header", "body"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: UpdateSessionRequestBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[UpdateSessionRequestBody, _Mapping]] = ...) -> None: ...

class UpdateSessionRequestBody(_message.Message):
    __slots__ = ["session"]
    SESSION_FIELD_NUMBER: _ClassVar[int]
    session: SessionMetadata
    def __init__(self, session: _Optional[_Union[SessionMetadata, _Mapping]] = ...) -> None: ...

class UpdateSessionResponse(_message.Message):
    __slots__ = ["header", "body"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: UpdateSessionResponseBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[UpdateSessionResponseBody, _Mapping]] = ...) -> None: ...

class UpdateSessionResponseBody(_message.Message):
    __slots__ = ["status", "session"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SESSION_FIELD_NUMBER: _ClassVar[int]
    status: _message_pb2.ResponseStatus
    session: SessionMetadata
    def __init__(self, status: _Optional[_Union[_message_pb2.ResponseStatus, _Mapping]] = ..., session: _Optional[_Union[SessionMetadata, _Mapping]] = ...) -> None: ...

class SessionMetadata(_message.Message):
    __slots__ = ["uid", "owner", "name", "description", "config", "createdAt", "updatedAt", "signature"]
    UID_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    UPDATEDAT_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    uid: str
    owner: str
    name: str
    description: str
    config: str
    createdAt: str
    updatedAt: str
    signature: str
    def __init__(self, uid: _Optional[str] = ..., owner: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., config: _Optional[str] = ..., createdAt: _Optional[str] = ..., updatedAt: _Optional[str] = ..., signature: _Optional[str] = ...) -> None: ...
