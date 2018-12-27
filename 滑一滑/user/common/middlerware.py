from django.utils.deprecation import MiddlewareMixin

from user.common.errors import LOGIN_REQUIRE, Fail, ErrorCodeException
from user.models import User
from user.lib.http import render_json


class AuthMiddleware(MiddlewareMixin):
    white_list = [
        '/user/vcode',
        '/user/login'
    ]

    def process_request(self, request):
        if request.path in self.white_list:
            return
        uid = request.session.get('uid', None)
        if not uid:
            raise LOGIN_REQUIRE
        else:
            try:
                user = User.objects.get(pk=uid)
            except User.DoesNotExist:
                raise Fail
            else:
                request.user = user


class ErrorCodeMiddleware(MiddlewareMixin):
    def process_execption(self, request, execpt):
        if isinstance(execpt, ErrorCodeException):
            print("*"*19)
            render_json(None, execpt.code)

