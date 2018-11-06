from django.contrib.auth.hashers import make_password
from django.db import models

from app.contant import BLACK_USER, COMMON_USER


class UserModel(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=256)
    phone = models.CharField(max_length=16, unique=True)
    mail = models.CharField(max_length=128, unique=True)
    is_delete = models.BooleanField(default=False)
    permission = models.IntegerField(default=COMMON_USER)

    def check_permission(self, permission):
        print(permission, BLACK_USER, self.permission)
        if (BLACK_USER & self.permission) == BLACK_USER:
            return False
        else:
            return permission & self.permission == permission





class BlockModel(models.Model):
    title = models.CharField(max_length=128, unique=True)
    content = models.TextField()
    b_user = models.ForeignKey(UserModel,related_name="blocks")


class CollectModel(models.Model):
    c_user = models.ForeignKey(UserModel)
    c_block = models.ForeignKey(BlockModel)
    click = models.IntegerField(default=0)
