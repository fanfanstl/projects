from django.conf.urls import url

from app import views

urlpatterns = [
    # 数据准备
    url(r"^hellow/",views.hellow,name="hellow"),
    url(r"^addcarousel/",views.add_carousel,name="addcarousel"),
    url(r"^addmovies/",views.add_movies,name="addmovies"),

    # 逻辑实现
    # 主页
    url(r"^home/",views.home,name="home"),

    # 注册
    url(r"^register/",views.register,name="register"),

    # 登录
    url(r"^login/",views.login,name="login"),

    # 个人信息
    url(r"^selfinfo/",views.self_info,name="selfinfo"),

    # 刷新页面
    url(r"^myflush/",views.myflush,name="myflush"),

    # 收藏取消收藏
    url(r"^collect/",views.collect,name="collect"),

    # 个人收藏
    url(r"^selfcollect/",views.self_collect,name="selfcollect"),

    # 添加缓存
    url(r"^mycache/",views.mycache,name="mycache"),











]