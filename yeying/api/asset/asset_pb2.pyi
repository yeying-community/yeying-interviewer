from yeying.api.common import message_pb2 as _message_pb2
from yeying.api.common import code_pb2 as _code_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SearchAssetRequest(_message.Message):
    __slots__ = ["header", "body"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: SearchAssetRequestBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[SearchAssetRequestBody, _Mapping]] = ...) -> None: ...

class SearchAssetRequestBody(_message.Message):
    __slots__ = ["condition", "page"]
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    condition: SearchAssetCondition
    page: _message_pb2.RequestPage
    def __init__(self, condition: _Optional[_Union[SearchAssetCondition, _Mapping]] = ..., page: _Optional[_Union[_message_pb2.RequestPage, _Mapping]] = ...) -> None: ...

class SearchAssetCondition(_message.Message):
    __slots__ = ["format", "hash", "namespaceId", "name"]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    NAMESPACEID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    format: _code_pb2.DigitalFormatEnum
    hash: str
    namespaceId: str
    name: str
    def __init__(self, format: _Optional[_Union[_code_pb2.DigitalFormatEnum, str]] = ..., hash: _Optional[str] = ..., namespaceId: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class SearchAssetResponse(_message.Message):
    __slots__ = ["header", "body"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: SearchAssetResponseBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[SearchAssetResponseBody, _Mapping]] = ...) -> None: ...

class SearchAssetResponseBody(_message.Message):
    __slots__ = ["status", "assets"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ASSETS_FIELD_NUMBER: _ClassVar[int]
    status: _message_pb2.ResponseStatus
    assets: _containers.RepeatedCompositeFieldContainer[AssetMetadata]
    def __init__(self, status: _Optional[_Union[_message_pb2.ResponseStatus, _Mapping]] = ..., assets: _Optional[_Iterable[_Union[AssetMetadata, _Mapping]]] = ...) -> None: ...

class SignAssetRequest(_message.Message):
    __slots__ = ["header", "body"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: SignAssetRequestBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[SignAssetRequestBody, _Mapping]] = ...) -> None: ...

class SignAssetRequestBody(_message.Message):
    __slots__ = ["asset"]
    ASSET_FIELD_NUMBER: _ClassVar[int]
    asset: AssetMetadata
    def __init__(self, asset: _Optional[_Union[AssetMetadata, _Mapping]] = ...) -> None: ...

class SignAssetResponse(_message.Message):
    __slots__ = ["header", "body"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: SignAssetResponseBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[SignAssetResponseBody, _Mapping]] = ...) -> None: ...

class SignAssetResponseBody(_message.Message):
    __slots__ = ["status", "asset"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ASSET_FIELD_NUMBER: _ClassVar[int]
    status: _message_pb2.ResponseStatus
    asset: AssetMetadata
    def __init__(self, status: _Optional[_Union[_message_pb2.ResponseStatus, _Mapping]] = ..., asset: _Optional[_Union[AssetMetadata, _Mapping]] = ...) -> None: ...

class UpdateAssetRequest(_message.Message):
    __slots__ = ["header", "body"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: UpdateAssetRequestBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[UpdateAssetRequestBody, _Mapping]] = ...) -> None: ...

class UpdateAssetRequestBody(_message.Message):
    __slots__ = ["asset"]
    ASSET_FIELD_NUMBER: _ClassVar[int]
    asset: AssetMetadata
    def __init__(self, asset: _Optional[_Union[AssetMetadata, _Mapping]] = ...) -> None: ...

class UpdateAssetResponse(_message.Message):
    __slots__ = ["header", "body"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: UpdateAssetResponseBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[UpdateAssetResponseBody, _Mapping]] = ...) -> None: ...

class UpdateAssetResponseBody(_message.Message):
    __slots__ = ["status", "asset"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ASSET_FIELD_NUMBER: _ClassVar[int]
    status: _message_pb2.ResponseStatus
    asset: AssetMetadata
    def __init__(self, status: _Optional[_Union[_message_pb2.ResponseStatus, _Mapping]] = ..., asset: _Optional[_Union[AssetMetadata, _Mapping]] = ...) -> None: ...

class AssetDetailRequest(_message.Message):
    __slots__ = ["header", "body"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: AssetDetailRequestBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[AssetDetailRequestBody, _Mapping]] = ...) -> None: ...

class AssetDetailRequestBody(_message.Message):
    __slots__ = ["hash", "namespaceId"]
    HASH_FIELD_NUMBER: _ClassVar[int]
    NAMESPACEID_FIELD_NUMBER: _ClassVar[int]
    hash: str
    namespaceId: str
    def __init__(self, hash: _Optional[str] = ..., namespaceId: _Optional[str] = ...) -> None: ...

class AssetDetailResponse(_message.Message):
    __slots__ = ["header", "body"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: AssetDetailResponseBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[AssetDetailResponseBody, _Mapping]] = ...) -> None: ...

class AssetDetailResponseBody(_message.Message):
    __slots__ = ["status", "asset"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ASSET_FIELD_NUMBER: _ClassVar[int]
    status: _message_pb2.ResponseStatus
    asset: AssetMetadata
    def __init__(self, status: _Optional[_Union[_message_pb2.ResponseStatus, _Mapping]] = ..., asset: _Optional[_Union[AssetMetadata, _Mapping]] = ...) -> None: ...

class DeleteAssetRequest(_message.Message):
    __slots__ = ["header", "body"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: DeleteAssetRequestBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[DeleteAssetRequestBody, _Mapping]] = ...) -> None: ...

class DeleteAssetRequestBody(_message.Message):
    __slots__ = ["hash", "namespaceId"]
    HASH_FIELD_NUMBER: _ClassVar[int]
    NAMESPACEID_FIELD_NUMBER: _ClassVar[int]
    hash: str
    namespaceId: str
    def __init__(self, hash: _Optional[str] = ..., namespaceId: _Optional[str] = ...) -> None: ...

class DeleteAssetResponse(_message.Message):
    __slots__ = ["header", "body"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: DeleteAssetResponseBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[DeleteAssetResponseBody, _Mapping]] = ...) -> None: ...

class DeleteAssetResponseBody(_message.Message):
    __slots__ = ["status"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: _message_pb2.ResponseStatus
    def __init__(self, status: _Optional[_Union[_message_pb2.ResponseStatus, _Mapping]] = ...) -> None: ...

class AssetMetadata(_message.Message):
    __slots__ = ["namespaceId", "owner", "parentHash", "hash", "version", "name", "chunks", "description", "format", "size", "createdAt", "updatedAt", "chunkCount", "chunkSize", "isEncrypted", "signature"]
    NAMESPACEID_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    PARENTHASH_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CHUNKS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    UPDATEDAT_FIELD_NUMBER: _ClassVar[int]
    CHUNKCOUNT_FIELD_NUMBER: _ClassVar[int]
    CHUNKSIZE_FIELD_NUMBER: _ClassVar[int]
    ISENCRYPTED_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    namespaceId: str
    owner: str
    parentHash: str
    hash: str
    version: int
    name: str
    chunks: _containers.RepeatedScalarFieldContainer[str]
    description: str
    format: _code_pb2.DigitalFormatEnum
    size: int
    createdAt: str
    updatedAt: str
    chunkCount: int
    chunkSize: int
    isEncrypted: bool
    signature: str
    def __init__(self, namespaceId: _Optional[str] = ..., owner: _Optional[str] = ..., parentHash: _Optional[str] = ..., hash: _Optional[str] = ..., version: _Optional[int] = ..., name: _Optional[str] = ..., chunks: _Optional[_Iterable[str]] = ..., description: _Optional[str] = ..., format: _Optional[_Union[_code_pb2.DigitalFormatEnum, str]] = ..., size: _Optional[int] = ..., createdAt: _Optional[str] = ..., updatedAt: _Optional[str] = ..., chunkCount: _Optional[int] = ..., chunkSize: _Optional[int] = ..., isEncrypted: bool = ..., signature: _Optional[str] = ...) -> None: ...
