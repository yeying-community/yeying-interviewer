from yeying.api.common import message_pb2 as _message_pb2
from yeying.api.asset import asset_pb2 as _asset_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SearchDeletedAssetRequest(_message.Message):
    __slots__ = ["header", "body"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: SearchDeletedAssetRequestBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[SearchDeletedAssetRequestBody, _Mapping]] = ...) -> None: ...

class SearchDeletedAssetRequestBody(_message.Message):
    __slots__ = ["condition", "page"]
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    condition: _asset_pb2.SearchAssetCondition
    page: _message_pb2.RequestPage
    def __init__(self, condition: _Optional[_Union[_asset_pb2.SearchAssetCondition, _Mapping]] = ..., page: _Optional[_Union[_message_pb2.RequestPage, _Mapping]] = ...) -> None: ...

class SearchDeletedAssetResponse(_message.Message):
    __slots__ = ["header", "body"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: SearchDeletedAssetResponseBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[SearchDeletedAssetResponseBody, _Mapping]] = ...) -> None: ...

class SearchDeletedAssetResponseBody(_message.Message):
    __slots__ = ["status", "assets"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ASSETS_FIELD_NUMBER: _ClassVar[int]
    status: _message_pb2.ResponseStatus
    assets: _containers.RepeatedCompositeFieldContainer[DeletedAssetMetadata]
    def __init__(self, status: _Optional[_Union[_message_pb2.ResponseStatus, _Mapping]] = ..., assets: _Optional[_Iterable[_Union[DeletedAssetMetadata, _Mapping]]] = ...) -> None: ...

class RecoverDeletedAssetRequest(_message.Message):
    __slots__ = ["header", "body"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: RecoverDeletedAssetRequestBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[RecoverDeletedAssetRequestBody, _Mapping]] = ...) -> None: ...

class RecoverDeletedAssetRequestBody(_message.Message):
    __slots__ = ["hash", "namespaceId"]
    HASH_FIELD_NUMBER: _ClassVar[int]
    NAMESPACEID_FIELD_NUMBER: _ClassVar[int]
    hash: str
    namespaceId: str
    def __init__(self, hash: _Optional[str] = ..., namespaceId: _Optional[str] = ...) -> None: ...

class RecoverDeletedAssetResponse(_message.Message):
    __slots__ = ["header", "body"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: RecoverDeletedAssetResponseBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[RecoverDeletedAssetResponseBody, _Mapping]] = ...) -> None: ...

class RecoverDeletedAssetResponseBody(_message.Message):
    __slots__ = ["status"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: _message_pb2.ResponseStatus
    def __init__(self, status: _Optional[_Union[_message_pb2.ResponseStatus, _Mapping]] = ...) -> None: ...

class RemoveDeletedAssetRequest(_message.Message):
    __slots__ = ["header", "body"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: RemoveDeletedAssetRequestBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[RemoveDeletedAssetRequestBody, _Mapping]] = ...) -> None: ...

class RemoveDeletedAssetRequestBody(_message.Message):
    __slots__ = ["hash", "namespaceId"]
    HASH_FIELD_NUMBER: _ClassVar[int]
    NAMESPACEID_FIELD_NUMBER: _ClassVar[int]
    hash: str
    namespaceId: str
    def __init__(self, hash: _Optional[str] = ..., namespaceId: _Optional[str] = ...) -> None: ...

class RemoveDeletedAssetResponse(_message.Message):
    __slots__ = ["header", "body"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: RemoveDeletedAssetResponseBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[RemoveDeletedAssetResponseBody, _Mapping]] = ...) -> None: ...

class RemoveDeletedAssetResponseBody(_message.Message):
    __slots__ = ["status"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: _message_pb2.ResponseStatus
    def __init__(self, status: _Optional[_Union[_message_pb2.ResponseStatus, _Mapping]] = ...) -> None: ...

class DeletedAssetMetadata(_message.Message):
    __slots__ = ["asset", "deletedAt"]
    ASSET_FIELD_NUMBER: _ClassVar[int]
    DELETEDAT_FIELD_NUMBER: _ClassVar[int]
    asset: _asset_pb2.AssetMetadata
    deletedAt: str
    def __init__(self, asset: _Optional[_Union[_asset_pb2.AssetMetadata, _Mapping]] = ..., deletedAt: _Optional[str] = ...) -> None: ...
