from yeying.api.common import message_pb2 as _message_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class KnowledgeMetadata(_message.Message):
    __slots__ = ("uid", "app", "owner", "description", "createdAt", "updatedAt", "signature")
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

class KnowledgeContent(_message.Message):
    __slots__ = ("knowledgeId", "url", "hash", "owner", "description", "createdAt", "updatedAt", "signature")
    KNOWLEDGEID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    UPDATEDAT_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    knowledgeId: str
    url: str
    hash: str
    owner: str
    description: str
    createdAt: str
    updatedAt: str
    signature: str
    def __init__(self, knowledgeId: _Optional[str] = ..., url: _Optional[str] = ..., hash: _Optional[str] = ..., owner: _Optional[str] = ..., description: _Optional[str] = ..., createdAt: _Optional[str] = ..., updatedAt: _Optional[str] = ..., signature: _Optional[str] = ...) -> None: ...

class CreateKnowledgeRequest(_message.Message):
    __slots__ = ("header", "body")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: CreateKnowledgeRequestBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[CreateKnowledgeRequestBody, _Mapping]] = ...) -> None: ...

class CreateKnowledgeRequestBody(_message.Message):
    __slots__ = ("knowledge",)
    KNOWLEDGE_FIELD_NUMBER: _ClassVar[int]
    knowledge: KnowledgeMetadata
    def __init__(self, knowledge: _Optional[_Union[KnowledgeMetadata, _Mapping]] = ...) -> None: ...

class CreateKnowledgeResponse(_message.Message):
    __slots__ = ("header", "body")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: CreateKnowledgeResponseBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[CreateKnowledgeResponseBody, _Mapping]] = ...) -> None: ...

class CreateKnowledgeResponseBody(_message.Message):
    __slots__ = ("status", "knowledge")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    KNOWLEDGE_FIELD_NUMBER: _ClassVar[int]
    status: _message_pb2.ResponseStatus
    knowledge: KnowledgeMetadata
    def __init__(self, status: _Optional[_Union[_message_pb2.ResponseStatus, _Mapping]] = ..., knowledge: _Optional[_Union[KnowledgeMetadata, _Mapping]] = ...) -> None: ...

class AddKnowledgeRequest(_message.Message):
    __slots__ = ("header", "body")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: AddKnowledgeRequestBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[AddKnowledgeRequestBody, _Mapping]] = ...) -> None: ...

class AddKnowledgeRequestBody(_message.Message):
    __slots__ = ("content",)
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    content: KnowledgeContent
    def __init__(self, content: _Optional[_Union[KnowledgeContent, _Mapping]] = ...) -> None: ...

class AddKnowledgeResponse(_message.Message):
    __slots__ = ("header", "body")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: AddKnowledgeResponseBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[AddKnowledgeResponseBody, _Mapping]] = ...) -> None: ...

class AddKnowledgeResponseBody(_message.Message):
    __slots__ = ("status", "content")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    status: _message_pb2.ResponseStatus
    content: KnowledgeContent
    def __init__(self, status: _Optional[_Union[_message_pb2.ResponseStatus, _Mapping]] = ..., content: _Optional[_Union[KnowledgeContent, _Mapping]] = ...) -> None: ...

class DeleteKnowledgeRequest(_message.Message):
    __slots__ = ("header", "body")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: DeleteKnowledgeRequestBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[DeleteKnowledgeRequestBody, _Mapping]] = ...) -> None: ...

class DeleteKnowledgeRequestBody(_message.Message):
    __slots__ = ("knowledgeId", "hash", "owner")
    KNOWLEDGEID_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    knowledgeId: str
    hash: str
    owner: str
    def __init__(self, knowledgeId: _Optional[str] = ..., hash: _Optional[str] = ..., owner: _Optional[str] = ...) -> None: ...

class DeleteKnowledgeResponse(_message.Message):
    __slots__ = ("header", "body")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: DeleteKnowledgeResponseBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[DeleteKnowledgeResponseBody, _Mapping]] = ...) -> None: ...

class DeleteKnowledgeResponseBody(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: _message_pb2.ResponseStatus
    def __init__(self, status: _Optional[_Union[_message_pb2.ResponseStatus, _Mapping]] = ...) -> None: ...
