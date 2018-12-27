from social.errors import NOT_MATCHING, LIKE
from social.models import Swiped
from user.lib.http import render_json
from user.models import User


def get_screening_cond(profile):
    max_age = profile.max_dating_age
    min_age = profile.min_dating_age
    sex = profile.dating_sex
    location = profile.location
    return {"max_age": max_age, "min_age": min_age, "sex": sex, "location": location, }


def get_match_users(cond):
    data = []
    users = User.objects.filter(location=cond['location']).filter(sex=cond['sex'])
    if not users:
        return render_json(None, NOT_MATCHING)
    for user in users:
        if (user.age > cond['min_age']) and (user.age < cond['max_age']):
            data.append(user.to_dict())


def create_swiped(request, swiper_type):
    cur_id = request.user.id
    uid = request.POST.get('uid')  # 被滑用户id
    user = Swiped()
    user.uid = cur_id
    user.sid = uid
    user.mark = swiper_type
    user.save()
    return user.to_dict()
