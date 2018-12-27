from django.core.cache import cache
from django.shortcuts import render

from user.common.errors import OK, Fail
from user.helper import save_upload_file, upload_avatar_to_qiniu
from user.lib.sms import get_code, check_vcode
from user.lib.sms import send_msg
from user.lib.http import render_json
from user.models import User, Profile
from user.verify_form import ProfileForm


def get_vcode(request):
    '''获取验证码'''
    phonenum = request.GET.get('phonenum')
    vcode = get_code(6)
    res = send_msg(phonenum, vcode)
    cache.set('Vcode-%s' % phonenum, vcode, timeout=3600)
    return render_json(None, OK)


def login(request):
    phonenum = request.POST.get('phonenum')
    vcode = request.POST.get('vcode')
    if check_vcode(phonenum, vcode):
        user, created = User.objects.get_or_create(phonenum=phonenum)
        request.session['uid'] = user.id
        return render_json(user.to_dict(), OK)
    else:
        return render_json(None, Fail.code)


def profile_show(request):
    user = request.user
    return render_json(user.to_dict(), OK)


def profile_modify(request):
    uid = request.user.id
    form = ProfileForm(request.POST)
    if not form.is_valid():
        return render_json(form.errors, Fail.code)
    profile = form.save(commit=False)
    profile.id = uid
    profile.save()
    return render_json(profile.to_dict(), OK)


def profile_upload(request):
    '''上传个人形象'''
    avatar = request.FILES.get("avatar")
    filepath, filename = save_upload_file(request.user, avatar)
    print(filename, filepath)
    # upload_avatar_to_qiniu(request.user, filepath, filename)
    return render_json('success', OK)


