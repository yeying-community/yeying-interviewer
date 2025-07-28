from yeying.api.common import message_pb2 as _message_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SearchNamespaceRequest(_message.Message):
    __slots__ = ("header", "body")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: SearchNamespaceRequestBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[SearchNamespaceRequestBody, _Mapping]] = ...) -> None: ...

class SearchNamespaceRequestBody(_message.Message):
    __slots__ = ("condition", "page")
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    condition: SearchNamespaceCondition
    page: _message_pb2.RequestPage
    def __init__(self, condition: _Optional[_Union[SearchNamespaceCondition, _Mapping]] = ..., page: _Optional[_Union[_message_pb2.RequestPage, _Mapping]] = ...) -> None: ...

class SearchNamespaceCondition(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class NamespaceDetailRequest(_message.Message):
    __slots__ = ("header", "body")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: NamespaceDetailRequestBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[NamespaceDetailRequestBody, _Mapping]] = ...) -> None: ...

class NamespaceDetailRequestBody(_message.Message):
    __slots__ = ("uid",)
    UID_FIELD_NUMBER: _ClassVar[int]
    uid: str
    def __init__(self, uid: _Optional[str] = ...) -> None: ...

class NamespaceDetailResponse(_message.Message):
    __slots__ = ("header", "body")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: NamespaceDetailResponseBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[NamespaceDetailResponseBody, _Mapping]] = ...) -> None: ...

class NamespaceDetailResponseBody(_message.Message):
    __slots__ = ("status", "namespace")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    status: _message_pb2.ResponseStatus
    namespace: NamespaceMetadata
    def __init__(self, status: _Optional[_Union[_message_pb2.ResponseStatus, _Mapping]] = ..., namespace: _Optional[_Union[NamespaceMetadata, _Mapping]] = ...) -> None: ...

class SearchNamespaceResponse(_message.Message):
    __slots__ = ("header", "body")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: SearchNamespaceResponseBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[SearchNamespaceResponseBody, _Mapping]] = ...) -> None: ...

class SearchNamespaceResponseBody(_message.Message):
    __slots__ = ("status", "namespaces")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    NAMESPACES_FIELD_NUMBER: _ClassVar[int]
    status: _message_pb2.ResponseStatus
    namespaces: _containers.RepeatedCompositeFieldContainer[NamespaceMetadata]
    def __init__(self, status: _Optional[_Union[_message_pb2.ResponseStatus, _Mapping]] = ..., namespaces: _Optional[_Iterable[_Union[NamespaceMetadata, _Mapping]]] = ...) -> None: ...

class CreateNamespaceRequest(_message.Message):
    __slots__ = ("header", "body")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: CreateNamespaceRequestBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[CreateNamespaceRequestBody, _Mapping]] = ...) -> None: ...

class CreateNamespaceRequestBody(_message.Message):
    __slots__ = ("namespace",)
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    namespace: NamespaceMetadata
    def __init__(self, namespace: _Optional[_Union[NamespaceMetadata, _Mapping]] = ...) -> None: ...

class CreateNamespaceResponse(_message.Message):
    __slots__ = ("header", "body")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: CreateNamespaceResponseBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[CreateNamespaceResponseBody, _Mapping]] = ...) -> None: ...

class CreateNamespaceResponseBody(_message.Message):
    __slots__ = ("status", "namespace")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    status: _message_pb2.ResponseStatus
    namespace: NamespaceMetadata
    def __init__(self, status: _Optional[_Union[_message_pb2.ResponseStatus, _Mapping]] = ..., namespace: _Optional[_Union[NamespaceMetadata, _Mapping]] = ...) -> None: ...

class UpdateNamespaceRequest(_message.Message):
    __slots__ = ("header", "body")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: UpdateNamespaceRequestBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[UpdateNamespaceRequestBody, _Mapping]] = ...) -> None: ...

class UpdateNamespaceRequestBody(_message.Message):
    __slots__ = ("namespace",)
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    namespace: NamespaceMetadata
    def __init__(self, namespace: _Optional[_Union[NamespaceMetadata, _Mapping]] = ...) -> None: ...

class UpdateNamespaceResponse(_message.Message):
    __slots__ = ("header", "body")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: UpdateNamespaceResponseBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[UpdateNamespaceResponseBody, _Mapping]] = ...) -> None: ...

class UpdateNamespaceResponseBody(_message.Message):
    __slots__ = ("status", "namespace")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    status: _message_pb2.ResponseStatus
    namespace: NamespaceMetadata
    def __init__(self, status: _Optional[_Union[_message_pb2.ResponseStatus, _Mapping]] = ..., namespace: _Optional[_Union[NamespaceMetadata, _Mapping]] = ...) -> None: ...

class DeleteNamespaceRequest(_message.Message):
    __slots__ = ("header", "body")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: DeleteNamespaceRequestBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[DeleteNamespaceRequestBody, _Mapping]] = ...) -> None: ...

class DeleteNamespaceRequestBody(_message.Message):
    __slots__ = ("uid",)
    UID_FIELD_NUMBER: _ClassVar[int]
    uid: str
    def __init__(self, uid: _Optional[str] = ...) -> None: ...

class DeleteNamespaceResponse(_message.Message):
    __slots__ = ("header", "body")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: DeleteNamespaceResponseBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[DeleteNamespaceResponseBody, _Mapping]] = ...) -> None: ...

class DeleteNamespaceResponseBody(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: _message_pb2.ResponseStatus
    def __init__(self, status: _Optional[_Union[_message_pb2.ResponseStatus, _Mapping]] = ...) -> None: ...

class NamespaceMetadata(_message.Message):
    __slots__ = ("owner", "participants", "uid", "name", "description", "createdAt", "updatedAt", "signature")
    OWNER_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANTS_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    UPDATEDAT_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    owner: str
    participants: str
    uid: str
    name: str
    description: str
    createdAt: str
    updatedAt: str
    signature: str
    def __init__(self, owner: _Optional[str] = ..., participants: _Optional[str] = ..., uid: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., createdAt: _Optional[str] = ..., updatedAt: _Optional[str] = ..., signature: _Optional[str] = ...) -> None: ...
