from yeying.api.common import message_pb2 as _message_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ModelTypeEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    MODEL_TYPE_UNKNOWN: _ClassVar[ModelTypeEnum]
    MODEL_TYPE_LLM: _ClassVar[ModelTypeEnum]
    MODEL_TYPE_TEXT_EMBEDDING: _ClassVar[ModelTypeEnum]
    MODEL_TYPE_RERANK: _ClassVar[ModelTypeEnum]
    MODEL_TYPE_SPEECH2TEXT: _ClassVar[ModelTypeEnum]
    MODEL_TYPE_TTS: _ClassVar[ModelTypeEnum]
    MODEL_TYPE_MODERATION: _ClassVar[ModelTypeEnum]
    MODEL_TYPE_TEXT2IMAGE: _ClassVar[ModelTypeEnum]

class ModelFeatureEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    MODEL_FEATURE_AGENT_THOUGHT: _ClassVar[ModelFeatureEnum]
    MODEL_FEATURE_VISION: _ClassVar[ModelFeatureEnum]
    MODEL_FEATURE_TOOL_CALL: _ClassVar[ModelFeatureEnum]
    MODEL_FEATURE_MULTI_TOOL_CALL: _ClassVar[ModelFeatureEnum]
    MODEL_FEATURE_STREAM_TOOL_CALL: _ClassVar[ModelFeatureEnum]
    MODEL_FEATURE_DOCUMENT: _ClassVar[ModelFeatureEnum]
    MODEL_FEATURE_VIDEO: _ClassVar[ModelFeatureEnum]
    MODEL_FEATURE_AUDIO: _ClassVar[ModelFeatureEnum]

class ProviderCodeEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    PROVIDER_CODE_UNKNOWN: _ClassVar[ProviderCodeEnum]
    PROVIDER_CODE_OPENAI: _ClassVar[ProviderCodeEnum]
    PROVIDER_CODE_TONGYI: _ClassVar[ProviderCodeEnum]
    PROVIDER_CODE_ZHIPUAI: _ClassVar[ProviderCodeEnum]
    PROVIDER_CODE_GROK: _ClassVar[ProviderCodeEnum]
    PROVIDER_CODE_DEEPSEEK: _ClassVar[ProviderCodeEnum]

class ProviderStatusEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    PROVIDER_STATUS_UNKNOWN: _ClassVar[ProviderStatusEnum]
    PROVIDER_STATUS_UNAVAILABLE: _ClassVar[ProviderStatusEnum]
    PROVIDER_STATUS_AVAILABLE: _ClassVar[ProviderStatusEnum]

class QuotaTypeEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    QUOTA_TYPE_UNKNOWN: _ClassVar[QuotaTypeEnum]
    QUOTA_TYPE_PAID: _ClassVar[QuotaTypeEnum]
    QUOTA_TYPE_FREE: _ClassVar[QuotaTypeEnum]
    QUOTA_TYPE_TRIAL: _ClassVar[QuotaTypeEnum]
MODEL_TYPE_UNKNOWN: ModelTypeEnum
MODEL_TYPE_LLM: ModelTypeEnum
MODEL_TYPE_TEXT_EMBEDDING: ModelTypeEnum
MODEL_TYPE_RERANK: ModelTypeEnum
MODEL_TYPE_SPEECH2TEXT: ModelTypeEnum
MODEL_TYPE_TTS: ModelTypeEnum
MODEL_TYPE_MODERATION: ModelTypeEnum
MODEL_TYPE_TEXT2IMAGE: ModelTypeEnum
MODEL_FEATURE_AGENT_THOUGHT: ModelFeatureEnum
MODEL_FEATURE_VISION: ModelFeatureEnum
MODEL_FEATURE_TOOL_CALL: ModelFeatureEnum
MODEL_FEATURE_MULTI_TOOL_CALL: ModelFeatureEnum
MODEL_FEATURE_STREAM_TOOL_CALL: ModelFeatureEnum
MODEL_FEATURE_DOCUMENT: ModelFeatureEnum
MODEL_FEATURE_VIDEO: ModelFeatureEnum
MODEL_FEATURE_AUDIO: ModelFeatureEnum
PROVIDER_CODE_UNKNOWN: ProviderCodeEnum
PROVIDER_CODE_OPENAI: ProviderCodeEnum
PROVIDER_CODE_TONGYI: ProviderCodeEnum
PROVIDER_CODE_ZHIPUAI: ProviderCodeEnum
PROVIDER_CODE_GROK: ProviderCodeEnum
PROVIDER_CODE_DEEPSEEK: ProviderCodeEnum
PROVIDER_STATUS_UNKNOWN: ProviderStatusEnum
PROVIDER_STATUS_UNAVAILABLE: ProviderStatusEnum
PROVIDER_STATUS_AVAILABLE: ProviderStatusEnum
QUOTA_TYPE_UNKNOWN: QuotaTypeEnum
QUOTA_TYPE_PAID: QuotaTypeEnum
QUOTA_TYPE_FREE: QuotaTypeEnum
QUOTA_TYPE_TRIAL: QuotaTypeEnum

class ProviderDescriptionsRequest(_message.Message):
    __slots__ = ["header"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ...) -> None: ...

class ProviderDescriptionsResponse(_message.Message):
    __slots__ = ["header", "body"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: ProviderDescriptionsResponseBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[ProviderDescriptionsResponseBody, _Mapping]] = ...) -> None: ...

class ProviderDescriptionsResponseBody(_message.Message):
    __slots__ = ["status", "descriptions"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    status: _message_pb2.ResponseStatus
    descriptions: _containers.RepeatedCompositeFieldContainer[ProviderDescription]
    def __init__(self, status: _Optional[_Union[_message_pb2.ResponseStatus, _Mapping]] = ..., descriptions: _Optional[_Iterable[_Union[ProviderDescription, _Mapping]]] = ...) -> None: ...

class ProviderModelsRequest(_message.Message):
    __slots__ = ["header", "body"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: ProviderModelsRequestBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[ProviderModelsRequestBody, _Mapping]] = ...) -> None: ...

class ProviderModelsRequestBody(_message.Message):
    __slots__ = ["code", "modelType"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    MODELTYPE_FIELD_NUMBER: _ClassVar[int]
    code: ProviderCodeEnum
    modelType: ModelTypeEnum
    def __init__(self, code: _Optional[_Union[ProviderCodeEnum, str]] = ..., modelType: _Optional[_Union[ModelTypeEnum, str]] = ...) -> None: ...

class ProviderModelsResponse(_message.Message):
    __slots__ = ["header", "body"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: ProviderModelsResponseBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[ProviderModelsResponseBody, _Mapping]] = ...) -> None: ...

class ProviderModelsResponseBody(_message.Message):
    __slots__ = ["status", "models"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MODELS_FIELD_NUMBER: _ClassVar[int]
    status: _message_pb2.ResponseStatus
    models: _containers.RepeatedCompositeFieldContainer[ModelMetadata]
    def __init__(self, status: _Optional[_Union[_message_pb2.ResponseStatus, _Mapping]] = ..., models: _Optional[_Iterable[_Union[ModelMetadata, _Mapping]]] = ...) -> None: ...

class DeleteProviderRequest(_message.Message):
    __slots__ = ["header", "body"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: DeleteProviderRequestBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[DeleteProviderRequestBody, _Mapping]] = ...) -> None: ...

class DeleteProviderRequestBody(_message.Message):
    __slots__ = ["uid"]
    UID_FIELD_NUMBER: _ClassVar[int]
    uid: str
    def __init__(self, uid: _Optional[str] = ...) -> None: ...

class DeleteProviderResponse(_message.Message):
    __slots__ = ["header", "body"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: DeleteProviderResponseBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[DeleteProviderResponseBody, _Mapping]] = ...) -> None: ...

class DeleteProviderResponseBody(_message.Message):
    __slots__ = ["status"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: _message_pb2.ResponseStatus
    def __init__(self, status: _Optional[_Union[_message_pb2.ResponseStatus, _Mapping]] = ...) -> None: ...

class SearchProviderRequest(_message.Message):
    __slots__ = ["header", "body"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: SearchProviderRequestBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[SearchProviderRequestBody, _Mapping]] = ...) -> None: ...

class SearchProviderRequestBody(_message.Message):
    __slots__ = ["page", "condition"]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    page: _message_pb2.RequestPage
    condition: SearchProviderCondition
    def __init__(self, page: _Optional[_Union[_message_pb2.RequestPage, _Mapping]] = ..., condition: _Optional[_Union[SearchProviderCondition, _Mapping]] = ...) -> None: ...

class SearchProviderResponse(_message.Message):
    __slots__ = ["header", "body"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: SearchProviderResponseBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[SearchProviderResponseBody, _Mapping]] = ...) -> None: ...

class SearchProviderResponseBody(_message.Message):
    __slots__ = ["status", "providers"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PROVIDERS_FIELD_NUMBER: _ClassVar[int]
    status: _message_pb2.ResponseStatus
    providers: _containers.RepeatedCompositeFieldContainer[ProviderMetadata]
    def __init__(self, status: _Optional[_Union[_message_pb2.ResponseStatus, _Mapping]] = ..., providers: _Optional[_Iterable[_Union[ProviderMetadata, _Mapping]]] = ...) -> None: ...

class AddProviderRequest(_message.Message):
    __slots__ = ["header", "body"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: AddProviderRequestBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[AddProviderRequestBody, _Mapping]] = ...) -> None: ...

class AddProviderRequestBody(_message.Message):
    __slots__ = ["provider"]
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    provider: ProviderMetadata
    def __init__(self, provider: _Optional[_Union[ProviderMetadata, _Mapping]] = ...) -> None: ...

class AddProviderResponse(_message.Message):
    __slots__ = ["header", "body"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: AddProviderResponseBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[AddProviderResponseBody, _Mapping]] = ...) -> None: ...

class AddProviderResponseBody(_message.Message):
    __slots__ = ["status", "provider"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    status: _message_pb2.ResponseStatus
    provider: ProviderMetadata
    def __init__(self, status: _Optional[_Union[_message_pb2.ResponseStatus, _Mapping]] = ..., provider: _Optional[_Union[ProviderMetadata, _Mapping]] = ...) -> None: ...

class ProviderDetailRequest(_message.Message):
    __slots__ = ["header", "body"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: ProviderDetailRequestBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[ProviderDetailRequestBody, _Mapping]] = ...) -> None: ...

class ProviderDetailRequestBody(_message.Message):
    __slots__ = ["uid"]
    UID_FIELD_NUMBER: _ClassVar[int]
    uid: str
    def __init__(self, uid: _Optional[str] = ...) -> None: ...

class ProviderDetailResponse(_message.Message):
    __slots__ = ["header", "body"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    header: _message_pb2.MessageHeader
    body: ProviderDetailResponseBody
    def __init__(self, header: _Optional[_Union[_message_pb2.MessageHeader, _Mapping]] = ..., body: _Optional[_Union[ProviderDetailResponseBody, _Mapping]] = ...) -> None: ...

class ProviderDetailResponseBody(_message.Message):
    __slots__ = ["status", "detail"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DETAIL_FIELD_NUMBER: _ClassVar[int]
    status: _message_pb2.ResponseStatus
    detail: ProviderDetail
    def __init__(self, status: _Optional[_Union[_message_pb2.ResponseStatus, _Mapping]] = ..., detail: _Optional[_Union[ProviderDetail, _Mapping]] = ...) -> None: ...

class ProviderDetail(_message.Message):
    __slots__ = ["provider", "state"]
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    provider: ProviderMetadata
    state: ProviderState
    def __init__(self, provider: _Optional[_Union[ProviderMetadata, _Mapping]] = ..., state: _Optional[_Union[ProviderState, _Mapping]] = ...) -> None: ...

class ProviderDescription(_message.Message):
    __slots__ = ["code", "name", "description", "supportedModelTypes", "avatar"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SUPPORTEDMODELTYPES_FIELD_NUMBER: _ClassVar[int]
    AVATAR_FIELD_NUMBER: _ClassVar[int]
    code: ProviderCodeEnum
    name: str
    description: str
    supportedModelTypes: _containers.RepeatedScalarFieldContainer[ModelTypeEnum]
    avatar: str
    def __init__(self, code: _Optional[_Union[ProviderCodeEnum, str]] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., supportedModelTypes: _Optional[_Iterable[_Union[ModelTypeEnum, str]]] = ..., avatar: _Optional[str] = ...) -> None: ...

class SearchProviderCondition(_message.Message):
    __slots__ = ["code"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    code: ProviderCodeEnum
    def __init__(self, code: _Optional[_Union[ProviderCodeEnum, str]] = ...) -> None: ...

class ProviderMetadata(_message.Message):
    __slots__ = ["uid", "owner", "name", "code", "config", "quotaType", "quotaLimit", "createdAt", "updatedAt", "signature"]
    UID_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    QUOTATYPE_FIELD_NUMBER: _ClassVar[int]
    QUOTALIMIT_FIELD_NUMBER: _ClassVar[int]
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    UPDATEDAT_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    uid: str
    owner: str
    name: str
    code: ProviderCodeEnum
    config: str
    quotaType: QuotaTypeEnum
    quotaLimit: int
    createdAt: str
    updatedAt: str
    signature: str
    def __init__(self, uid: _Optional[str] = ..., owner: _Optional[str] = ..., name: _Optional[str] = ..., code: _Optional[_Union[ProviderCodeEnum, str]] = ..., config: _Optional[str] = ..., quotaType: _Optional[_Union[QuotaTypeEnum, str]] = ..., quotaLimit: _Optional[int] = ..., createdAt: _Optional[str] = ..., updatedAt: _Optional[str] = ..., signature: _Optional[str] = ...) -> None: ...

class ModelMetadata(_message.Message):
    __slots__ = ["providerCode", "type", "name", "features"]
    PROVIDERCODE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    FEATURES_FIELD_NUMBER: _ClassVar[int]
    providerCode: ProviderCodeEnum
    type: ModelTypeEnum
    name: str
    features: _containers.RepeatedScalarFieldContainer[ModelFeatureEnum]
    def __init__(self, providerCode: _Optional[_Union[ProviderCodeEnum, str]] = ..., type: _Optional[_Union[ModelTypeEnum, str]] = ..., name: _Optional[str] = ..., features: _Optional[_Iterable[_Union[ModelFeatureEnum, str]]] = ...) -> None: ...

class ProviderState(_message.Message):
    __slots__ = ["serviceDid", "uid", "status", "quotaUsed", "createdAt", "updatedAt", "signature"]
    SERVICEDID_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    QUOTAUSED_FIELD_NUMBER: _ClassVar[int]
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    UPDATEDAT_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    serviceDid: str
    uid: str
    status: ProviderStatusEnum
    quotaUsed: int
    createdAt: str
    updatedAt: str
    signature: str
    def __init__(self, serviceDid: _Optional[str] = ..., uid: _Optional[str] = ..., status: _Optional[_Union[ProviderStatusEnum, str]] = ..., quotaUsed: _Optional[int] = ..., createdAt: _Optional[str] = ..., updatedAt: _Optional[str] = ..., signature: _Optional[str] = ...) -> None: ...
