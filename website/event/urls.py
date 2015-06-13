from django.conf.urls import patterns,include,url
from django.views.generic import ListView
from event.models import EventObject   


urlpatterns = patterns('',
            url(r'^',ListView.as_view(
				queryset=EventObject.objects.all().order_by("start_time")[:3],template_name="event.html")),
			      
	)
