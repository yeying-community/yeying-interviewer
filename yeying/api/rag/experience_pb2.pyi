from yeying.api.common import message_pb2 as _message_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExperienceMetadata(_message.Message):
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

class ExperienceContent(_message.Message):
    __slots__ = ("experienceId", "url", "hash", "owner", "description", "createdAt", "updatedAt", "signature")
    EXPERIENCEID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    UPDATEDAT_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    experienceId: str
    url: str
    hash: str
    owner: str
    description: str
    createdAt: str
    updatedAt: str
    signature: str
    def __init__(self, experienceId: _Optional[str] = ..., url: _Optional[str] = ..., hash: _Optional[str] = ..., owner: _Optional[str] = ..., description: _Optional[str] = ..., createdAt: _Optional[str] = ..., updatedAt: _Optional[str] = ..., signature: _Optional[str] = ...) -> None: ...

class CreateExperienceRequest(_message.Message):
    __slots__ = ("header", "body")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: CreateExperienceRequestBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[CreateExperienceRequestBody, _Mapping]] = ...) -> None: ...

class CreateExperienceRequestBody(_message.Message):
    __slots__ = ("experience",)
    EXPERIENCE_FIELD_NUMBER: _ClassVar[int]
    experience: ExperienceMetadata
    def __init__(self, experience: _Optional[_Union[ExperienceMetadata, _Mapping]] = ...) -> None: ...

class CreateExperienceResponse(_message.Message):
    __slots__ = ("header", "body")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: CreateExperienceResponseBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[CreateExperienceResponseBody, _Mapping]] = ...) -> None: ...

class CreateExperienceResponseBody(_message.Message):
    __slots__ = ("status", "experience")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    EXPERIENCE_FIELD_NUMBER: _ClassVar[int]
    status: _message_pb2.ResponseStatus
    experience: ExperienceMetadata
    def __init__(self, status: _Optional[_Union[_message_pb2.ResponseStatus, _Mapping]] = ..., experience: _Optional[_Union[ExperienceMetadata, _Mapping]] = ...) -> None: ...

class AddExperienceRequest(_message.Message):
    __slots__ = ("header", "body")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: AddExperienceRequestBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[AddExperienceRequestBody, _Mapping]] = ...) -> None: ...

class AddExperienceRequestBody(_message.Message):
    __slots__ = ("content",)
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    content: ExperienceContent
    def __init__(self, content: _Optional[_Union[ExperienceContent, _Mapping]] = ...) -> None: ...

class AddExperienceResponse(_message.Message):
    __slots__ = ("header", "body")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: AddExperienceResponseBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[AddExperienceResponseBody, _Mapping]] = ...) -> None: ...

class AddExperienceResponseBody(_message.Message):
    __slots__ = ("status", "content")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    status: _message_pb2.ResponseStatus
    content: ExperienceContent
    def __init__(self, status: _Optional[_Union[_message_pb2.ResponseStatus, _Mapping]] = ..., content: _Optional[_Union[ExperienceContent, _Mapping]] = ...) -> None: ...

class DeleteExperienceRequest(_message.Message):
    __slots__ = ("header", "body")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: DeleteExperienceRequestBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[DeleteExperienceRequestBody, _Mapping]] = ...) -> None: ...

class DeleteExperienceRequestBody(_message.Message):
    __slots__ = ("experienceId", "hash", "owner")
    EXPERIENCEID_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    experienceId: str
    hash: str
    owner: str
    def __init__(self, experienceId: _Optional[str] = ..., hash: _Optional[str] = ..., owner: _Optional[str] = ...) -> None: ...

class DeleteExperienceResponse(_message.Message):
    __slots__ = ("header", "body")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: DeleteExperienceResponseBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[DeleteExperienceResponseBody, _Mapping]] = ...) -> None: ...

class DeleteExperienceResponseBody(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: _message_pb2.ResponseStatus
    def __init__(self, status: _Optional[_Union[_message_pb2.ResponseStatus, _Mapping]] = ...) -> None: ...
