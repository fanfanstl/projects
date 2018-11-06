from django.db import models

from movie_user.contant import PERMISSION_NONE


class UserModel(models.Model):
    username = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=256, null=False)
    phone = models.CharField(max_length=32, unique=True)
    is_delete = models.BooleanField(default=False)
    permission = models.IntegerField(default=PERMISSION_NONE)


class Letter(models.Model):
    letter = models.CharField(max_length=1)


class City(models.Model):
    c_id = models.IntegerField(default=0)
    c_parent_id = models.IntegerField(default=0)
    c_region_name = models.CharField(max_length=16)
    c_city_code = models.IntegerField(default=0)
    c_pinyin = models.CharField(max_length=64)
    c_letter = models.ForeignKey(Letter)



