from django.conf.urls import url

from app.views import UsersApi, UserApi, BlocksApi

urlpatterns = [
    url(r"^users/$",UsersApi.as_view()),
    url(r"^users/(?P<uid>\d+)/$",UserApi.as_view()),
    url(r"^blocks/$",BlocksApi.as_view()),
]