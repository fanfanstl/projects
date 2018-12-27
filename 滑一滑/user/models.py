import datetime

from django.db import models


class BaseModel(models.Model):
    class Meta:
        abstract = True

    def to_dict(self,ignore=()): # 这里的ignore使用元组
        att_dict = {}
        for field in self._meta.fields: # 获取Model对象
            if field not in ignore:
                att_dict[field.attname] = getattr(self, field.attname)
        return att_dict


class User(BaseModel):
    SEX = (
        ('男性', '男性'),
        ('女性', '女性'),
    )
    phonenum = models.CharField(max_length=16, unique=True)
    nickname = models.CharField(max_length=32, unique=True)
    sex = models.CharField(max_length=8, choices=SEX)

    birth_year = models.IntegerField(verbose_name='出生年', default=2000)
    birth_month = models.IntegerField(verbose_name='出生月', default=1)
    birth_day = models.IntegerField(verbose_name='出生日', default=1)

    avatar = models.CharField(max_length=256, verbose_name='个人形象')
    location = models.CharField(max_length=32, verbose_name='常居地')

    @property
    def age(self):
        today = datetime.date.today()
        birth_time = datetime.date(self.birth_year, self.birth_month, self.birth_day)
        return (today - birth_time) // 365


class Profile(BaseModel):
    SEX = (
        ('男性', '男性'),
        ('女性', '女性'),
    )
    dating_sex = models.CharField(max_length=8, choices=SEX, verbose_name='匹配的性别')
    location = models.CharField(max_length=32, verbose_name='目标城市')

    min_distance = models.IntegerField(default=1, verbose_name='最小查找范围')
    max_distance = models.IntegerField(default=10, verbose_name='最大查找范围')

    min_dating_age = models.IntegerField(verbose_name='最小交友年龄', default=18)
    max_dating_age = models.IntegerField(verbose_name='最大交友年龄', default=50)

    vibration = models.BooleanField(default=True, verbose_name='是否开启震动')
    only_matche = models.BooleanField(default=True, verbose_name='不让未匹配的人看我的相册')
    auto_play = models.BooleanField(default=True, verbose_name='是否自动播放视频')

