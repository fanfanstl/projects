import random
from uuid import uuid4

from alipay import AliPay
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from forclass.models import User
from forgood.models import Type, Good
from forgood.view_constant import ALL

# 添加物品
from school.settings import APP_PRIVATE_KEY, ALIPAY_PUBLIC_KEY, APP_ID


def add_goods(request):
    for i in range(100):
        good = Good()
        good.g_name = "good%d" % i
        good.g_price = random.randrange(1, 101)
        good.g_img_one = 'http://img01.bqstatic.com/upload/goods/000/000/2172/0000002172.jpg@200w_200h_90Q'
        good.g_img_two = 'http://img01.bqstatic.com/upload/goods/000/000/2172/0000002172.jpg@200w_200h_90Q'
        good.g_type_id = random.randrange(1, 8)
        good.save()
    return HttpResponse("添加成功")


# 实现
def home(request):
    return redirect(reverse('forgood:homewithargument', kwargs={
        "tid": ALL,
    }))


def home_with_argument(request, tid):

    username = request.session.get("username")
    users = User.objects.filter(u_name=username)
    if not users.exists():
        user = None
        user_icon = None
    else:
        user = users.first()
        user_icon = "/static/upload/" + user.u_icon.url
    types = Type.objects.all()
    goods = Good.objects.all()
    if tid == ALL:
        goods = goods[0:20]
    else:
        goods = goods.filter(g_type_id=tid)
    data = {
        "title": "主页",
        "types": types,
        "goods": goods,
        "tid": int(tid),
        "user": user,
        "user_icon": user_icon
    }
    return render(request, "forgood/forgood_home.html", context=data)


def query_good(request):
    gid = request.GET.get("gid")
    good = Good.objects.get(id=gid)
    data = {
        "g_name": good.g_name,
        "g_des": good.g_des,
        "g_price": good.g_price,
        "g_phone": good.g_phone,
        "g_addr": good.g_addr,
        "g_collected": good.g_collected

    }
    return JsonResponse(data)


def add_good(request):
    user = request.user
    if request.method == "GET":
        if user.u_ispay:
            types = Type.objects.all()
            data = {
                "title": "添加商品",
                "types": types,
            }
            return render(request, 'forgood/add_good.html', data)
        else:
            return redirect(reverse("forgood:alipay"))
    elif request.method == 'POST':
        user.u_ispay = not user.u_ispay
        print(user.u_name)
        user.save()
        good = Good()
        good.g_name = request.POST.get("goodname")
        good.g_addr = request.POST.get("addr")
        good.g_phone = request.POST.get("phone")
        good.g_price = request.POST.get("price")
        good.g_img_one = request.FILES.get("icon1")
        good.g_img_two = request.FILES.get("icon2")
        good.g_des = request.POST.get("des")
        good.g_type_id = request.POST.get("ttype")
        good.save()
        return redirect(reverse("forgood:home"))


def alipay(request):
    # 构建支付的客户端  AlipayClient
    alipay_client = AliPay(
        appid=APP_ID,
        app_notify_url=None,  # 默认回调url
        app_private_key_string=APP_PRIVATE_KEY,
        alipay_public_key_string=ALIPAY_PUBLIC_KEY,  # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
        sign_type="RSA",  # RSA 或者 RSA2
        debug=False  # 默认False
    )
    # 使用Alipay进行支付请求的发起

    subject = "发布商品费用"

    # 电脑网站支付，需要跳转到https://openapi.alipay.com/gateway.do? + order_string
    order_string = alipay_client.api_alipay_trade_page_pay(
        out_trade_no=uuid4().hex,
        total_amount=1,
        subject=subject,
        return_url="http://www.fand.wang/forgood/changestate/",
        # notify_url="http://www.fand.wang"  # 可选, 不填则使用默认notify url
    )
    # 客户端操作

    return redirect("https://openapi.alipaydev.com/gateway.do?" + order_string)


def change_state(request):
    user = request.user
    user.u_ispay = True
    user.save()
    return redirect(reverse("forgood:addgood"))