from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from django.views.generic import TemplateView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sat.views.home', name='home'),
    url(r'login/', include('sat.login.urls')),
    # url(r'^sat/', include('sat.foo.urls')),
    url(r'^home/(?P<user_type>.*)$', 'sat.truenorth.views.home', name='home'),
    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('django.views.generic.simple', 
    url(r'^$', TemplateView.as_view(template_name='index.html')),
)