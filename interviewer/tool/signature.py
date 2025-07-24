import binascii
import hashlib

from ecdsa import keys, util, curves


# 因为在生成签名的过程中每次都会选择一个新的随机数k，即使使用的是相同的私钥和相同的消息内容，由于k的不同，最终生成的（r, s）对也会不同，
# 因此签名每次都是唯一的
def sign(private_key, data, sigencode=util.sigencode_der):
    signingKey = keys.SigningKey.from_string(private_key, curve=curves.SECP256k1)
    digest = hashlib.sha256(data).digest()
    return binascii.hexlify(signingKey.sign_digest(digest=digest, sigencode=sigencode))


def verify(public_key: str, data: bytes, signature: str, sigdecode=util.sigdecode_der):
    vk = keys.VerifyingKey.from_string(public_key, curve=curves.SECP256k1)
    digest = hashlib.sha256(data).digest()
    return vk.verify_digest(signature=binascii.unhexlify(signature), digest=digest, sigdecode=sigdecode)
