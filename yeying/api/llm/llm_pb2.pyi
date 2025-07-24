from yeying.api.common import message_pb2 as _message_pb2
from yeying.api.common import code_pb2 as _code_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MessageRoleEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    MESSAGE_ROLE_UNKNOWN: _ClassVar[MessageRoleEnum]
    MESSAGE_ROLE_ASSISTANT: _ClassVar[MessageRoleEnum]
    MESSAGE_ROLE_USER: _ClassVar[MessageRoleEnum]
    MESSAGE_ROLE_SYSTEM: _ClassVar[MessageRoleEnum]

class ContentTypeEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    CONTENT_TYPE_UNKNOWN: _ClassVar[ContentTypeEnum]
    CONTENT_TYPE_TEXT: _ClassVar[ContentTypeEnum]
    CONTENT_TYPE_IMAGE: _ClassVar[ContentTypeEnum]
    CONTENT_TYPE_AUDIO: _ClassVar[ContentTypeEnum]
    CONTENT_TYPE_VIDEO: _ClassVar[ContentTypeEnum]
    CONTENT_TYPE_DOCUMENT: _ClassVar[ContentTypeEnum]
MESSAGE_ROLE_UNKNOWN: MessageRoleEnum
MESSAGE_ROLE_ASSISTANT: MessageRoleEnum
MESSAGE_ROLE_USER: MessageRoleEnum
MESSAGE_ROLE_SYSTEM: MessageRoleEnum
CONTENT_TYPE_UNKNOWN: ContentTypeEnum
CONTENT_TYPE_TEXT: ContentTypeEnum
CONTENT_TYPE_IMAGE: ContentTypeEnum
CONTENT_TYPE_AUDIO: ContentTypeEnum
CONTENT_TYPE_VIDEO: ContentTypeEnum
CONTENT_TYPE_DOCUMENT: ContentTypeEnum

class CompleteRequest(_message.Message):
    __slots__ = ["header", "body"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: CompleteRequestBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[CompleteRequestBody, _Mapping]] = ...) -> None: ...

class CompleteRequestBody(_message.Message):
    __slots__ = ["sessionId", "promptId", "providerId", "model", "stream", "messages"]
    SESSIONID_FIELD_NUMBER: _ClassVar[int]
    PROMPTID_FIELD_NUMBER: _ClassVar[int]
    PROVIDERID_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    STREAM_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    sessionId: str
    promptId: str
    providerId: str
    model: str
    stream: bool
    messages: _containers.RepeatedCompositeFieldContainer[Message]
    def __init__(self, sessionId: _Optional[str] = ..., promptId: _Optional[str] = ..., providerId: _Optional[str] = ..., model: _Optional[str] = ..., stream: bool = ..., messages: _Optional[_Iterable[_Union[Message, _Mapping]]] = ...) -> None: ...

class Message(_message.Message):
    __slots__ = ["role", "content"]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    role: MessageRoleEnum
    content: Content
    def __init__(self, role: _Optional[_Union[MessageRoleEnum, str]] = ..., content: _Optional[_Union[Content, _Mapping]] = ...) -> None: ...

class Content(_message.Message):
    __slots__ = ["type", "data"]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    type: ContentTypeEnum
    data: str
    def __init__(self, type: _Optional[_Union[ContentTypeEnum, str]] = ..., data: _Optional[str] = ...) -> None: ...

class Answer(_message.Message):
    __slots__ = ["model", "id", "createdAt", "choices"]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    CHOICES_FIELD_NUMBER: _ClassVar[int]
    model: str
    id: str
    createdAt: int
    choices: _containers.RepeatedCompositeFieldContainer[Choice]
    def __init__(self, model: _Optional[str] = ..., id: _Optional[str] = ..., createdAt: _Optional[int] = ..., choices: _Optional[_Iterable[_Union[Choice, _Mapping]]] = ...) -> None: ...

class CompleteResponse(_message.Message):
    __slots__ = ["head", "body", "tail"]
    HEAD_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    TAIL_FIELD_NUMBER: _ClassVar[int]
    head: CompleteResponseHead
    body: CompleteResponseBody
    tail: CompleteResponseTail
    def __init__(self, head: _Optional[_Union[CompleteResponseHead, _Mapping]] = ..., body: _Optional[_Union[CompleteResponseBody, _Mapping]] = ..., tail: _Optional[_Union[CompleteResponseTail, _Mapping]] = ...) -> None: ...

class CompleteResponseHead(_message.Message):
    __slots__ = ["header", "body"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: CompleteResponseHeadBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[CompleteResponseHeadBody, _Mapping]] = ...) -> None: ...

class CompleteResponseHeadBody(_message.Message):
    __slots__ = ["status"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: _message_pb2.ResponseStatus
    def __init__(self, status: _Optional[_Union[_message_pb2.ResponseStatus, _Mapping]] = ...) -> None: ...

class CompleteResponseBody(_message.Message):
    __slots__ = ["data"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: str
    def __init__(self, data: _Optional[str] = ...) -> None: ...

class CompleteResponseTail(_message.Message):
    __slots__ = ["header", "body"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: CompleteResponseTailBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[CompleteResponseTailBody, _Mapping]] = ...) -> None: ...

class CompleteResponseTailBody(_message.Message):
    __slots__ = ["status"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: _message_pb2.ResponseStatus
    def __init__(self, status: _Optional[_Union[_message_pb2.ResponseStatus, _Mapping]] = ...) -> None: ...

class GenerateRequest(_message.Message):
    __slots__ = ["header", "body"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: GenerateRequestBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[GenerateRequestBody, _Mapping]] = ...) -> None: ...

class GenerateRequestBody(_message.Message):
    __slots__ = ["llmId", "model", "prompt", "responseContentFormat", "count", "size", "quality", "style"]
    LLMID_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    PROMPT_FIELD_NUMBER: _ClassVar[int]
    RESPONSECONTENTFORMAT_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    QUALITY_FIELD_NUMBER: _ClassVar[int]
    STYLE_FIELD_NUMBER: _ClassVar[int]
    llmId: str
    model: str
    prompt: str
    responseContentFormat: _code_pb2.ContentFormatEnum
    count: int
    size: str
    quality: str
    style: str
    def __init__(self, llmId: _Optional[str] = ..., model: _Optional[str] = ..., prompt: _Optional[str] = ..., responseContentFormat: _Optional[_Union[_code_pb2.ContentFormatEnum, str]] = ..., count: _Optional[int] = ..., size: _Optional[str] = ..., quality: _Optional[str] = ..., style: _Optional[str] = ...) -> None: ...

class GenerateResponse(_message.Message):
    __slots__ = ["head", "body", "tail"]
    HEAD_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    TAIL_FIELD_NUMBER: _ClassVar[int]
    head: GenerateResponseHead
    body: GenerateResponseBody
    tail: GenerateResponseTail
    def __init__(self, head: _Optional[_Union[GenerateResponseHead, _Mapping]] = ..., body: _Optional[_Union[GenerateResponseBody, _Mapping]] = ..., tail: _Optional[_Union[GenerateResponseTail, _Mapping]] = ...) -> None: ...

class GenerateResponseHead(_message.Message):
    __slots__ = ["header", "body"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: GenerateResponseHeadBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[GenerateResponseHeadBody, _Mapping]] = ...) -> None: ...

class GenerateResponseHeadBody(_message.Message):
    __slots__ = ["status"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: _message_pb2.ResponseStatus
    def __init__(self, status: _Optional[_Union[_message_pb2.ResponseStatus, _Mapping]] = ...) -> None: ...

class GenerateResponseBody(_message.Message):
    __slots__ = ["data"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: str
    def __init__(self, data: _Optional[str] = ...) -> None: ...

class GenerateResponseTail(_message.Message):
    __slots__ = ["header", "body"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: GenerateResponseTailBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[GenerateResponseTailBody, _Mapping]] = ...) -> None: ...

class GenerateResponseTailBody(_message.Message):
    __slots__ = ["status"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: _message_pb2.ResponseStatus
    def __init__(self, status: _Optional[_Union[_message_pb2.ResponseStatus, _Mapping]] = ...) -> None: ...

class TextPrompt(_message.Message):
    __slots__ = ["message"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class ImagePrompt(_message.Message):
    __slots__ = ["message", "mask", "image"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    MASK_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    mask: bytes
    image: bytes
    def __init__(self, message: _Optional[str] = ..., mask: _Optional[bytes] = ..., image: _Optional[bytes] = ...) -> None: ...

class ImageResult(_message.Message):
    __slots__ = ["responseContentFormat", "count", "size", "quality", "style"]
    RESPONSECONTENTFORMAT_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    QUALITY_FIELD_NUMBER: _ClassVar[int]
    STYLE_FIELD_NUMBER: _ClassVar[int]
    responseContentFormat: _code_pb2.ContentFormatEnum
    count: int
    size: str
    quality: str
    style: str
    def __init__(self, responseContentFormat: _Optional[_Union[_code_pb2.ContentFormatEnum, str]] = ..., count: _Optional[int] = ..., size: _Optional[str] = ..., quality: _Optional[str] = ..., style: _Optional[str] = ...) -> None: ...

class EditRequest(_message.Message):
    __slots__ = ["did", "llmId", "model", "srcType", "desType", "textPrompt", "imagePrompt", "imageResult"]
    DID_FIELD_NUMBER: _ClassVar[int]
    LLMID_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    SRCTYPE_FIELD_NUMBER: _ClassVar[int]
    DESTYPE_FIELD_NUMBER: _ClassVar[int]
    TEXTPROMPT_FIELD_NUMBER: _ClassVar[int]
    IMAGEPROMPT_FIELD_NUMBER: _ClassVar[int]
    IMAGERESULT_FIELD_NUMBER: _ClassVar[int]
    did: str
    llmId: str
    model: str
    srcType: _code_pb2.DigitalFormatEnum
    desType: _code_pb2.DigitalFormatEnum
    textPrompt: TextPrompt
    imagePrompt: ImagePrompt
    imageResult: ImageResult
    def __init__(self, did: _Optional[str] = ..., llmId: _Optional[str] = ..., model: _Optional[str] = ..., srcType: _Optional[_Union[_code_pb2.DigitalFormatEnum, str]] = ..., desType: _Optional[_Union[_code_pb2.DigitalFormatEnum, str]] = ..., textPrompt: _Optional[_Union[TextPrompt, _Mapping]] = ..., imagePrompt: _Optional[_Union[ImagePrompt, _Mapping]] = ..., imageResult: _Optional[_Union[ImageResult, _Mapping]] = ...) -> None: ...

class EditResponse(_message.Message):
    __slots__ = ["status", "base64", "bytes"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    BASE64_FIELD_NUMBER: _ClassVar[int]
    BYTES_FIELD_NUMBER: _ClassVar[int]
    status: _message_pb2.ResponseStatus
    base64: str
    bytes: bytes
    def __init__(self, status: _Optional[_Union[_message_pb2.ResponseStatus, _Mapping]] = ..., base64: _Optional[str] = ..., bytes: _Optional[bytes] = ...) -> None: ...

class TranslateRequest(_message.Message):
    __slots__ = ["did", "llmId", "instance"]
    DID_FIELD_NUMBER: _ClassVar[int]
    LLMID_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    did: str
    llmId: str
    instance: str
    def __init__(self, did: _Optional[str] = ..., llmId: _Optional[str] = ..., instance: _Optional[str] = ...) -> None: ...

class TranslateResponse(_message.Message):
    __slots__ = ["status"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: _message_pb2.ResponseStatus
    def __init__(self, status: _Optional[_Union[_message_pb2.ResponseStatus, _Mapping]] = ...) -> None: ...

class ConvertRequest(_message.Message):
    __slots__ = ["did", "llmId", "instance"]
    DID_FIELD_NUMBER: _ClassVar[int]
    LLMID_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    did: str
    llmId: str
    instance: str
    def __init__(self, did: _Optional[str] = ..., llmId: _Optional[str] = ..., instance: _Optional[str] = ...) -> None: ...

class ConvertResponse(_message.Message):
    __slots__ = ["status"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: _message_pb2.ResponseStatus
    def __init__(self, status: _Optional[_Union[_message_pb2.ResponseStatus, _Mapping]] = ...) -> None: ...

class Choice(_message.Message):
    __slots__ = ["index", "role", "content", "finishReason"]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    FINISHREASON_FIELD_NUMBER: _ClassVar[int]
    index: int
    role: MessageRoleEnum
    content: Content
    finishReason: str
    def __init__(self, index: _Optional[int] = ..., role: _Optional[_Union[MessageRoleEnum, str]] = ..., content: _Optional[_Union[Content, _Mapping]] = ..., finishReason: _Optional[str] = ...) -> None: ...

class SpeechRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SpeechResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
