from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from event.models import EventObject
# Create your views here.
from forms import SearchForm
import sys

def home_page(request):
    html = template_name="event1.html" 
    return render(request, html)

def all_events(request):
	return render_to_response('all_events.html',{'info_list': EventObject.objects.all()})


def search(request):
	reload(sys)  # Reload does the trick!
	sys.setdefaultencoding('UTF8')
	answerList=[]

	searchInput=str(request.GET.get('user_search'))
	#searchInput=unicode(tempsearchInput, "utf-8")
	allevents=EventObject.objects.all()
	print(type(allevents))

	for event in allevents:
		if searchInput in event.title:
			answerList.append(event)
		
		elif searchInput in event.description:
			answerList.append(event)
		
		elif searchInput in event.owner_name:
			answerList.append(event)
		
		elif searchInput in event.place:
			answerList.append(event)


	return render_to_response('all_events.html',{'info_list': answerList})


def search1(request):
	#search is executed when user clicks search button in /events 


	#getting user search query input
	searchInput=str(request.GET.get('user_search'))
	print(searchInput)
	#allevents hold all event objects in DB
	allevents=EventObject.objects.all()
	for event in allevents:
		if searchInput in event.title :
			#answerList.append(event)
			print(event.owner_name)
			html= """<html lang="en"><body><div class="col-md-4"> <h4><strong> %s </strong></h4>""" %event.title
			html=html+"""	</p> <img src=%s  class="img-rounded" alt="Cinque Terre" width="104" height="86"/></p> """ % event.photoUrl
			html=html+"""        <p> on %s</p>""" %event.start_time
			html=html+	'	<p>	%s</p>' % event.owner_name
			html=html+"""  <p><a class="btn btn-default" role="button">&raquo;</a></p> </div> </body></html>"""


	return HttpResponse(html)



