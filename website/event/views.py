from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from event.models import EventObject
# Create your views here.
from forms import SearchForm
import sys


#called when parta events button in homepage is clicked,
def all_events(request):
	category_List=[]
	allcategorys=EventObject.objects.all()
	for event in allcategorys:
		category_List.append(event.category)
	category_List = set(category_List)
	return render_to_response('all_events.html',{'info_list': EventObject.objects.all(),'cat_list':category_List})

#function called when event title/perissotera is clicked
def event_details(request,id):
	answerList=[]
	allevents=EventObject.objects.all()
	
	reload(sys)  # Reload does the trick!
	sys.setdefaultencoding('UTF8')
	for event in allevents:
		
		if int(id)==event.eventsID:
			answerList.append(event)
			print(id)
	#return render_to_response('event_info.html',{'event_list':answerList})
	return render_to_response('event_info.html',{'info_list':answerList})

#called when category in dropdown bar is clicked
def category_events(request,cat):
	answerList=[]
	category_List=[]
	allevents=EventObject.objects.all()
	for event in allevents:
		category_List.append(event.category)
		
		if str(cat)==event.category:
			answerList.append(event)
			print(cat)
	category_List = set(category_List)

	return render_to_response('all_events.html',{'info_list':answerList, 'cat_list':category_List})
	
def date(request):
	return render_to_response('datepicker.html')
	
#called when search button is clicked
def search(request):
	reload(sys)  # Reload does the trick!
	sys.setdefaultencoding('UTF8')
	answerList=[]
	category_List=[]

	searchInput=str(request.GET.get('user_search'))
	#searchInput=unicode(tempsearchInput, "utf-8")
	allevents=EventObject.objects.all()
	print(type(allevents))

	for event in allevents:

		category_List.append(event.category)

		if searchInput in event.title:
			answerList.append(event)
		
		elif searchInput in event.description:
			answerList.append(event)
		
		elif searchInput in event.owner_name:
			answerList.append(event)
		
		elif searchInput in event.place:
			answerList.append(event)

	category_List = set(category_List)

	return render_to_response('all_events.html',{'info_list': answerList, 'cat_list':category_List})




