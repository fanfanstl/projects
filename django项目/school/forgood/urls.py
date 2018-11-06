from django.conf.urls import url

from forgood import views

urlpatterns=[

    # 数据添加
    url(r"^addgoods/",views.add_goods,name="addgoods"),


    # 实现
    url(r"^home/",views.home,name="home"),
    url(r"^homewithargument/(?P<tid>\d+)/",views.home_with_argument,name="homewithargument"),
    url(r"^querygood/",views.query_good,name="querygood"),
    url(r"^addgood/",views.add_good,name="addgood"),
    url(r"^changestate/",views.change_state,name="changestate"),


    url(r"^alipay/",views.alipay,name="alipay"),


]