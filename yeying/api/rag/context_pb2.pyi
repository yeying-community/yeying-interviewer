from yeying.api.common import message_pb2 as _message_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ContextMetadata(_message.Message):
    __slots__ = ["uid", "app", "owner", "description", "createdAt", "updatedAt", "signature"]
    UID_FIELD_NUMBER: _ClassVar[int]
    APP_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    UPDATEDAT_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    uid: str
    app: str
    owner: str
    description: str
    createdAt: str
    updatedAt: str
    signature: str
    def __init__(self, uid: _Optional[str] = ..., app: _Optional[str] = ..., owner: _Optional[str] = ..., description: _Optional[str] = ..., createdAt: _Optional[str] = ..., updatedAt: _Optional[str] = ..., signature: _Optional[str] = ...) -> None: ...

class ContextContent(_message.Message):
    __slots__ = ["contextId", "url", "hash", "owner", "description", "createdAt", "updatedAt", "signature"]
    CONTEXTID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    UPDATEDAT_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    contextId: str
    url: str
    hash: str
    owner: str
    description: str
    createdAt: str
    updatedAt: str
    signature: str
    def __init__(self, contextId: _Optional[str] = ..., url: _Optional[str] = ..., hash: _Optional[str] = ..., owner: _Optional[str] = ..., description: _Optional[str] = ..., createdAt: _Optional[str] = ..., updatedAt: _Optional[str] = ..., signature: _Optional[str] = ...) -> None: ...

class CreateContextRequest(_message.Message):
    __slots__ = ["header", "body"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: CreateContextRequestBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[CreateContextRequestBody, _Mapping]] = ...) -> None: ...

class CreateContextRequestBody(_message.Message):
    __slots__ = ["context"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    context: ContextMetadata
    def __init__(self, context: _Optional[_Union[ContextMetadata, _Mapping]] = ...) -> None: ...

class CreateContextResponse(_message.Message):
    __slots__ = ["header", "body"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: CreateContextResponseBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[CreateContextResponseBody, _Mapping]] = ...) -> None: ...

class CreateContextResponseBody(_message.Message):
    __slots__ = ["status", "context"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    status: _message_pb2.ResponseStatus
    context: ContextMetadata
    def __init__(self, status: _Optional[_Union[_message_pb2.ResponseStatus, _Mapping]] = ..., context: _Optional[_Union[ContextMetadata, _Mapping]] = ...) -> None: ...

class AddContextRequest(_message.Message):
    __slots__ = ["header", "body"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: AddContextRequestBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[AddContextRequestBody, _Mapping]] = ...) -> None: ...

class AddContextRequestBody(_message.Message):
    __slots__ = ["content"]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    content: ContextContent
    def __init__(self, content: _Optional[_Union[ContextContent, _Mapping]] = ...) -> None: ...

class AddContextResponse(_message.Message):
    __slots__ = ["header", "body"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: AddContextResponseBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[AddContextResponseBody, _Mapping]] = ...) -> None: ...

class AddContextResponseBody(_message.Message):
    __slots__ = ["status", "content"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    status: _message_pb2.ResponseStatus
    content: ContextContent
    def __init__(self, status: _Optional[_Union[_message_pb2.ResponseStatus, _Mapping]] = ..., content: _Optional[_Union[ContextContent, _Mapping]] = ...) -> None: ...

class DeleteContextRequest(_message.Message):
    __slots__ = ["header", "body"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: DeleteContextRequestBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[DeleteContextRequestBody, _Mapping]] = ...) -> None: ...

class DeleteContextRequestBody(_message.Message):
    __slots__ = ["contextId", "hash", "owner"]
    CONTEXTID_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    contextId: str
    hash: str
    owner: str
    def __init__(self, contextId: _Optional[str] = ..., hash: _Optional[str] = ..., owner: _Optional[str] = ...) -> None: ...

class DeleteContextResponse(_message.Message):
    __slots__ = ["header", "body"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: DeleteContextResponseBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[DeleteContextResponseBody, _Mapping]] = ...) -> None: ...

class DeleteContextResponseBody(_message.Message):
    __slots__ = ["status"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: _message_pb2.ResponseStatus
    def __init__(self, status: _Optional[_Union[_message_pb2.ResponseStatus, _Mapping]] = ...) -> None: ...

class DeleteContextMessageRequest(_message.Message):
    __slots__ = ["header", "body"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: DeleteContextMessageRequestBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[DeleteContextMessageRequestBody, _Mapping]] = ...) -> None: ...

class DeleteContextMessageRequestBody(_message.Message):
    __slots__ = ["contextId", "hash", "owner", "index"]
    CONTEXTID_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    contextId: str
    hash: str
    owner: str
    index: int
    def __init__(self, contextId: _Optional[str] = ..., hash: _Optional[str] = ..., owner: _Optional[str] = ..., index: _Optional[int] = ...) -> None: ...

class DeleteContextMessageResponse(_message.Message):
    __slots__ = ["header", "body"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: DeleteContextMessageResponseBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[DeleteContextMessageResponseBody, _Mapping]] = ...) -> None: ...

class DeleteContextMessageResponseBody(_message.Message):
    __slots__ = ["status"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: _message_pb2.ResponseStatus
    def __init__(self, status: _Optional[_Union[_message_pb2.ResponseStatus, _Mapping]] = ...) -> None: ...
