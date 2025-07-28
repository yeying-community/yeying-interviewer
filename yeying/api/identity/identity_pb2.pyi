from yeying.api.common import message_pb2 as _message_pb2
from yeying.api.common import code_pb2 as _code_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DepositRequest(_message.Message):
    __slots__ = ("header", "body")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: DepositRequestBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[DepositRequestBody, _Mapping]] = ...) -> None: ...

class DepositRequestBody(_message.Message):
    __slots__ = ("cipher", "protocol")
    CIPHER_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    cipher: str
    protocol: str
    def __init__(self, cipher: _Optional[str] = ..., protocol: _Optional[str] = ...) -> None: ...

class DepositResponse(_message.Message):
    __slots__ = ("header", "body")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: DepositResponseBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[DepositResponseBody, _Mapping]] = ...) -> None: ...

class DepositResponseBody(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: _message_pb2.ResponseStatus
    def __init__(self, status: _Optional[_Union[_message_pb2.ResponseStatus, _Mapping]] = ...) -> None: ...

class RetrieveRequest(_message.Message):
    __slots__ = ("header",)
    HEADER_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ...) -> None: ...

class RetrieveResponse(_message.Message):
    __slots__ = ("header",)
    HEADER_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ...) -> None: ...

class ShareRequest(_message.Message):
    __slots__ = ("header",)
    HEADER_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ...) -> None: ...

class ShareResponse(_message.Message):
    __slots__ = ("header",)
    HEADER_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ...) -> None: ...

class QueryRequest(_message.Message):
    __slots__ = ("header", "body")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: QueryRequestBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[QueryRequestBody, _Mapping]] = ...) -> None: ...

class QueryRequestBody(_message.Message):
    __slots__ = ("serviceCode",)
    SERVICECODE_FIELD_NUMBER: _ClassVar[int]
    serviceCode: _code_pb2.ServiceCodeEnum
    def __init__(self, serviceCode: _Optional[_Union[_code_pb2.ServiceCodeEnum, str]] = ...) -> None: ...

class QueryResponse(_message.Message):
    __slots__ = ("header", "body")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: QueryResponseBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[QueryResponseBody, _Mapping]] = ...) -> None: ...

class QueryResponseBody(_message.Message):
    __slots__ = ("status", "cipher", "protocol")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CIPHER_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    status: _message_pb2.ResponseStatus
    cipher: str
    protocol: str
    def __init__(self, status: _Optional[_Union[_message_pb2.ResponseStatus, _Mapping]] = ..., cipher: _Optional[str] = ..., protocol: _Optional[str] = ...) -> None: ...

class CancelRequest(_message.Message):
    __slots__ = ("header", "body")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: CancelRequestBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[CancelRequestBody, _Mapping]] = ...) -> None: ...

class CancelRequestBody(_message.Message):
    __slots__ = ("did",)
    DID_FIELD_NUMBER: _ClassVar[int]
    did: str
    def __init__(self, did: _Optional[str] = ...) -> None: ...

class CancelResponse(_message.Message):
    __slots__ = ("header", "body")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: CancelResponseBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[CancelResponseBody, _Mapping]] = ...) -> None: ...

class CancelResponseBody(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: _message_pb2.ResponseStatus
    def __init__(self, status: _Optional[_Union[_message_pb2.ResponseStatus, _Mapping]] = ...) -> None: ...
