import uuid

from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse
from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.response import Response

from movie_user.models import UserModel
from movie_user.serializers import UserModelSerializers


class UsersView(CreateAPIView):
    serializer_class = UserModelSerializers
    queryset = UserModel

    def post(self, request, *args, **kwargs):
        action = request.GET.get("action")
        if action == 'login':
            username = request.POST.get("username")
            password = request.POST.get("password")
            print("==================================")
            user = UserModel.objects.filter(username=username).first()
            if not user:
                data = {
                    "status":400,
                    "msg":"用户名或密码错误"
                }
                return JsonResponse(data=data)
            # if user.password == password:
            if check_password(password,user.password):
                token = uuid.uuid4().hex
                data = {
                    "token":token,
                    "status":200,
                    "msg":"登录成功"
                }
                return JsonResponse(data)

        elif action == "register":
            return self.create(request, *args, **kwargs)
        else:
            data = {
                "status":400,
                "msg":"请输入有效的请求参数",
            }
            return JsonResponse(data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        username = request.data.get("username")
        user = UserModel.objects.get(username=username)
        user.password = make_password(user.password)
        print(user.password)
        user.save()
        headers = self.get_success_headers(serializer.data)
        data = serializer.data
        data["password"] = user.password

        return Response(data, status=status.HTTP_201_CREATED, headers=headers)


class UserView(RetrieveAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializers


