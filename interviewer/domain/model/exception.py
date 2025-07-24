
class UserCustomException(Exception):
    def __init__(self, message):
        super().__init__(message)


class PermissionDeniedException(UserCustomException):
    def __init__(self, message):
        super().__init__(message=message)


class UnavailableException(UserCustomException):
    def __init__(self, message):
        super().__init__(message=message)


class UnauthenticatedException(UserCustomException):
    def __init__(self, message):
        super().__init__(message=message)


class LimitExceededException(UserCustomException):
    def __init__(self, message):
        super().__init__(message=message)


class AlreadyExistException(UserCustomException):
    def __init__(self, message):
        super().__init__(message=message)


class NotFoundException(UserCustomException):
    def __init__(self, message):
        super().__init__(message=message)


class InvalidArgumentException(UserCustomException):
    def __init__(self, message):
        super().__init__(message=message)
