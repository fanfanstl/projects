import json
from django.http import HttpResponse
from django.conf import settings


def render_json(data, code):
    result = {
        "code":code,
        "data":data,
    }
    if settings.DEBUG:
        result_json = json.dumps(result, ensure_ascii=False, indent=4, sort_keys=True)
        return HttpResponse(result_json)
    result_json = json.dumps(result, ensure_ascii=False, separators=[':', ','])
    return HttpResponse(result_json)