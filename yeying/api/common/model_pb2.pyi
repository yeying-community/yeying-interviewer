from yeying.api.common import code_pb2 as _code_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ApplicationMetadata(_message.Message):
    __slots__ = ("owner", "network", "address", "did", "version", "hash", "name", "code", "description", "location", "serviceCodes", "avatar", "createdAt", "updatedAt", "signature", "codePackagePath")
    OWNER_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    DID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    SERVICECODES_FIELD_NUMBER: _ClassVar[int]
    AVATAR_FIELD_NUMBER: _ClassVar[int]
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    UPDATEDAT_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    CODEPACKAGEPATH_FIELD_NUMBER: _ClassVar[int]
    owner: str
    network: str
    address: str
    did: str
    version: int
    hash: str
    name: str
    code: _code_pb2.ApplicationCodeEnum
    description: str
    location: str
    serviceCodes: _containers.RepeatedScalarFieldContainer[_code_pb2.ServiceCodeEnum]
    avatar: str
    createdAt: str
    updatedAt: str
    signature: str
    codePackagePath: str
    def __init__(self, owner: _Optional[str] = ..., network: _Optional[str] = ..., address: _Optional[str] = ..., did: _Optional[str] = ..., version: _Optional[int] = ..., hash: _Optional[str] = ..., name: _Optional[str] = ..., code: _Optional[_Union[_code_pb2.ApplicationCodeEnum, str]] = ..., description: _Optional[str] = ..., location: _Optional[str] = ..., serviceCodes: _Optional[_Iterable[_Union[_code_pb2.ServiceCodeEnum, str]]] = ..., avatar: _Optional[str] = ..., createdAt: _Optional[str] = ..., updatedAt: _Optional[str] = ..., signature: _Optional[str] = ..., codePackagePath: _Optional[str] = ...) -> None: ...

class ServiceMetadata(_message.Message):
    __slots__ = ("owner", "network", "address", "did", "version", "name", "description", "code", "apiCodes", "proxy", "grpc", "avatar", "createdAt", "updatedAt", "signature", "codePackagePath")
    OWNER_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    DID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    APICODES_FIELD_NUMBER: _ClassVar[int]
    PROXY_FIELD_NUMBER: _ClassVar[int]
    GRPC_FIELD_NUMBER: _ClassVar[int]
    AVATAR_FIELD_NUMBER: _ClassVar[int]
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    UPDATEDAT_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    CODEPACKAGEPATH_FIELD_NUMBER: _ClassVar[int]
    owner: str
    network: str
    address: str
    did: str
    version: int
    name: str
    description: str
    code: _code_pb2.ServiceCodeEnum
    apiCodes: _containers.RepeatedScalarFieldContainer[_code_pb2.ApiCodeEnum]
    proxy: str
    grpc: str
    avatar: str
    createdAt: str
    updatedAt: str
    signature: str
    codePackagePath: str
    def __init__(self, owner: _Optional[str] = ..., network: _Optional[str] = ..., address: _Optional[str] = ..., did: _Optional[str] = ..., version: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., code: _Optional[_Union[_code_pb2.ServiceCodeEnum, str]] = ..., apiCodes: _Optional[_Iterable[_Union[_code_pb2.ApiCodeEnum, str]]] = ..., proxy: _Optional[str] = ..., grpc: _Optional[str] = ..., avatar: _Optional[str] = ..., createdAt: _Optional[str] = ..., updatedAt: _Optional[str] = ..., signature: _Optional[str] = ..., codePackagePath: _Optional[str] = ...) -> None: ...

class StateMetadata(_message.Message):
    __slots__ = ("did", "version", "status", "signature", "createdAt", "updatedAt", "type")
    DID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    UPDATEDAT_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    did: str
    version: int
    status: _code_pb2.ApplicationStatusEnum
    signature: str
    createdAt: str
    updatedAt: str
    type: _code_pb2.AuditTypeEnum
    def __init__(self, did: _Optional[str] = ..., version: _Optional[int] = ..., status: _Optional[_Union[_code_pb2.ApplicationStatusEnum, str]] = ..., signature: _Optional[str] = ..., createdAt: _Optional[str] = ..., updatedAt: _Optional[str] = ..., type: _Optional[_Union[_code_pb2.AuditTypeEnum, str]] = ...) -> None: ...
