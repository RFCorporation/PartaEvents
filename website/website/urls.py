from django.conf.urls import include,url,patterns
from django.contrib import admin
from event.views import home_page
urlpatterns = patterns('',
     # url(r'^$', 'website.views.home', name='home'),
     url(r'^$', include('event.urls')),
     url(r'^events/$',home_page),
     url(r'^admin/', include(admin.site.urls)),
    )