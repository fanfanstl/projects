from social.errors import OK, LIKE, SUPER_LIKE, DONT_LIKE
from social.logic import get_screening_cond, get_match_users, create_swiped
from user.lib.http import render_json
from user.models import Profile


def get_recommendation(request):
    uid = request.user.id
    profile = Profile.objects.get(id=uid)
    # 获取筛选条件
    cond = get_screening_cond(profile)
    data = get_match_users(cond)
    return render_json(data, OK)


def match(request):
    pass


def like(request):
    data = create_swiped(request, LIKE)
    return render_json(data, OK)


def super_like(request):
    data = create_swiped(request, SUPER_LIKE)
    return render_json(data, OK)


def dont_like(request):
    data = create_swiped(request, DONT_LIKE)
    return render_json(data, OK)


def goback(request):
    pass


def get_liked(request):
    pass


