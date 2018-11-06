from django.db import models

class User(models.Model):
    u_name = models.CharField(max_length=32,unique=True)
    u_passwd = models.CharField(max_length=255)
    u_phone = models.CharField(max_length=16,unique=True)
    u_icon = models.ImageField(upload_to='icons/%Y/%m/%d',default="icons/default.jpg")
    u_is_delete = models.BooleanField(default=False)
    u_is_active = models.BooleanField(default=False)
    u_ispay = models.BooleanField(default=False)
