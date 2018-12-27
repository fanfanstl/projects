from django.conf.urls import url

from social import apis

urlpatterns = [
    url(r'^recommendation', apis.get_recommendation),
    url(r'^matching', apis.match),
    url(r'^like', apis.like),
    url(r'^superlike', apis.super_like),
    url(r'^dontlike', apis.dont_like),
    url(r'^goback', apis.goback),
    url(r'^getliked', apis.get_liked),

]