from django.conf.urls import patterns, include, url
from .views import *
urlpatterns = patterns('',

    url(r'^$',Index.as_view(),name="index"),
    url(r'^signup$',SignUpView.as_view(),name="signup"),
    url(r'^login$',LoginView.as_view(),name="login"),
    url(r'^logout$',LogOutView.as_view(),name="logout"),

)
