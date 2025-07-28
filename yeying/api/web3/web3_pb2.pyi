from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class IdentityCodeEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    IDENTITY_CODE_UNKNOWN: _ClassVar[IdentityCodeEnum]
    IDENTITY_CODE_PERSONAL: _ClassVar[IdentityCodeEnum]
    IDENTITY_CODE_ORGANIZATION: _ClassVar[IdentityCodeEnum]
    IDENTITY_CODE_SERVICE: _ClassVar[IdentityCodeEnum]
    IDENTITY_CODE_APPLICATION: _ClassVar[IdentityCodeEnum]
    IDENTITY_CODE_ASSET: _ClassVar[IdentityCodeEnum]

class NetworkTypeEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NETWORK_TYPE_UNKNOWN: _ClassVar[NetworkTypeEnum]
    NETWORK_TYPE_YEYING: _ClassVar[NetworkTypeEnum]
IDENTITY_CODE_UNKNOWN: IdentityCodeEnum
IDENTITY_CODE_PERSONAL: IdentityCodeEnum
IDENTITY_CODE_ORGANIZATION: IdentityCodeEnum
IDENTITY_CODE_SERVICE: IdentityCodeEnum
IDENTITY_CODE_APPLICATION: IdentityCodeEnum
IDENTITY_CODE_ASSET: IdentityCodeEnum
NETWORK_TYPE_UNKNOWN: NetworkTypeEnum
NETWORK_TYPE_YEYING: NetworkTypeEnum

class Identity(_message.Message):
    __slots__ = ("metadata", "blockAddress", "securityConfig", "registry", "signature", "personalExtend", "serviceExtend", "organizationExtend", "applicationExtend")
    METADATA_FIELD_NUMBER: _ClassVar[int]
    BLOCKADDRESS_FIELD_NUMBER: _ClassVar[int]
    SECURITYCONFIG_FIELD_NUMBER: _ClassVar[int]
    REGISTRY_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    PERSONALEXTEND_FIELD_NUMBER: _ClassVar[int]
    SERVICEEXTEND_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATIONEXTEND_FIELD_NUMBER: _ClassVar[int]
    APPLICATIONEXTEND_FIELD_NUMBER: _ClassVar[int]
    metadata: IdentityMetadata
    blockAddress: str
    securityConfig: SecurityConfig
    registry: Registry
    signature: str
    personalExtend: IdentityPersonalExtend
    serviceExtend: IdentityServiceExtend
    organizationExtend: IdentityOrganizationExtend
    applicationExtend: IdentityApplicationExtend
    def __init__(self, metadata: _Optional[_Union[IdentityMetadata, _Mapping]] = ..., blockAddress: _Optional[str] = ..., securityConfig: _Optional[_Union[SecurityConfig, _Mapping]] = ..., registry: _Optional[_Union[Registry, _Mapping]] = ..., signature: _Optional[str] = ..., personalExtend: _Optional[_Union[IdentityPersonalExtend, _Mapping]] = ..., serviceExtend: _Optional[_Union[IdentityServiceExtend, _Mapping]] = ..., organizationExtend: _Optional[_Union[IdentityOrganizationExtend, _Mapping]] = ..., applicationExtend: _Optional[_Union[IdentityApplicationExtend, _Mapping]] = ...) -> None: ...

class Registry(_message.Message):
    __slots__ = ("nodes",)
    NODES_FIELD_NUMBER: _ClassVar[int]
    nodes: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, nodes: _Optional[_Iterable[str]] = ...) -> None: ...

class IdentityMetadata(_message.Message):
    __slots__ = ("parent", "network", "did", "version", "address", "name", "description", "code", "avatar", "createdAt", "updatedAt")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    DID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    AVATAR_FIELD_NUMBER: _ClassVar[int]
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    UPDATEDAT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    network: NetworkTypeEnum
    did: str
    version: int
    address: str
    name: str
    description: str
    code: IdentityCodeEnum
    avatar: str
    createdAt: str
    updatedAt: str
    def __init__(self, parent: _Optional[str] = ..., network: _Optional[_Union[NetworkTypeEnum, str]] = ..., did: _Optional[str] = ..., version: _Optional[int] = ..., address: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., code: _Optional[_Union[IdentityCodeEnum, str]] = ..., avatar: _Optional[str] = ..., createdAt: _Optional[str] = ..., updatedAt: _Optional[str] = ...) -> None: ...

class BlockAddress(_message.Message):
    __slots__ = ("identifier", "address", "privateKey", "publicKey", "mnemonic")
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PRIVATEKEY_FIELD_NUMBER: _ClassVar[int]
    PUBLICKEY_FIELD_NUMBER: _ClassVar[int]
    MNEMONIC_FIELD_NUMBER: _ClassVar[int]
    identifier: str
    address: str
    privateKey: str
    publicKey: str
    mnemonic: Mnemonic
    def __init__(self, identifier: _Optional[str] = ..., address: _Optional[str] = ..., privateKey: _Optional[str] = ..., publicKey: _Optional[str] = ..., mnemonic: _Optional[_Union[Mnemonic, _Mapping]] = ...) -> None: ...

class Mnemonic(_message.Message):
    __slots__ = ("phrase", "path", "locale", "password")
    PHRASE_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    phrase: str
    path: str
    locale: str
    password: str
    def __init__(self, phrase: _Optional[str] = ..., path: _Optional[str] = ..., locale: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class IdentityServiceExtend(_message.Message):
    __slots__ = ("code", "apiCodes", "proxy", "grpc", "extend")
    CODE_FIELD_NUMBER: _ClassVar[int]
    APICODES_FIELD_NUMBER: _ClassVar[int]
    PROXY_FIELD_NUMBER: _ClassVar[int]
    GRPC_FIELD_NUMBER: _ClassVar[int]
    EXTEND_FIELD_NUMBER: _ClassVar[int]
    code: str
    apiCodes: str
    proxy: str
    grpc: str
    extend: str
    def __init__(self, code: _Optional[str] = ..., apiCodes: _Optional[str] = ..., proxy: _Optional[str] = ..., grpc: _Optional[str] = ..., extend: _Optional[str] = ...) -> None: ...

class IdentityOrganizationExtend(_message.Message):
    __slots__ = ("address", "code", "extend")
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    EXTEND_FIELD_NUMBER: _ClassVar[int]
    address: str
    code: str
    extend: str
    def __init__(self, address: _Optional[str] = ..., code: _Optional[str] = ..., extend: _Optional[str] = ...) -> None: ...

class IdentityPersonalExtend(_message.Message):
    __slots__ = ("email", "telephone", "extend")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    TELEPHONE_FIELD_NUMBER: _ClassVar[int]
    EXTEND_FIELD_NUMBER: _ClassVar[int]
    email: str
    telephone: str
    extend: str
    def __init__(self, email: _Optional[str] = ..., telephone: _Optional[str] = ..., extend: _Optional[str] = ...) -> None: ...

class IdentityApplicationExtend(_message.Message):
    __slots__ = ("code", "serviceCodes", "location", "hash", "extend")
    CODE_FIELD_NUMBER: _ClassVar[int]
    SERVICECODES_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    EXTEND_FIELD_NUMBER: _ClassVar[int]
    code: str
    serviceCodes: str
    location: str
    hash: str
    extend: str
    def __init__(self, code: _Optional[str] = ..., serviceCodes: _Optional[str] = ..., location: _Optional[str] = ..., hash: _Optional[str] = ..., extend: _Optional[str] = ...) -> None: ...

class SecurityConfig(_message.Message):
    __slots__ = ("algorithm",)
    ALGORITHM_FIELD_NUMBER: _ClassVar[int]
    algorithm: SecurityAlgorithm
    def __init__(self, algorithm: _Optional[_Union[SecurityAlgorithm, _Mapping]] = ...) -> None: ...

class SecurityAlgorithm(_message.Message):
    __slots__ = ("name", "iv")
    NAME_FIELD_NUMBER: _ClassVar[int]
    IV_FIELD_NUMBER: _ClassVar[int]
    name: str
    iv: str
    def __init__(self, name: _Optional[str] = ..., iv: _Optional[str] = ...) -> None: ...
