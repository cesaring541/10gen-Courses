from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import *


handler404 = error404

handler500 = error500


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DjangoBlog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^',include("Blog.urls")),
    url(r'^admin/', include(admin.site.urls)),
)


