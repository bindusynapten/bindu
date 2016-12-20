from django.conf.urls import include, url
from django.contrib import admin

from offapp.views import home, index, show, task

urlpatterns = [
    # Examples:
    # url(r'^$', 'official.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
     url(r'^home/$', home),
    url(r'^index/$', index),
    url(r'^show/$', show),
    url(r'^task/$',task),
]
