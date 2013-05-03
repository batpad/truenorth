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
    url(r'logout/', 'sat.login.views.logout_user'),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
# These are the URLs for truenorth core

urlpatterns += patterns('sat.truenorth.views', 
    # url(r'^$', TemplateView.as_view(template_name='login.html')),
    #  url(r'^base/$', TemplateView.as_view(template_name='base.html')),
     url(r'^staff/$', 'viewstafflist'),
     url(r'^selectcenter/$', 'selectcenter'),    
     url(r'^menu/$', 'menu'),    
     url(r'^students/$', 'viewstudentlist'),    
     url(r'^tutors/$', 'viewtutorlist'), 
     url(r'^student/add/$', 'add_student'),                       
     url(r'^staff/add/$', 'add_staff'),
     url(r'^tutor/add/$', 'add_tutor'),
     url(r'^student/edit/(?P<iden>\d+)/$', 'edit_student'),                       
     url(r'^tutor/edit/(?P<iden>\d+)/$', 'edit_tutor'),                       


       
)



