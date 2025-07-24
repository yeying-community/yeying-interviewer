import uuid


def unicode_encode(name):
    return name.encode('unicode-escape').decode('utf-8')


def unicode_decode(name):
    return name.encode('utf-8').decode('unicode-escape')


def generateUuid():
    return str(uuid.uuid4())


def isEmpty(s):
    return False if s and not s.isspace() else True
