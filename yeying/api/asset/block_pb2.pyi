from yeying.api.common import message_pb2 as _message_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConfirmBlockRequest(_message.Message):
    __slots__ = ["header", "body"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: ConfirmBlockRequestBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[ConfirmBlockRequestBody, _Mapping]] = ...) -> None: ...

class ConfirmBlockRequestBody(_message.Message):
    __slots__ = ["block"]
    BLOCK_FIELD_NUMBER: _ClassVar[int]
    block: BlockMetadata
    def __init__(self, block: _Optional[_Union[BlockMetadata, _Mapping]] = ...) -> None: ...

class ConfirmBlockResponse(_message.Message):
    __slots__ = ["header", "body"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: ConfirmBlockResponseBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[ConfirmBlockResponseBody, _Mapping]] = ...) -> None: ...

class ConfirmBlockResponseBody(_message.Message):
    __slots__ = ["status", "block"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    BLOCK_FIELD_NUMBER: _ClassVar[int]
    status: _message_pb2.ResponseStatus
    block: BlockMetadata
    def __init__(self, status: _Optional[_Union[_message_pb2.ResponseStatus, _Mapping]] = ..., block: _Optional[_Union[BlockMetadata, _Mapping]] = ...) -> None: ...

class StreamPutBlockRequest(_message.Message):
    __slots__ = ["head", "body", "Tail"]
    HEAD_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    TAIL_FIELD_NUMBER: _ClassVar[int]
    head: StreamPutBlockRequestHead
    body: StreamPutBlockRequestBody
    Tail: StreamPutBlockRequestTail
    def __init__(self, head: _Optional[_Union[StreamPutBlockRequestHead, _Mapping]] = ..., body: _Optional[_Union[StreamPutBlockRequestBody, _Mapping]] = ..., Tail: _Optional[_Union[StreamPutBlockRequestTail, _Mapping]] = ...) -> None: ...

class StreamPutBlockRequestHead(_message.Message):
    __slots__ = ["header", "body"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: StreamPutBlockRequestHeadBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[StreamPutBlockRequestHeadBody, _Mapping]] = ...) -> None: ...

class StreamPutBlockRequestHeadBody(_message.Message):
    __slots__ = ["block"]
    BLOCK_FIELD_NUMBER: _ClassVar[int]
    block: BlockMetadata
    def __init__(self, block: _Optional[_Union[BlockMetadata, _Mapping]] = ...) -> None: ...

class StreamPutBlockRequestBody(_message.Message):
    __slots__ = ["data"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    def __init__(self, data: _Optional[bytes] = ...) -> None: ...

class StreamPutBlockRequestTail(_message.Message):
    __slots__ = ["header"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ...) -> None: ...

class StreamPutBlockResponse(_message.Message):
    __slots__ = ["head", "tail"]
    HEAD_FIELD_NUMBER: _ClassVar[int]
    TAIL_FIELD_NUMBER: _ClassVar[int]
    head: StreamPutBlockResponseHead
    tail: StreamPutBlockResponseTail
    def __init__(self, head: _Optional[_Union[StreamPutBlockResponseHead, _Mapping]] = ..., tail: _Optional[_Union[StreamPutBlockResponseTail, _Mapping]] = ...) -> None: ...

class StreamPutBlockResponseHead(_message.Message):
    __slots__ = ["header", "body"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: StreamPutBlockResponseHeadBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[StreamPutBlockResponseHeadBody, _Mapping]] = ...) -> None: ...

class StreamPutBlockResponseHeadBody(_message.Message):
    __slots__ = ["status", "block"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    BLOCK_FIELD_NUMBER: _ClassVar[int]
    status: _message_pb2.ResponseStatus
    block: BlockMetadata
    def __init__(self, status: _Optional[_Union[_message_pb2.ResponseStatus, _Mapping]] = ..., block: _Optional[_Union[BlockMetadata, _Mapping]] = ...) -> None: ...

class StreamPutBlockResponseTail(_message.Message):
    __slots__ = ["header", "body"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: StreamPutBlockResponseTailBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[StreamPutBlockResponseTailBody, _Mapping]] = ...) -> None: ...

class StreamPutBlockResponseTailBody(_message.Message):
    __slots__ = ["status"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: _message_pb2.ResponseStatus
    def __init__(self, status: _Optional[_Union[_message_pb2.ResponseStatus, _Mapping]] = ...) -> None: ...

class PutBlockRequest(_message.Message):
    __slots__ = ["header", "body", "data"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: PutBlockRequestBody
    data: bytes
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[PutBlockRequestBody, _Mapping]] = ..., data: _Optional[bytes] = ...) -> None: ...

class PutBlockRequestBody(_message.Message):
    __slots__ = ["block"]
    BLOCK_FIELD_NUMBER: _ClassVar[int]
    block: BlockMetadata
    def __init__(self, block: _Optional[_Union[BlockMetadata, _Mapping]] = ...) -> None: ...

class PutBlockResponse(_message.Message):
    __slots__ = ["header", "body"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: PutBlockResponseBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[PutBlockResponseBody, _Mapping]] = ...) -> None: ...

class PutBlockResponseBody(_message.Message):
    __slots__ = ["status", "block"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    BLOCK_FIELD_NUMBER: _ClassVar[int]
    status: _message_pb2.ResponseStatus
    block: BlockMetadata
    def __init__(self, status: _Optional[_Union[_message_pb2.ResponseStatus, _Mapping]] = ..., block: _Optional[_Union[BlockMetadata, _Mapping]] = ...) -> None: ...

class GetBlockRequest(_message.Message):
    __slots__ = ["header", "body"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: GetBlockRequestBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[GetBlockRequestBody, _Mapping]] = ...) -> None: ...

class GetBlockRequestBody(_message.Message):
    __slots__ = ["namespaceId", "hash"]
    NAMESPACEID_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    namespaceId: str
    hash: str
    def __init__(self, namespaceId: _Optional[str] = ..., hash: _Optional[str] = ...) -> None: ...

class StreamGetBlockRequest(_message.Message):
    __slots__ = ["head", "body"]
    HEAD_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    head: StreamGetBlockRequestHead
    body: StreamGetBlockRequestBody
    def __init__(self, head: _Optional[_Union[StreamGetBlockRequestHead, _Mapping]] = ..., body: _Optional[_Union[StreamGetBlockRequestBody, _Mapping]] = ...) -> None: ...

class StreamGetBlockRequestHead(_message.Message):
    __slots__ = ["header", "body"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: StreamGetBlockRequestHeadBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[StreamGetBlockRequestHeadBody, _Mapping]] = ...) -> None: ...

class StreamGetBlockRequestHeadBody(_message.Message):
    __slots__ = ["namespaceId", "hash"]
    NAMESPACEID_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    namespaceId: str
    hash: str
    def __init__(self, namespaceId: _Optional[str] = ..., hash: _Optional[str] = ...) -> None: ...

class StreamGetBlockRequestBody(_message.Message):
    __slots__ = ["header"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ...) -> None: ...

class StreamGetBlockResponse(_message.Message):
    __slots__ = ["head", "body", "tail"]
    HEAD_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    TAIL_FIELD_NUMBER: _ClassVar[int]
    head: StreamGetBlockResponseHead
    body: StreamGetBlockResponseBody
    tail: StreamGetBlockResponseTail
    def __init__(self, head: _Optional[_Union[StreamGetBlockResponseHead, _Mapping]] = ..., body: _Optional[_Union[StreamGetBlockResponseBody, _Mapping]] = ..., tail: _Optional[_Union[StreamGetBlockResponseTail, _Mapping]] = ...) -> None: ...

class StreamGetBlockResponseHead(_message.Message):
    __slots__ = ["header", "body"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: StreamGetBlockResponseHeadBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[StreamGetBlockResponseHeadBody, _Mapping]] = ...) -> None: ...

class StreamGetBlockResponseHeadBody(_message.Message):
    __slots__ = ["status", "block"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    BLOCK_FIELD_NUMBER: _ClassVar[int]
    status: _message_pb2.ResponseStatus
    block: BlockMetadata
    def __init__(self, status: _Optional[_Union[_message_pb2.ResponseStatus, _Mapping]] = ..., block: _Optional[_Union[BlockMetadata, _Mapping]] = ...) -> None: ...

class StreamGetBlockResponseBody(_message.Message):
    __slots__ = ["data"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    def __init__(self, data: _Optional[bytes] = ...) -> None: ...

class StreamGetBlockResponseTail(_message.Message):
    __slots__ = ["header", "body"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: StreamGetBlockResponseTailBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[StreamGetBlockResponseTailBody, _Mapping]] = ...) -> None: ...

class StreamGetBlockResponseTailBody(_message.Message):
    __slots__ = ["status"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: _message_pb2.ResponseStatus
    def __init__(self, status: _Optional[_Union[_message_pb2.ResponseStatus, _Mapping]] = ...) -> None: ...

class GetBlockResponseBody(_message.Message):
    __slots__ = ["status", "block"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    BLOCK_FIELD_NUMBER: _ClassVar[int]
    status: _message_pb2.ResponseStatus
    block: BlockMetadata
    def __init__(self, status: _Optional[_Union[_message_pb2.ResponseStatus, _Mapping]] = ..., block: _Optional[_Union[BlockMetadata, _Mapping]] = ...) -> None: ...

class GetBlockResponse(_message.Message):
    __slots__ = ["header", "body", "data"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: GetBlockResponseBody
    data: bytes
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[GetBlockResponseBody, _Mapping]] = ..., data: _Optional[bytes] = ...) -> None: ...

class BlockMetadata(_message.Message):
    __slots__ = ["namespaceId", "uploader", "owner", "hash", "size", "createdAt", "signature"]
    NAMESPACEID_FIELD_NUMBER: _ClassVar[int]
    UPLOADER_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    namespaceId: str
    uploader: str
    owner: str
    hash: str
    size: int
    createdAt: str
    signature: str
    def __init__(self, namespaceId: _Optional[str] = ..., uploader: _Optional[str] = ..., owner: _Optional[str] = ..., hash: _Optional[str] = ..., size: _Optional[int] = ..., createdAt: _Optional[str] = ..., signature: _Optional[str] = ...) -> None: ...
