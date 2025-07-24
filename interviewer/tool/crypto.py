import base64
import codecs
import hashlib
import os

from cryptography.hazmat.primitives.ciphers.aead import AESGCM


def generate_text_hash(text: str) -> str:
    hash_text = str(text) + "None"
    return hashlib.sha256(hash_text.encode()).hexdigest()


def encodeString(s):
    return s.encode('utf-8')


def decodeString(b):
    return b.decode('utf-8')


def generateIv(length=12):
    return os.urandom(length)


def encodeBase64(b):
    return base64.b64encode(b)


def decodeBase64(b):
    return base64.b64decode(b)


def computeHash(b):
    return hashlib.sha256(b).digest()


def encodeHex(b):
    return codecs.encode(b, 'hex').decode('utf-8')


def decodeHex(s):
    return codecs.decode(s, 'hex')


def encrypt(key, nonce, b):
    aesgcm = AESGCM(key)
    return aesgcm.encrypt(nonce, b, None)


def decrypt(key, nonce, b):
    aesgcm = AESGCM(key)
    return aesgcm.decrypt(nonce, b, None)
