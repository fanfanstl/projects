from django.http import JsonResponse
from django.shortcuts import render
from django.utils.deprecation import MiddlewareMixin

from forclass.models import User
from school.settings import NEED_LOGIN_NORMAL, NEED_LOGIN_AJAX


class NeedLoginMiddleware(MiddlewareMixin):
    def process_request(self, request):
        query_path = request.path
        username = request.session.get("username", None)
        # 网页访问
        if query_path in NEED_LOGIN_NORMAL:
            if not username:
                return render(request, "usermanagement/login.html", context={"title": "登录"})
            else:
                request.user = User.objects.filter(u_name=username).first()

        # ajax访问
        if query_path in NEED_LOGIN_AJAX:
            if not username:
                data = {
                    "stat_code":901,
                    "msg":"请登录"
                }
                return JsonResponse(data)
            else:
                request.user = User.objects.filter(u_name=username).first()

