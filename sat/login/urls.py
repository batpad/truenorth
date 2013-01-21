from django.conf.urls import patterns, include, url                           
from views import login_user


urlpatterns = patterns('',
    (r'^login/$', login_user),
)
