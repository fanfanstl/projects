from django.conf.urls import url

from forclass import views

urlpatterns=[
    url(r"^hellow/",views.hellow,name="hellow"),

    # 用户管理

    url(r"^register/",views.register,name="register"),
    url(r"^checkusername/",views.check_username,name="checkusername"),
    url(r"^checkphone/",views.check_phone,name="checkphone"),

    url(r"^login/",views.login,name="login"),
    url(r"^logout/",views.logout,name="logout"),




]