from yeying.api.common import message_pb2 as _message_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UrlStatusEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    URL_STATUS_UNKNOWN: _ClassVar[UrlStatusEnum]
    URL_STATUS_ENABLE: _ClassVar[UrlStatusEnum]
    URL_STATUS_DISABLE: _ClassVar[UrlStatusEnum]

class LinkTypeEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    LINK_TYPE_UNKNOWN: _ClassVar[LinkTypeEnum]
    LINK_TYPE_PUBLIC: _ClassVar[LinkTypeEnum]
    LINK_TYPE_AUTHENTICATED: _ClassVar[LinkTypeEnum]
URL_STATUS_UNKNOWN: UrlStatusEnum
URL_STATUS_ENABLE: UrlStatusEnum
URL_STATUS_DISABLE: UrlStatusEnum
LINK_TYPE_UNKNOWN: LinkTypeEnum
LINK_TYPE_PUBLIC: LinkTypeEnum
LINK_TYPE_AUTHENTICATED: LinkTypeEnum

class CreateLinkRequest(_message.Message):
    __slots__ = ["header", "body"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: CreateLinkRequestBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[CreateLinkRequestBody, _Mapping]] = ...) -> None: ...

class CreateLinkRequestBody(_message.Message):
    __slots__ = ["link"]
    LINK_FIELD_NUMBER: _ClassVar[int]
    link: LinkMetadata
    def __init__(self, link: _Optional[_Union[LinkMetadata, _Mapping]] = ...) -> None: ...

class CreateLinkResponse(_message.Message):
    __slots__ = ["header", "body"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: CreateLinkResponseBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[CreateLinkResponseBody, _Mapping]] = ...) -> None: ...

class CreateLinkResponseBody(_message.Message):
    __slots__ = ["status", "detail"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DETAIL_FIELD_NUMBER: _ClassVar[int]
    status: _message_pb2.ResponseStatus
    detail: LinkDetail
    def __init__(self, status: _Optional[_Union[_message_pb2.ResponseStatus, _Mapping]] = ..., detail: _Optional[_Union[LinkDetail, _Mapping]] = ...) -> None: ...

class SearchLinkRequest(_message.Message):
    __slots__ = ["header", "body"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: SearchLinkRequestBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[SearchLinkRequestBody, _Mapping]] = ...) -> None: ...

class SearchLinkRequestBody(_message.Message):
    __slots__ = ["page", "condition"]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    page: _message_pb2.RequestPage
    condition: SearchLinkCondition
    def __init__(self, page: _Optional[_Union[_message_pb2.RequestPage, _Mapping]] = ..., condition: _Optional[_Union[SearchLinkCondition, _Mapping]] = ...) -> None: ...

class SearchLinkCondition(_message.Message):
    __slots__ = ["hash"]
    HASH_FIELD_NUMBER: _ClassVar[int]
    hash: str
    def __init__(self, hash: _Optional[str] = ...) -> None: ...

class SearchLinkResponse(_message.Message):
    __slots__ = ["header", "body"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: SearchLinkResponseBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[SearchLinkResponseBody, _Mapping]] = ...) -> None: ...

class SearchLinkResponseBody(_message.Message):
    __slots__ = ["status", "page", "links"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    LINKS_FIELD_NUMBER: _ClassVar[int]
    status: _message_pb2.ResponseStatus
    page: _message_pb2.ResponsePage
    links: _containers.RepeatedCompositeFieldContainer[LinkMetadata]
    def __init__(self, status: _Optional[_Union[_message_pb2.ResponseStatus, _Mapping]] = ..., page: _Optional[_Union[_message_pb2.ResponsePage, _Mapping]] = ..., links: _Optional[_Iterable[_Union[LinkMetadata, _Mapping]]] = ...) -> None: ...

class DisableLinkRequest(_message.Message):
    __slots__ = ["header", "body"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: DisableLinkRequestBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[DisableLinkRequestBody, _Mapping]] = ...) -> None: ...

class DisableLinkRequestBody(_message.Message):
    __slots__ = ["linkId"]
    LINKID_FIELD_NUMBER: _ClassVar[int]
    linkId: str
    def __init__(self, linkId: _Optional[str] = ...) -> None: ...

class DisableLinkResponse(_message.Message):
    __slots__ = ["header", "body"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: DisableLinkResponseBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[DisableLinkResponseBody, _Mapping]] = ...) -> None: ...

class DisableLinkResponseBody(_message.Message):
    __slots__ = ["status"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: _message_pb2.ResponseStatus
    def __init__(self, status: _Optional[_Union[_message_pb2.ResponseStatus, _Mapping]] = ...) -> None: ...

class UpdateLinkRequest(_message.Message):
    __slots__ = ["header", "body"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: UpdateLinkRequestBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[UpdateLinkRequestBody, _Mapping]] = ...) -> None: ...

class UpdateLinkRequestBody(_message.Message):
    __slots__ = ["link"]
    LINK_FIELD_NUMBER: _ClassVar[int]
    link: LinkMetadata
    def __init__(self, link: _Optional[_Union[LinkMetadata, _Mapping]] = ...) -> None: ...

class UpdateLinkResponse(_message.Message):
    __slots__ = ["header", "body"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: UpdateLinkResponseBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[UpdateLinkResponseBody, _Mapping]] = ...) -> None: ...

class UpdateLinkResponseBody(_message.Message):
    __slots__ = ["status", "detail"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DETAIL_FIELD_NUMBER: _ClassVar[int]
    status: _message_pb2.ResponseStatus
    detail: LinkDetail
    def __init__(self, status: _Optional[_Union[_message_pb2.ResponseStatus, _Mapping]] = ..., detail: _Optional[_Union[LinkDetail, _Mapping]] = ...) -> None: ...

class LinkDetailRequest(_message.Message):
    __slots__ = ["header", "body"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: LinkDetailRequestBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[LinkDetailRequestBody, _Mapping]] = ...) -> None: ...

class LinkDetailRequestBody(_message.Message):
    __slots__ = ["uid"]
    UID_FIELD_NUMBER: _ClassVar[int]
    uid: str
    def __init__(self, uid: _Optional[str] = ...) -> None: ...

class LinkDetailResponse(_message.Message):
    __slots__ = ["header", "body"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: LinkDetailResponseBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[LinkDetailResponseBody, _Mapping]] = ...) -> None: ...

class LinkDetailResponseBody(_message.Message):
    __slots__ = ["status", "detail"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DETAIL_FIELD_NUMBER: _ClassVar[int]
    status: _message_pb2.ResponseStatus
    detail: LinkDetail
    def __init__(self, status: _Optional[_Union[_message_pb2.ResponseStatus, _Mapping]] = ..., detail: _Optional[_Union[LinkDetail, _Mapping]] = ...) -> None: ...

class LinkDetail(_message.Message):
    __slots__ = ["url", "link"]
    URL_FIELD_NUMBER: _ClassVar[int]
    LINK_FIELD_NUMBER: _ClassVar[int]
    url: UrlMetadata
    link: LinkMetadata
    def __init__(self, url: _Optional[_Union[UrlMetadata, _Mapping]] = ..., link: _Optional[_Union[LinkMetadata, _Mapping]] = ...) -> None: ...

class LinkVisitorRequest(_message.Message):
    __slots__ = ["header", "body"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: LinkVisitorRequestBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[LinkVisitorRequestBody, _Mapping]] = ...) -> None: ...

class LinkVisitorRequestBody(_message.Message):
    __slots__ = ["uid", "page"]
    UID_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    uid: str
    page: _message_pb2.RequestPage
    def __init__(self, uid: _Optional[str] = ..., page: _Optional[_Union[_message_pb2.RequestPage, _Mapping]] = ...) -> None: ...

class LinkVisitorResponse(_message.Message):
    __slots__ = ["header", "body"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: LinkVisitorResponseBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[LinkVisitorResponseBody, _Mapping]] = ...) -> None: ...

class LinkVisitorResponseBody(_message.Message):
    __slots__ = ["status", "page", "visitors"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    VISITORS_FIELD_NUMBER: _ClassVar[int]
    status: _message_pb2.ResponseStatus
    page: _message_pb2.ResponsePage
    visitors: _containers.RepeatedCompositeFieldContainer[VisitorMetadata]
    def __init__(self, status: _Optional[_Union[_message_pb2.ResponseStatus, _Mapping]] = ..., page: _Optional[_Union[_message_pb2.ResponsePage, _Mapping]] = ..., visitors: _Optional[_Iterable[_Union[VisitorMetadata, _Mapping]]] = ...) -> None: ...

class LinkMetadata(_message.Message):
    __slots__ = ["owner", "uid", "type", "visitors", "namespaceId", "name", "description", "hash", "token", "startedAt", "expiredAt", "createdAt", "signature"]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VISITORS_FIELD_NUMBER: _ClassVar[int]
    NAMESPACEID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    STARTEDAT_FIELD_NUMBER: _ClassVar[int]
    EXPIREDAT_FIELD_NUMBER: _ClassVar[int]
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    owner: str
    uid: str
    type: LinkTypeEnum
    visitors: str
    namespaceId: str
    name: str
    description: str
    hash: str
    token: str
    startedAt: str
    expiredAt: str
    createdAt: str
    signature: str
    def __init__(self, owner: _Optional[str] = ..., uid: _Optional[str] = ..., type: _Optional[_Union[LinkTypeEnum, str]] = ..., visitors: _Optional[str] = ..., namespaceId: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., hash: _Optional[str] = ..., token: _Optional[str] = ..., startedAt: _Optional[str] = ..., expiredAt: _Optional[str] = ..., createdAt: _Optional[str] = ..., signature: _Optional[str] = ...) -> None: ...

class UrlMetadata(_message.Message):
    __slots__ = ["serviceDid", "linkId", "token", "url", "status", "createdAt", "updatedAt", "signature"]
    SERVICEDID_FIELD_NUMBER: _ClassVar[int]
    LINKID_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    UPDATEDAT_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    serviceDid: str
    linkId: str
    token: str
    url: str
    status: UrlStatusEnum
    createdAt: str
    updatedAt: str
    signature: str
    def __init__(self, serviceDid: _Optional[str] = ..., linkId: _Optional[str] = ..., token: _Optional[str] = ..., url: _Optional[str] = ..., status: _Optional[_Union[UrlStatusEnum, str]] = ..., createdAt: _Optional[str] = ..., updatedAt: _Optional[str] = ..., signature: _Optional[str] = ...) -> None: ...

class VisitorMetadata(_message.Message):
    __slots__ = ["linkId", "did", "createdAt", "signature"]
    LINKID_FIELD_NUMBER: _ClassVar[int]
    DID_FIELD_NUMBER: _ClassVar[int]
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    linkId: str
    did: str
    createdAt: str
    signature: str
    def __init__(self, linkId: _Optional[str] = ..., did: _Optional[str] = ..., createdAt: _Optional[str] = ..., signature: _Optional[str] = ...) -> None: ...
