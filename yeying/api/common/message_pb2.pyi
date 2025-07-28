from yeying.api.common import code_pb2 as _code_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MessageHeader(_message.Message):
    __slots__ = ("did", "authType", "authContent", "nonce", "timestamp", "version")
    DID_FIELD_NUMBER: _ClassVar[int]
    AUTHTYPE_FIELD_NUMBER: _ClassVar[int]
    AUTHCONTENT_FIELD_NUMBER: _ClassVar[int]
    NONCE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    did: str
    authType: _code_pb2.AuthenticateTypeEnum
    authContent: str
    nonce: str
    timestamp: str
    version: int
    def __init__(self, did: _Optional[str] = ..., authType: _Optional[_Union[_code_pb2.AuthenticateTypeEnum, str]] = ..., authContent: _Optional[str] = ..., nonce: _Optional[str] = ..., timestamp: _Optional[str] = ..., version: _Optional[int] = ...) -> None: ...

class ResponseStatus(_message.Message):
    __slots__ = ("code", "message")
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    code: _code_pb2.ResponseCodeEnum
    message: str
    def __init__(self, code: _Optional[_Union[_code_pb2.ResponseCodeEnum, str]] = ..., message: _Optional[str] = ...) -> None: ...

class ResponsePage(_message.Message):
    __slots__ = ("total", "page", "pageSize")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    PAGESIZE_FIELD_NUMBER: _ClassVar[int]
    total: int
    page: int
    pageSize: int
    def __init__(self, total: _Optional[int] = ..., page: _Optional[int] = ..., pageSize: _Optional[int] = ...) -> None: ...

class RequestPage(_message.Message):
    __slots__ = ("page", "pageSize")
    PAGE_FIELD_NUMBER: _ClassVar[int]
    PAGESIZE_FIELD_NUMBER: _ClassVar[int]
    page: int
    pageSize: int
    def __init__(self, page: _Optional[int] = ..., pageSize: _Optional[int] = ...) -> None: ...
