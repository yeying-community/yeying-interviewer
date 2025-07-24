from interviewer.domain.model.exception import PermissionDeniedException, InvalidArgumentException
from interviewer.domain.model.identity import encodeKey, convertDidToPublicKey
from interviewer.tool.date import getCurrentUtcString, isExpired
from interviewer.tool.object import composite
from interviewer.tool.signature import sign, verify
from interviewer.tool.string import generateUuid
from yeying.api.common import AuthenticateTypeEnum, MessageHeader


def verifyData(did: str, data: bytes, signature: str):
    if not verify(public_key=encodeKey(convertDidToPublicKey(did)), data=data, signature=signature):
        raise PermissionDeniedException('Invalid signature!')


class Authenticate(object):
    def __init__(self, blockAddress):
        self.blockAddress = blockAddress
        self.validity = 5

    def getDid(self):
        return self.blockAddress.identifier

    def createHeader(self, body=None):
        header = MessageHeader()
        header.did = self.blockAddress.identifier
        header.authType = AuthenticateTypeEnum.AUTHENTICATE_TYPE_CERT
        header.nonce = generateUuid()
        header.version = 0
        header.timestamp = getCurrentUtcString()

        if body is None:
            data = header.SerializeToString()
        else:
            data = composite(header.SerializeToString(), body.SerializeToString())

        header.authContent = self.signData(data)
        return header

    def verifyHeader(self, header, body=None):
        if isExpired(header.timestamp, self.validity):
            raise InvalidArgumentException('request expired!')

        signature = header.authContent
        header.authContent = ''
        if body is None:
            data = header.SerializeToString()
        else:
            data = composite(header.SerializeToString(), body.SerializeToString())

        verifyData(did=header.did, data=data, signature=signature)

    def signData(self, data: bytes):
        privateKey = encodeKey(self.blockAddress.privateKey)
        return sign(privateKey, data)