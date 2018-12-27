from django.db import models

from user.models import BaseModel


class Swiped(BaseModel):
    '''滑动记录表'''
    like_type = (
        ("左滑", "喜欢"),
        ("右滑", "不喜欢"),
        ("上滑", "超级喜欢"),
    )
    uid = models.IntegerField(null=False, verbose_name="滑动者id")
    sid = models.IntegerField(null=False, verbose_name="被滑动者id")
    mark = models.CharField(choices=like_type, max_length=16)
    time = models.DateTimeField(auto_now=True)


class Friend(BaseModel):
    '''好友关系表'''
    uid1 = models.IntegerField(null=False)
    uid2 = models.IntegerField(null=False)


