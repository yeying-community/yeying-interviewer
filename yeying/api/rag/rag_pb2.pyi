from yeying.api.common import message_pb2 as _message_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PENDING: _ClassVar[Status]
    PROCESSED: _ClassVar[Status]
    FAILED: _ClassVar[Status]

class SenderType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    USER: _ClassVar[SenderType]
    SYSTEM: _ClassVar[SenderType]
PENDING: Status
PROCESSED: Status
FAILED: Status
USER: SenderType
SYSTEM: SenderType

class CreateSessionRequest(_message.Message):
    __slots__ = ("header", "body")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: CreateSessionRequestBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[CreateSessionRequestBody, _Mapping]] = ...) -> None: ...

class CreateSessionRequestBody(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CreateSessionResponse(_message.Message):
    __slots__ = ("header", "body")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: CreateSessionResponseBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[CreateSessionResponseBody, _Mapping]] = ...) -> None: ...

class CreateSessionResponseBody(_message.Message):
    __slots__ = ("status", "memoryKey")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MEMORYKEY_FIELD_NUMBER: _ClassVar[int]
    status: _message_pb2.ResponseStatus
    memoryKey: str
    def __init__(self, status: _Optional[_Union[_message_pb2.ResponseStatus, _Mapping]] = ..., memoryKey: _Optional[str] = ...) -> None: ...

class AddMessageRequest(_message.Message):
    __slots__ = ("header", "body")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: AddMessageRequestBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[AddMessageRequestBody, _Mapping]] = ...) -> None: ...

class AddMessageRequestBody(_message.Message):
    __slots__ = ("memoryKey", "urls", "timestamp")
    MEMORYKEY_FIELD_NUMBER: _ClassVar[int]
    URLS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    memoryKey: str
    urls: _containers.RepeatedScalarFieldContainer[str]
    timestamp: int
    def __init__(self, memoryKey: _Optional[str] = ..., urls: _Optional[_Iterable[str]] = ..., timestamp: _Optional[int] = ...) -> None: ...

class AddMessageResponse(_message.Message):
    __slots__ = ("header", "body")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: AddMessageResponseBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[AddMessageResponseBody, _Mapping]] = ...) -> None: ...

class AddMessageResponseBody(_message.Message):
    __slots__ = ("status", "errorMessage")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERRORMESSAGE_FIELD_NUMBER: _ClassVar[int]
    status: _message_pb2.ResponseStatus
    errorMessage: str
    def __init__(self, status: _Optional[_Union[_message_pb2.ResponseStatus, _Mapping]] = ..., errorMessage: _Optional[str] = ...) -> None: ...

class DeleteMessageRequest(_message.Message):
    __slots__ = ("header", "body")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: DeleteMessageRequestBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[DeleteMessageRequestBody, _Mapping]] = ...) -> None: ...

class DeleteMessageRequestBody(_message.Message):
    __slots__ = ("memoryKey", "urls")
    MEMORYKEY_FIELD_NUMBER: _ClassVar[int]
    URLS_FIELD_NUMBER: _ClassVar[int]
    memoryKey: str
    urls: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, memoryKey: _Optional[str] = ..., urls: _Optional[_Iterable[str]] = ...) -> None: ...

class DeleteMessageResponse(_message.Message):
    __slots__ = ("header", "body")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: DeleteMessageResponseBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[DeleteMessageResponseBody, _Mapping]] = ...) -> None: ...

class DeleteMessageResponseBody(_message.Message):
    __slots__ = ("status", "errorMessage")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERRORMESSAGE_FIELD_NUMBER: _ClassVar[int]
    status: _message_pb2.ResponseStatus
    errorMessage: str
    def __init__(self, status: _Optional[_Union[_message_pb2.ResponseStatus, _Mapping]] = ..., errorMessage: _Optional[str] = ...) -> None: ...

class InteractionMetadata(_message.Message):
    __slots__ = ("memoryKey", "urls", "urlTimestamp", "status")
    MEMORYKEY_FIELD_NUMBER: _ClassVar[int]
    URLS_FIELD_NUMBER: _ClassVar[int]
    URLTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    memoryKey: str
    urls: _containers.RepeatedScalarFieldContainer[str]
    urlTimestamp: int
    status: Status
    def __init__(self, memoryKey: _Optional[str] = ..., urls: _Optional[_Iterable[str]] = ..., urlTimestamp: _Optional[int] = ..., status: _Optional[_Union[Status, str]] = ...) -> None: ...

class MainHistoryMetaData(_message.Message):
    __slots__ = ("memoryKey", "messageId", "messageContent", "vectorEmbedding", "createdAt", "updatedAt", "isDeleted", "isSummary", "senderType")
    MEMORYKEY_FIELD_NUMBER: _ClassVar[int]
    MESSAGEID_FIELD_NUMBER: _ClassVar[int]
    MESSAGECONTENT_FIELD_NUMBER: _ClassVar[int]
    VECTOREMBEDDING_FIELD_NUMBER: _ClassVar[int]
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    UPDATEDAT_FIELD_NUMBER: _ClassVar[int]
    ISDELETED_FIELD_NUMBER: _ClassVar[int]
    ISSUMMARY_FIELD_NUMBER: _ClassVar[int]
    SENDERTYPE_FIELD_NUMBER: _ClassVar[int]
    memoryKey: str
    messageId: int
    messageContent: str
    vectorEmbedding: bytes
    createdAt: int
    updatedAt: int
    isDeleted: bool
    isSummary: bool
    senderType: SenderType
    def __init__(self, memoryKey: _Optional[str] = ..., messageId: _Optional[int] = ..., messageContent: _Optional[str] = ..., vectorEmbedding: _Optional[bytes] = ..., createdAt: _Optional[int] = ..., updatedAt: _Optional[int] = ..., isDeleted: bool = ..., isSummary: bool = ..., senderType: _Optional[_Union[SenderType, str]] = ...) -> None: ...

class VectorIndex(_message.Message):
    __slots__ = ("memoryKey", "messageId", "vector", "createdAt", "updatedAt")
    MEMORYKEY_FIELD_NUMBER: _ClassVar[int]
    MESSAGEID_FIELD_NUMBER: _ClassVar[int]
    VECTOR_FIELD_NUMBER: _ClassVar[int]
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    UPDATEDAT_FIELD_NUMBER: _ClassVar[int]
    memoryKey: str
    messageId: int
    vector: bytes
    createdAt: int
    updatedAt: int
    def __init__(self, memoryKey: _Optional[str] = ..., messageId: _Optional[int] = ..., vector: _Optional[bytes] = ..., createdAt: _Optional[int] = ..., updatedAt: _Optional[int] = ...) -> None: ...
