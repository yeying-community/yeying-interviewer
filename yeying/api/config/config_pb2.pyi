from yeying.api.common import message_pb2 as _message_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConfigTypeEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    CONFIG_TYPE_UNKNOWN: _ClassVar[ConfigTypeEnum]
    CONFIG_TYPE_SYSTEM: _ClassVar[ConfigTypeEnum]
    CONFIG_TYPE_USER: _ClassVar[ConfigTypeEnum]
CONFIG_TYPE_UNKNOWN: ConfigTypeEnum
CONFIG_TYPE_SYSTEM: ConfigTypeEnum
CONFIG_TYPE_USER: ConfigTypeEnum

class GetConfigRequest(_message.Message):
    __slots__ = ["header", "body"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: GetConfigRequestBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[GetConfigRequestBody, _Mapping]] = ...) -> None: ...

class GetConfigRequestBody(_message.Message):
    __slots__ = ["key", "type"]
    KEY_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    key: str
    type: ConfigTypeEnum
    def __init__(self, key: _Optional[str] = ..., type: _Optional[_Union[ConfigTypeEnum, str]] = ...) -> None: ...

class GetConfigResponse(_message.Message):
    __slots__ = ["header", "body"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: GetConfigResponseBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[GetConfigResponseBody, _Mapping]] = ...) -> None: ...

class GetConfigResponseBody(_message.Message):
    __slots__ = ["status", "config"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    status: _message_pb2.ResponseStatus
    config: ConfigMetadata
    def __init__(self, status: _Optional[_Union[_message_pb2.ResponseStatus, _Mapping]] = ..., config: _Optional[_Union[ConfigMetadata, _Mapping]] = ...) -> None: ...

class SetConfigRequest(_message.Message):
    __slots__ = ["header", "body"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: SetConfigRequestBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[SetConfigRequestBody, _Mapping]] = ...) -> None: ...

class SetConfigRequestBody(_message.Message):
    __slots__ = ["config"]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    config: ConfigMetadata
    def __init__(self, config: _Optional[_Union[ConfigMetadata, _Mapping]] = ...) -> None: ...

class SetConfigResponse(_message.Message):
    __slots__ = ["header", "body"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: SetConfigResponseBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[SetConfigResponseBody, _Mapping]] = ...) -> None: ...

class SetConfigResponseBody(_message.Message):
    __slots__ = ["status", "config"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    status: _message_pb2.ResponseStatus
    config: ConfigMetadata
    def __init__(self, status: _Optional[_Union[_message_pb2.ResponseStatus, _Mapping]] = ..., config: _Optional[_Union[ConfigMetadata, _Mapping]] = ...) -> None: ...

class ConfigMetadata(_message.Message):
    __slots__ = ["owner", "key", "value", "createdAt", "updatedAt", "signature"]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    UPDATEDAT_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    owner: str
    key: str
    value: str
    createdAt: str
    updatedAt: str
    signature: str
    def __init__(self, owner: _Optional[str] = ..., key: _Optional[str] = ..., value: _Optional[str] = ..., createdAt: _Optional[str] = ..., updatedAt: _Optional[str] = ..., signature: _Optional[str] = ...) -> None: ...
