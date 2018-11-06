from django.core.cache import cache
from rest_framework.authentication import BaseAuthentication
from rest_framework.permissions import BasePermission
from rest_framework.response import Response

from app.contant import COMMON_USER, VIP
from app.models import UserModel


class Auth(BaseAuthentication):
    def authenticate(self, request):
        token = request.query_params.get("token")
        if not token:
            return (None, None)
        user_id = cache.get(token)
        try:
            user = UserModel.objects.filter(pk=user_id).first()
        except:
            return (None, None)
        if not user:
            return (None, None)
        return (user, token)


class RequireLogin(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if not user:
            return False
        return True


class Permission(BasePermission):
    def has_permission(self, request, view):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        user = request.user
        if not user:
            return False
        if request.method == "DELETE":
            if not user.check_permission(VIP):
                return False
        if not user.check_permission(COMMON_USER):
            return False
        return True

# class PermissionVip(BasePermission):
#     def has_permission(self, request, view):
#         """
#         Return `True` if permission is granted, `False` otherwise.
#         """
#         user = request.user
#         if not user:
#             return False
#         if not user.check_permission(VIP):
#             return False
#         return True
