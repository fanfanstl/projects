from django.contrib.auth.hashers import make_password, check_password
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

from django.urls import reverse

from forclass.forclass_const import USERNAME_EXIST, USERNAME_OK, PHONE_EXIST, PHONE_OK
from forclass.models import User
from forgood.models import Type, Good


def hellow(request):
    return render(request, 'base.html')


def register(request):
    if request.method == "GET":
        data = {
            "title": "注册",
        }
        return render(request, 'usermanagement/register.html', data)
    elif request.method == "POST":
        username = request.POST.get("username")
        phone = request.POST.get("phone")
        passwd = request.POST.get("passwd")
        print(passwd,"============")
        icon = request.FILES.get("icon")
        user = User()
        user.u_name = username
        user.u_phone = phone
        passwd = make_password(passwd)
        user.u_passwd = passwd
        user.u_icon = icon
        user.save()
    return render(request, 'usermanagement/login.html')


def check_username(request):
    # 判断用户名是否可用
    username = request.GET.get("user_name")
    user = User.objects.filter(u_name=username)
    if user.exists():
        data = {
            "code": USERNAME_EXIST,
            "msg": "username exist"
        }
    else:
        data = {
            "code": USERNAME_OK,
            "msg": "username can use",
        }
    return JsonResponse(data)


def check_phone(request):
    phone = request.GET.get("phone")
    user = User.objects.filter(u_phone=phone)
    if user.exists():
        data = {
            "code": PHONE_EXIST,
            "msg": "phone exist"
        }
    else:
        data = {
            "code": PHONE_OK,
            "msg": "phone can use",
        }
    return JsonResponse(data)


def login(request):
    if request.method == "GET":
        data = {
            "title": "登录",
        }
        return render(request, 'usermanagement/login.html', context=data)
    elif request.method == "POST":
        username = request.POST.get("username")
        passwd = request.POST.get("passwd")
        users = User.objects.filter(Q(u_name=username) | Q(u_phone=username))
        if users.exists():
            user = users.first()
            if check_password(passwd,user.u_passwd):
                # 密码验证通过
                request.session["username"] = user.u_name
                return redirect(reverse("forgood:home"))
        return render(request, "usermanagement/login.html", context={"title": "登录", "error_info":"用户名或密码错误"})


def logout(request):
    request.session.flush()
    return redirect(reverse("forgood:home"))