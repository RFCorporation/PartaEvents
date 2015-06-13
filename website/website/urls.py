from django.conf.urls import include,url,patterns
from django.contrib import admin
from event.views import search, all_events
urlpatterns = patterns('',
     # url(r'^$', 'website.views.home', name='home'),
     url(r'^$', include('event.urls')),
     url(r'^events/',all_events),
     url(r'^admin/', include(admin.site.urls)),
     url(r'^search', search)
     
    )