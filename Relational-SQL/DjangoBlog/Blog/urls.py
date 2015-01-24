from django.conf.urls import patterns, include, url
from .views import *
urlpatterns = patterns('',

    url(r'^$',IndexView.as_view(),name="index"),
    url(r'^welcome$',WelComeView.as_view(),name="welcome"),
    url(r'^signup$',SignUpView.as_view(),name="signup"),
    url(r'^login$',LoginView.as_view(),name="login"),
    url(r'^logout$',LogOutView.as_view(),name="logout"),
    url(r'^newpost$',PostView.as_view(),name="newpost"),
    url(r'^post/(?P<permalink>[\w\s]+)$',CommentView.as_view(),name="add_comment"),

)
