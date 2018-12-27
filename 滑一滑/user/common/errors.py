OK = 0


class ErrorCodeException(Exception):
    code = 0


def get_error_code_class(class_name, base_class, code):
    result_class = type(class_name, (base_class,), {'code':code})
    return result_class


Fail = get_error_code_class('Fail', ErrorCodeException, 1000)
LOGIN_REQUIRE = get_error_code_class('LOGIN_REQUIRE', ErrorCodeException, 1001)
USER_NOT_EXIST = get_error_code_class('USER_NOT_EXIST', ErrorCodeException, 1002)
PROFILE_ERROR = get_error_code_class('PROFILE_ERROR', ErrorCodeException, 1003)
