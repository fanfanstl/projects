from django.conf.urls import url
from user import apis


urlpatterns = [
    url(r"^vcode", apis.get_vcode),
    url(r"^login$", apis.login),
    url(r"^profile/show$", apis.profile_show),
    url(r"^profile/modify$", apis.profile_modify),
    url(r"^profile/upload$", apis.profile_upload),
]