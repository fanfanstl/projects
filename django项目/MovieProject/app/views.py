from time import sleep

import requests
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt
from app.models import Carousel, Movie, User


# 测试
def hellow(request):
    return HttpResponse("hellow")


# 动态添加轮播图
def add_carousel(request):
    url = r"https://www.vmovier.com/apiv3/index/getBanner"
    res = requests.get(url=url)
    res = res.json().get("data")
    # 获取image的url
    for item in res:
        carousel = Carousel()
        carousel.c_url = item["image"]
        carousel.save()
    return HttpResponse("添加轮播图数据成功")


# 动态添加电影数据
def add_movies(request):
    for i in range(30):
        url = r"https://www.vmovier.com/apiv3/post/getPostInCate?cateid=0&p=%d" % i
        get_movies_data(url)
    return HttpResponse("添加电影数据成功")


# 爬取电影数据函数
def get_movies_data(url):
    data = requests.get(url=url)
    data = data.json().get("data")
    for item in data:
        movie = Movie()
        movie.m_postid = item.get("postid")
        movie.m_title = item.get("title")
        movie.m_duration = deal_time(item.get("duration"))
        movie.m_paa_fu_title = item.get("wx_small_app_title")
        movie.m_img = item.get("image")
        movie.m_more = "https://www.vmovier.com/%s?qingapp=app_new" % item.get("postid")
        movie.save()


# 处理时间函数
def deal_time(s):
    s = int(s)
    m, s = divmod(s, 60)
    h, m = divmod(m, 60)
    return "%d:%02d:%02d" % (h, m, s)


# 展示主页面
# def home(request):
#     # 轮播图加载
#     carousels = Carousel.objects.all()
#     movies  = Movie.objects.all()[0:10]
#     for item in movies:
#         count = item.m_user.all().count()
#         print(count)
#         item.count = count
#     # print(movies.first().m_img)
#     return render(request,'home.html',context=locals())


#展示主页面
def home(request):
    # 轮播图加载
    carousels = Carousel.objects.all()
    movies = Movie.objects.all()
    page_num = request.GET.get("page",1)
    per_page = request.GET.get("per_page",20)
    paginator = Paginator(movies,per_page=per_page)
    page = paginator.page(page_num)
    all = paginator.num_pages
    if all > 10:
        per = range(1,6)
        last = range(all-4,all+1)
        data = {
            "carousels": carousels,
            "per":per,
            "last":last,
            "page": page
        }
    else:
        data = {
            "carousels":carousels,
            "all_page":paginator.page_range,
            "page":page
        }
    print(paginator.num_pages)
    return render(request, 'home.html', context=data)


# 注册页面呈现及注册
def register(request):
    if request.method == "GET":
        return render(request,'register.html')
    elif request.method == "POST":
        u_name = request.POST.get("username")
        u_passwd = request.POST.get("passwd")
        u_email = request.POST.get("email")
        u_icon = request.FILES.get("img")
        user = User.objects.filter(Q(u_name=u_name) | Q(u_email=u_email)).first()
        if user:
            # 用户已存在
            print(user)
            return render(request, 'register.html')
        else:
            # 用户不存在
            user = User()
            user.u_name, user.u_passwd, user.u_email, user.u_icon = u_name, u_passwd, u_email, u_icon
            user.save()
            return render(request,'login.html')


# 登录页面呈现及登录
def login(request):
    if request.method == "GET":
        return render(request,'login.html')
    elif request.method == "POST":
        u_name = request.POST.get("username")
        u_passwd = request.POST.get("passwd")
        users = User.objects.filter(u_name=u_name).filter(u_passwd=u_passwd)
        if users.exists():
            # 用户存在
            user = users.first()
            carousels = Carousel.objects.all()
            movies = Movie.objects.all()[0:10]
            for item in movies:
                count = item.m_user.all().count()
                item.count = count
            content = {
                "username":user.u_name,
                "icon":"/static/upload/" + user.u_icon.url,
                "carousels":carousels,
                "movies":movies
            }
            request.session["u_id"] = user.id
            return render(request,'home_logined.html',context=content)
        else:
            # 用户不存在
            return render(request,'login.html')



# 个人信息展示及修改
def self_info(request):
    if request.method == "GET":
        user_id = request.session.get("u_id")
        if user_id:
            user = User.objects.get(pk=user_id)
            context = {
                "username":user.u_name,
                "icon":"/static/upload/" + user.u_icon.url
            }
            return render(request,'userinfo_mod.html',context=context)
        else:
            return render(request,'login.html')
    elif request.method == "POST":
        u_emial = request.POST.get("email")
        u_id = request.session.get("u_id")
        if User.objects.get(pk=u_id).u_email == u_emial:
            u_icon = request.FILES.get("icon")
            user = User.objects.get(pk=u_id)
            user.u_icon = u_icon
            user.save()
            return redirect(reverse('app:myflush'))
        else:
            return HttpResponse("旧邮箱输入错误")


#刷新当前页面
def myflush(request):
    u_id = request.session.get("u_id")
    user = User.objects.get(pk=u_id)
    carousels = Carousel.objects.all()
    movies = Movie.objects.all()[0:10]
    content = {
        "username": user.u_name,
        "icon": "/static/upload/" + user.u_icon.url,
        "carousels": carousels,
        "movies": movies
    }
    return render(request, 'home_logined.html', context=content)


# 收藏和取消收藏
@csrf_exempt
def collect(request):
    u_id = request.session.get("u_id")
    m_postid = request.POST.get("postid")
    if u_id:
        if request.POST.get("flag") == "cancel":
            # 取消收藏
            user = User.objects.get(pk=u_id)
            movie = Movie.objects.get(m_postid=m_postid)
            user.movie_set.remove(movie)
            return JsonResponse({"flag1": "ok"})
        elif request.POST.get("flag") == "add":
            # 收藏
            user = User.objects.get(pk=u_id)
            movie = Movie.objects.get(m_postid=m_postid)
            user.movie_set.add(movie)
            return JsonResponse({"flag":"ok"})
    else:
        return render(request,'login.html')


# 个人收藏
def self_collect(request):
    u_id = request.session.get("u_id")
    if u_id:
        # 已登录
        user = User.objects.get(pk=u_id)
        carousels = Carousel.objects.all()
        # movies = Movie.objects.all()[0:10]
        movies = user.movie_set.all()[0:10]
        # 计算收藏量
        for item in movies:
            count = item.m_user.all().count()
            print(count)
            item.count = count
        content = {
            "username": user.u_name,
            "icon": "/static/upload/" + user.u_icon.url,
            "carousels": carousels,
            "movies": movies
        }
        return render(request,'home_logined_collected.html',context=content)
    else:
        # 未登录
        return render(request,"login.html")


@cache_page(20,cache="redis")
def mycache(request):
    sleep(3)
    content = []
    for i in range(10):
        content.append("tom%d" % i)
    data = {
        "content":content
    }
    return render(request,'cache.html',context=data)