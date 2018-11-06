from django.db import models

# 用户表
class User(models.Model):
    u_name = models.CharField(max_length=16,unique=True)
    u_passwd = models.CharField(max_length=128,null=False)
    u_email = models.CharField(max_length=128,null=False,unique=True)
    # 相对于的是MEDIA_ROOT 媒体目录
    u_icon = models.ImageField(upload_to='icons/%Y/%m/%d')


#电影信息
class Movie(models.Model):
    m_postid = models.IntegerField(unique=True)
    m_title = models.CharField(max_length=255)
    m_img = models.CharField(max_length=255)
    m_duration = models.CharField(max_length=10)
    m_paa_fu_title = models.TextField()
    m_more = models.CharField(max_length=255,null=True)
    m_collected = models.IntegerField(default=0)
    m_user = models.ManyToManyField(User)


# 轮播
class Carousel(models.Model):
    c_url = models.CharField(max_length=255)
