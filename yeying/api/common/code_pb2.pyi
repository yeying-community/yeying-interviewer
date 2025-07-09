from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ResponseCodeEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RESPONSE_CODE_UNKNOWN: _ClassVar[ResponseCodeEnum]
    OK: _ClassVar[ResponseCodeEnum]
    INVALID_ARGUMENT: _ClassVar[ResponseCodeEnum]
    UNAUTHENTICATED: _ClassVar[ResponseCodeEnum]
    PERMISSION_DENIED: _ClassVar[ResponseCodeEnum]
    NOT_FOUND: _ClassVar[ResponseCodeEnum]
    ALREADY_EXISTS: _ClassVar[ResponseCodeEnum]
    LIMIT_EXCEEDED: _ClassVar[ResponseCodeEnum]
    UNAVAILABLE: _ClassVar[ResponseCodeEnum]
    UNKNOWN_ERROR: _ClassVar[ResponseCodeEnum]
    NETWORK_ERROR: _ClassVar[ResponseCodeEnum]
    INVALID_CERT: _ClassVar[ResponseCodeEnum]
    NOT_SUPPORTED: _ClassVar[ResponseCodeEnum]
    DATA_CORRUPTED: _ClassVar[ResponseCodeEnum]

class ContractStatusEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONTRACT_STATUS_UNKNOWN: _ClassVar[ContractStatusEnum]
    CONTRACT_STATUS_INACTIVATED: _ClassVar[ContractStatusEnum]
    CONTRACT_STATUS_ACTIVATED: _ClassVar[ContractStatusEnum]
    CONTRACT_STATUS_EXPIRED: _ClassVar[ContractStatusEnum]
    CONTRACT_STATUS_CANCELED: _ClassVar[ContractStatusEnum]

class LanguageCodeEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LANGUAGE_CODE_UNKNOWN: _ClassVar[LanguageCodeEnum]
    LANGUAGE_CODE_ZH_CH: _ClassVar[LanguageCodeEnum]
    LANGUAGE_CODE_EN_US: _ClassVar[LanguageCodeEnum]

class ApplicationCodeEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    APPLICATION_CODE_UNKNOWN: _ClassVar[ApplicationCodeEnum]
    APPLICATION_CODE_MARKET: _ClassVar[ApplicationCodeEnum]
    APPLICATION_CODE_ASSET: _ClassVar[ApplicationCodeEnum]
    APPLICATION_CODE_KNOWLEDGE: _ClassVar[ApplicationCodeEnum]
    APPLICATION_CODE_KEEPER: _ClassVar[ApplicationCodeEnum]
    APPLICATION_CODE_SOCIAL: _ClassVar[ApplicationCodeEnum]
    APPLICATION_CODE_WORKBENCH: _ClassVar[ApplicationCodeEnum]

class ServiceCodeEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SERVICE_CODE_UNKNOWN: _ClassVar[ServiceCodeEnum]
    SERVICE_CODE_NODE: _ClassVar[ServiceCodeEnum]
    SERVICE_CODE_WAREHOUSE: _ClassVar[ServiceCodeEnum]
    SERVICE_CODE_AGENT: _ClassVar[ServiceCodeEnum]
    SERVICE_CODE_MCP: _ClassVar[ServiceCodeEnum]

class ApiCodeEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    API_CODE_UNKNOWN: _ClassVar[ApiCodeEnum]
    API_CODE_USER: _ClassVar[ApiCodeEnum]
    API_CODE_IDENTITY: _ClassVar[ApiCodeEnum]
    API_CODE_LLM_SERVICE: _ClassVar[ApiCodeEnum]
    API_CODE_LLM_PROVIDER: _ClassVar[ApiCodeEnum]
    API_CODE_ASSET_SERVICE: _ClassVar[ApiCodeEnum]
    API_CODE_ASSET_BLOCK: _ClassVar[ApiCodeEnum]
    API_CODE_ASSET_LINK: _ClassVar[ApiCodeEnum]
    API_CODE_ASSET_NAMESPACE: _ClassVar[ApiCodeEnum]
    API_CODE_ASSET_RECYCLE: _ClassVar[ApiCodeEnum]
    API_CODE_CERTIFICATE: _ClassVar[ApiCodeEnum]
    API_CODE_STORAGE: _ClassVar[ApiCodeEnum]
    API_CODE_APPLICATION: _ClassVar[ApiCodeEnum]
    API_CODE_EVENT: _ClassVar[ApiCodeEnum]
    API_CODE_INVITATION: _ClassVar[ApiCodeEnum]
    API_CODE_SERVICE: _ClassVar[ApiCodeEnum]

class ImageFormatEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    IMAGE_FORMAT_UNKNOWN: _ClassVar[ImageFormatEnum]
    IMAGE_FORMAT_PNG: _ClassVar[ImageFormatEnum]

class DigitalFormatEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DIGITAL_FORMAT_UNKNOWN: _ClassVar[DigitalFormatEnum]
    DIGITAL_FORMAT_TEXT: _ClassVar[DigitalFormatEnum]
    DIGITAL_FORMAT_IMAGE: _ClassVar[DigitalFormatEnum]
    DIGITAL_FORMAT_VIDEO: _ClassVar[DigitalFormatEnum]
    DIGITAL_FORMAT_AUDIO: _ClassVar[DigitalFormatEnum]
    DIGITAL_FORMAT_APP: _ClassVar[DigitalFormatEnum]
    DIGITAL_FORMAT_OTHER: _ClassVar[DigitalFormatEnum]

class ContentFormatEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONTENT_FORMAT_UNKNOWN: _ClassVar[ContentFormatEnum]
    CONTENT_FORMAT_URL: _ClassVar[ContentFormatEnum]
    CONTENT_FORMAT_BASE64: _ClassVar[ContentFormatEnum]

class SessionSceneEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SESSION_SCENE_UNKNOWN: _ClassVar[SessionSceneEnum]
    SESSION_SCENE_DIALOGUE: _ClassVar[SessionSceneEnum]
    SESSION_SCENE_DRAWING: _ClassVar[SessionSceneEnum]
    SESSION_SCENE_TRANSLATION: _ClassVar[SessionSceneEnum]

class SessionRoleEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SESSION_ROLE_UNKNOWN: _ClassVar[SessionRoleEnum]
    SESSION_ROLE_PARTICIPANT: _ClassVar[SessionRoleEnum]
    SESSION_ROLE_ADMIN: _ClassVar[SessionRoleEnum]

class ParticipantTypeEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PARTICIPANT_TYPE_UNKNOWN: _ClassVar[ParticipantTypeEnum]
    PARTICIPANT_TYPE_SERVICE: _ClassVar[ParticipantTypeEnum]
    PARTICIPANT_TYPE_PEOPLE: _ClassVar[ParticipantTypeEnum]

class AuditTypeEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AUDIT_TYPE_APPLICATION: _ClassVar[AuditTypeEnum]
    AUDIT_TYPE_SERVICE: _ClassVar[AuditTypeEnum]
    AUDIT_TYPE_UNKNOWN: _ClassVar[AuditTypeEnum]

class ApplicationStatusEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    APPLICATION_STATUS_UNKNOWN: _ClassVar[ApplicationStatusEnum]
    APPLICATION_STATUS_CREATED: _ClassVar[ApplicationStatusEnum]
    APPLICATION_STATUS_AUDITED: _ClassVar[ApplicationStatusEnum]
    APPLICATION_STATUS_REFUSED: _ClassVar[ApplicationStatusEnum]
    APPLICATION_STATUS_OFFLINE: _ClassVar[ApplicationStatusEnum]
    APPLICATION_STATUS_ONLINE: _ClassVar[ApplicationStatusEnum]

class CipherTypeEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CIPHER_TYPE_UNKNOWN: _ClassVar[CipherTypeEnum]
    CIPHER_TYPE_AES_GCM_256: _ClassVar[CipherTypeEnum]

class AuthenticateTypeEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AUTHENTICATE_TYPE_UNKNOWN: _ClassVar[AuthenticateTypeEnum]
    AUTHENTICATE_TYPE_CERT: _ClassVar[AuthenticateTypeEnum]
    AUTHENTICATE_TYPE_TOKEN: _ClassVar[AuthenticateTypeEnum]
RESPONSE_CODE_UNKNOWN: ResponseCodeEnum
OK: ResponseCodeEnum
INVALID_ARGUMENT: ResponseCodeEnum
UNAUTHENTICATED: ResponseCodeEnum
PERMISSION_DENIED: ResponseCodeEnum
NOT_FOUND: ResponseCodeEnum
ALREADY_EXISTS: ResponseCodeEnum
LIMIT_EXCEEDED: ResponseCodeEnum
UNAVAILABLE: ResponseCodeEnum
UNKNOWN_ERROR: ResponseCodeEnum
NETWORK_ERROR: ResponseCodeEnum
INVALID_CERT: ResponseCodeEnum
NOT_SUPPORTED: ResponseCodeEnum
DATA_CORRUPTED: ResponseCodeEnum
CONTRACT_STATUS_UNKNOWN: ContractStatusEnum
CONTRACT_STATUS_INACTIVATED: ContractStatusEnum
CONTRACT_STATUS_ACTIVATED: ContractStatusEnum
CONTRACT_STATUS_EXPIRED: ContractStatusEnum
CONTRACT_STATUS_CANCELED: ContractStatusEnum
LANGUAGE_CODE_UNKNOWN: LanguageCodeEnum
LANGUAGE_CODE_ZH_CH: LanguageCodeEnum
LANGUAGE_CODE_EN_US: LanguageCodeEnum
APPLICATION_CODE_UNKNOWN: ApplicationCodeEnum
APPLICATION_CODE_MARKET: ApplicationCodeEnum
APPLICATION_CODE_ASSET: ApplicationCodeEnum
APPLICATION_CODE_KNOWLEDGE: ApplicationCodeEnum
APPLICATION_CODE_KEEPER: ApplicationCodeEnum
APPLICATION_CODE_SOCIAL: ApplicationCodeEnum
APPLICATION_CODE_WORKBENCH: ApplicationCodeEnum
SERVICE_CODE_UNKNOWN: ServiceCodeEnum
SERVICE_CODE_NODE: ServiceCodeEnum
SERVICE_CODE_WAREHOUSE: ServiceCodeEnum
SERVICE_CODE_AGENT: ServiceCodeEnum
SERVICE_CODE_MCP: ServiceCodeEnum
API_CODE_UNKNOWN: ApiCodeEnum
API_CODE_USER: ApiCodeEnum
API_CODE_IDENTITY: ApiCodeEnum
API_CODE_LLM_SERVICE: ApiCodeEnum
API_CODE_LLM_PROVIDER: ApiCodeEnum
API_CODE_ASSET_SERVICE: ApiCodeEnum
API_CODE_ASSET_BLOCK: ApiCodeEnum
API_CODE_ASSET_LINK: ApiCodeEnum
API_CODE_ASSET_NAMESPACE: ApiCodeEnum
API_CODE_ASSET_RECYCLE: ApiCodeEnum
API_CODE_CERTIFICATE: ApiCodeEnum
API_CODE_STORAGE: ApiCodeEnum
API_CODE_APPLICATION: ApiCodeEnum
API_CODE_EVENT: ApiCodeEnum
API_CODE_INVITATION: ApiCodeEnum
API_CODE_SERVICE: ApiCodeEnum
IMAGE_FORMAT_UNKNOWN: ImageFormatEnum
IMAGE_FORMAT_PNG: ImageFormatEnum
DIGITAL_FORMAT_UNKNOWN: DigitalFormatEnum
DIGITAL_FORMAT_TEXT: DigitalFormatEnum
DIGITAL_FORMAT_IMAGE: DigitalFormatEnum
DIGITAL_FORMAT_VIDEO: DigitalFormatEnum
DIGITAL_FORMAT_AUDIO: DigitalFormatEnum
DIGITAL_FORMAT_APP: DigitalFormatEnum
DIGITAL_FORMAT_OTHER: DigitalFormatEnum
CONTENT_FORMAT_UNKNOWN: ContentFormatEnum
CONTENT_FORMAT_URL: ContentFormatEnum
CONTENT_FORMAT_BASE64: ContentFormatEnum
SESSION_SCENE_UNKNOWN: SessionSceneEnum
SESSION_SCENE_DIALOGUE: SessionSceneEnum
SESSION_SCENE_DRAWING: SessionSceneEnum
SESSION_SCENE_TRANSLATION: SessionSceneEnum
SESSION_ROLE_UNKNOWN: SessionRoleEnum
SESSION_ROLE_PARTICIPANT: SessionRoleEnum
SESSION_ROLE_ADMIN: SessionRoleEnum
PARTICIPANT_TYPE_UNKNOWN: ParticipantTypeEnum
PARTICIPANT_TYPE_SERVICE: ParticipantTypeEnum
PARTICIPANT_TYPE_PEOPLE: ParticipantTypeEnum
AUDIT_TYPE_APPLICATION: AuditTypeEnum
AUDIT_TYPE_SERVICE: AuditTypeEnum
AUDIT_TYPE_UNKNOWN: AuditTypeEnum
APPLICATION_STATUS_UNKNOWN: ApplicationStatusEnum
APPLICATION_STATUS_CREATED: ApplicationStatusEnum
APPLICATION_STATUS_AUDITED: ApplicationStatusEnum
APPLICATION_STATUS_REFUSED: ApplicationStatusEnum
APPLICATION_STATUS_OFFLINE: ApplicationStatusEnum
APPLICATION_STATUS_ONLINE: ApplicationStatusEnum
CIPHER_TYPE_UNKNOWN: CipherTypeEnum
CIPHER_TYPE_AES_GCM_256: CipherTypeEnum
AUTHENTICATE_TYPE_UNKNOWN: AuthenticateTypeEnum
AUTHENTICATE_TYPE_CERT: AuthenticateTypeEnum
AUTHENTICATE_TYPE_TOKEN: AuthenticateTypeEnum
