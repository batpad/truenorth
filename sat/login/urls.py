from django.conf.urls import patterns, include, url                           
from views import login_user,logout_user


urlpatterns = patterns('',
url(r'^login/password/reset/$', 
        'django.contrib.auth.views.password_reset', 
        {'post_reset_redirect' : '/user/password/reset/done/'},
        name="password_reset"),
    (r'^login/password/reset/done/$',
        'django.contrib.auth.views.password_reset_done'),
    (r'^login/password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 
        'django.contrib.auth.views.password_reset_confirm', 
        {'post_reset_redirect' : '/user/password/done/'}),
    (r'^login/password/done/$', 
        'django.contrib.auth.views.password_reset_complete'),
    (r'^$', login_user),


)
