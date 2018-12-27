import random
import requests
from django.core.cache import cache

from user.myconfig import ACCOUNT, PASSWORD, TEXT, HEADERS, URL
from worker import call_by_worker


def get_code(length):
    template = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    vcode = ''.join(random.choices(template, k=6))
    print(vcode)
    return vcode


# @call_by_worker
def send_msg(phonenum, code):
    text = TEXT % code
    data = {'account': ACCOUNT, 'password': PASSWORD, 'content': text, 'mobile': phonenum, 'format': 'json'}
    res = requests.post(url=URL, data=data, headers=HEADERS)
    return 1


def check_vcode(phonenum, vcode):
    code = cache.get('Vcode-%s' % phonenum)
    return vcode == code
