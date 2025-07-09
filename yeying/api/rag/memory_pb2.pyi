from yeying.api.common import message_pb2 as _message_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateMemoryRequest(_message.Message):
    __slots__ = ("header", "body")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: CreateMemoryRequestBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[CreateMemoryRequestBody, _Mapping]] = ...) -> None: ...

class CreateMemoryRequestBody(_message.Message):
    __slots__ = ("domain",)
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    domain: str
    def __init__(self, domain: _Optional[str] = ...) -> None: ...

class CreateMemoryResponse(_message.Message):
    __slots__ = ("header", "body")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: CreateMemoryResponseBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[CreateMemoryResponseBody, _Mapping]] = ...) -> None: ...

class CreateMemoryResponseBody(_message.Message):
    __slots__ = ("status", "memory_id")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MEMORY_ID_FIELD_NUMBER: _ClassVar[int]
    status: _message_pb2.ResponseStatus
    memory_id: str
    def __init__(self, status: _Optional[_Union[_message_pb2.ResponseStatus, _Mapping]] = ..., memory_id: _Optional[str] = ...) -> None: ...

class AddMemoryRequest(_message.Message):
    __slots__ = ("header", "body")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: AddMemoryRequestBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[AddMemoryRequestBody, _Mapping]] = ...) -> None: ...

class AddMemoryRequestBody(_message.Message):
    __slots__ = ("memory_id", "url")
    MEMORY_ID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    memory_id: str
    url: str
    def __init__(self, memory_id: _Optional[str] = ..., url: _Optional[str] = ...) -> None: ...

class AddMemoryResponse(_message.Message):
    __slots__ = ("header", "body")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: AddMemoryResponseBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[AddMemoryResponseBody, _Mapping]] = ...) -> None: ...

class AddMemoryResponseBody(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: _message_pb2.ResponseStatus
    def __init__(self, status: _Optional[_Union[_message_pb2.ResponseStatus, _Mapping]] = ...) -> None: ...

class DeleteMemoryRequest(_message.Message):
    __slots__ = ("header", "body")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: DeleteMemoryRequestBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[DeleteMemoryRequestBody, _Mapping]] = ...) -> None: ...

class DeleteMemoryRequestBody(_message.Message):
    __slots__ = ("memory_id", "url")
    MEMORY_ID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    memory_id: str
    url: str
    def __init__(self, memory_id: _Optional[str] = ..., url: _Optional[str] = ...) -> None: ...

class DeleteMemoryResponse(_message.Message):
    __slots__ = ("header", "body")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: DeleteMemoryResponseBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[DeleteMemoryResponseBody, _Mapping]] = ...) -> None: ...

class DeleteMemoryResponseBody(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: _message_pb2.ResponseStatus
    def __init__(self, status: _Optional[_Union[_message_pb2.ResponseStatus, _Mapping]] = ...) -> None: ...
