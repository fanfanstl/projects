import uuid

from django.contrib.auth.hashers import make_password, check_password
from django.core.cache import cache
from rest_framework.response import Response
from rest_framework.views import APIView

from app.auth_permission import Auth, Permission, RequireLogin
from app.models import UserModel, BlockModel
from app.serializers import UserModelSerializers, BlockModelSerializers
from app.utils import get_user


class UsersApi(APIView):
    def post(self, request):
        action = request.query_params.get("action")
        if action == "login":
            phone = request.data.get("phone")
            password = request.data.get("password")
            mail = request.data.get("mail")
            user_ident = mail or phone
            user = get_user(user_ident)
            if not user:
                return Response({"msg": "用户名或密码错误", "status": 400})
            if not check_password(password, user.password):
                return Response({"msg": "用户名或密码错误", "status": 400})
            token = uuid.uuid4().hex
            cache.set(token, user.id)
            data = {
                "status": 200,
                "msg": "login success",
                "token": token
            }
            return Response(data)
        elif action == "register":
            name = request.data.get("name")
            password = request.data.get("password")
            phone = request.data.get("phone")
            mail = request.data.get("mail")
            try:
                user = UserModel()
                user.name = name
                user.password = make_password(password)
                user.phone = phone
                user.mail = mail
                user.save()
            except Exception as e:
                print(str(e))
                return Response(data={"status": 400, "msg": "创建用户失败"})
            else:
                user_serializers = UserModelSerializers(user)
                data = {
                    "status": 201,
                    "msg": "create user ok",
                    "data": user_serializers.data
                }
                return Response(data)
        else:
            return Response(data={"status": 400, "msg": "请输入有效参数"})


class UserApi(APIView):
    authentication_classes = (Auth,)
    permission_classes = (Permission,)

    def delete(self, request, uid):
        user = UserModel.objects.filter(pk=uid).first()
        if not user:
            return Response({"msg": "要删除用户不存在"})
        user.is_delete = True
        user.save()
        return Response({"msg": "删除用户成功"})

    def put(self, request, uid):
        user = request.user
        if not user.id == int(uid):
            return Response({"msg": "用户不匹配"})

        name = request.data.get("name")
        password = request.data.get("password")
        phone = request.data.get("phone")
        mail = request.data.get("mail")
        user.name = name
        user.password = password
        user.phone = phone
        user.mail = mail
        user.save()
        user_serializers = UserModelSerializers(user)
        data = {
            "status": 203,
            "msg": "修改用户成功",
            "data": user_serializers.data
        }
        return Response(data)

    def patch(self, request, uid):
        user = request.user
        if not user.id == int(uid):
            return Response({"msg": "用户不匹配"})

        name = request.data.get("name")
        password = request.data.get("password")
        phone = request.data.get("phone")
        mail = request.data.get("mail")
        user.name = name
        user.password = password
        user.phone = phone
        user.mail = mail
        user.save()
        user_serializers = UserModelSerializers(user)
        data = {
            "status": 203,
            "msg": "修改用户成功",
            "data": user_serializers.data
        }
        return Response(data)


class BlocksApi(APIView):
    authentication_classes = (Auth,)
    permission_classes = (RequireLogin,)

    def post(self, request):
        title = request.data.get("title")
        content = request.data.get("content")
        user = request.user
        block = BlockModel()
        block.title = title
        block.b_user = user
        block.content = content
        block.save()
        block_serializers = BlockModelSerializers(block)
        data = {
            "status": 201,
            "msg": "create block ok",
            "data": block_serializers.data
        }
        return Response(data)


class BlockApi(APIView):
    authentication_classes = (Auth,)
    permission_classes = (RequireLogin,)

    def delete(self, request, bid):
        return Response()

    def put(self, request, bid):
        block = BlockModel.objects.filter(pk=bid).first()
        if not block:
            pass
        user = request.user
        if not user.id == int(block.b_user_id):
            return Response({"msg": "用户不匹配"})

        name = request.data.get("name")
        password = request.data.get("password")
        phone = request.data.get("phone")
        mail = request.data.get("mail")
        user.name = name
        user.password = password
        user.phone = phone
        user.mail = mail
        user.save()
        user_serializers = UserModelSerializers(user)
        data = {
            "status": 203,
            "msg": "修改用户成功",
            "data": user_serializers.data
        }
        return Response(data)

    def dispatch(self, request, bid):
        pass
