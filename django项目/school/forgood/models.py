from django.db import models

# 类别表
from forclass.models import User


class Type(models.Model):
    t_name = models.CharField(max_length=128)


# 物品表   类别表1 ：n物品表
class Good(models.Model):
    g_name = models.CharField(max_length=128)
    g_price = models.FloatField(default=0)
    g_des = models.TextField(default="无描述")
    g_phone = models.CharField(max_length=16, default="12345678910")
    g_addr = models.CharField(max_length=255, default="山西大学大东关校区")
    g_img_one = models.ImageField(upload_to="goods/%Y/%m/%m/")
    g_img_two = models.ImageField(upload_to="goods/%Y/%m/%m/")
    g_collected = models.IntegerField(default=0)
    g_type = models.ForeignKey(Type)


# 购物车
class Cart(models.Model):
    c_good = models.ForeignKey(Good)
    c_user = models.ForeignKey(User)
    is_select = models.BooleanField(default=True)
    c_goods_num = models.IntegerField(default=1)
