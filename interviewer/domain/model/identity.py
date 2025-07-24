import codecs

from interviewer.tool.signature import verify


def encodeKey(key):
    return codecs.decode(key[2:] if key.startswith("0x") else key, 'hex')


def convertDidToPublicKey(did):
    public_key = did.split(":")[-1]
    return public_key[2:] if public_key.startswith("0x") else public_key


def verifyIdentity(identity):
    signature = identity.signature
    try:
        identity.signature = ''
        public_key = encodeKey(convertDidToPublicKey(identity.metadata.did))
        return verify(public_key=public_key, data=identity.SerializeToString(), signature=signature)
    finally:
        identity.signature = signature
