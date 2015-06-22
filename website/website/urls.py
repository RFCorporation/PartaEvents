from django.conf.urls import include,url,patterns
from django.contrib import admin
from event.views import *
urlpatterns = patterns('',
     # url(r'^$', 'website.views.home', name='home'),
     url(r'^$', include('event.urls')),
     url(r'^events/',all_events),
     url(r'^admin/', include(admin.site.urls)),
     url(r'^search', search),
     url(r'^event/(?P<id>[0-9]+)',event_details),
	 url(r'^cat/(?P<cat>[A-Za-z/\s]+)/$',category_events),
	 url(r'^date/$',date),
	 url(r'^maps/$',maps),
     url(r'^datesearch/$', datesearch),
	 url(r'^rss/(?P<categ>[A-Za-z/,\s]+)/$',index),
	 url(r'^rss/$',all_events),
    )