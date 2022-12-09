from core.exceptions import CustomException

class PasswordDoesNotMatchException(CustomException):
    code = 401
    error_code = 20000
    message = "password does not match"


class DuplicateEmailOrNicknameException(CustomException):
    code = 400
    error_code = 20001
    message = "duplicate email or nickname"


class UserNotFoundException(CustomException):
    code = 404
    error_code = 20002
    message = "user not found"

class UserNotDeletedException(CustomException):
    code = 304
    error_code = 20003
    message = "user not deleted"

class OtpMismatchException(CustomException):
    code = 403
    error_code = 20004
    message = 'otp mismatch'

class PasswordNotChangedException(CustomException):
    code = 304
    error_code = 20005
    message = "password not updated"