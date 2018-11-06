from django.conf.urls import url

from movie_user.views.user_api import UsersView, UserView

urlpatterns = [
    url(r"^users/$",UsersView.as_view()),
    url(r"^user/(?P<pk>\d+)/$",UserView.as_view(),name="usermodel-detail"),
]