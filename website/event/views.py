from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from event.models import EventObject
from forms import SearchForm
from operator import attrgetter
from django.contrib import messages
from django.utils import feedgenerator

import re
import sys,datetime,pytz,os
import PyRSS2Gen

# Create your views here.


#called when "par'ta events" button in homepage is clicked,
def all_events(request):
	category_List=[]
	event_list=EventObject.objects.all().order_by("start_time")

	for event in event_list:
		category_List.append(event.category)
		print(event.start_time)

	#keep only unique items/no double entries
	category_List = set(category_List)
	
	return render_to_response('all_events.html',{'info_list': event_list,'cat_list':category_List})

#called when event title/perissotera button is clicked
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
#returns events that belong to selected category
def category_events(request,cat):
	answerList=[]
	category_List=[]
	allevents=EventObject.objects.all().order_by("start_time")
	for event in allevents:
		category_List.append(event.category)
		
		if str(cat)==event.category:
			answerList.append(event)
			print(cat)
	category_List = set(category_List)

	return render_to_response('all_events.html',{'info_list':answerList, 'cat_list':category_List})


#function called when user searches trough datepicker
#returns all events in time 
def datesearch(request):
	answerList=[]
	allevents=EventObject.objects.all().order_by("start_time")
	#getting data from form submitted
	start_date=str(request.GET.get('startDate')).split('/')
	end_date=str(request.GET.get('endDate')).split('/')

	#if user doesnt enter end_date return all events in [start,+oo]
	if end_date[0]=='' and start_date[0]!='':
		
		start_date=datetime.datetime(int(start_date[2]),int(start_date[0]),int(start_date[1]),0,0,0,0).replace(tzinfo=pytz.UTC)

		for event in allevents:
			event.start_time=event.start_time.replace(hour=0,minute=0,tzinfo=pytz.UTC)
			if event.start_time>= start_date:
				answerList.append(event)

	#if user doesnt enter start_date return all events in [-oo,end_date]		
	elif start_date[0]=='' and end_date[0]!='':

		end_date=datetime.datetime(int(end_date[2]),int(end_date[0]),int(end_date[1]),0,0,0,0).replace(tzinfo=pytz.UTC)

		for event in allevents:
			event.start_time = event.start_time.replace(hour=0,minute=0,tzinfo=pytz.UTC)
			if event.start_time <= end_date:
				answerList.append(event)

	#if user entered both dates return events in [start_date,end_date]
	elif start_date[0]!='' and end_date[0]!='':
		#morfing of data
		start_date=datetime.datetime(int(start_date[2]),int(start_date[0]),int(start_date[1]),0,0,0,0).replace(tzinfo=pytz.UTC)
		end_date=datetime.datetime(int(end_date[2]),int(end_date[0]),int(end_date[1]),0,0,0,0).replace(tzinfo=pytz.UTC)

		#checkinf if end date is after start date
		if end_date >= start_date:
			

			for event in allevents:
				event.start_time=event.start_time.replace(hour=0,minute=0,tzinfo=pytz.UTC)
				#print(event.start_time, end_date)

				if event.start_time>= start_date and event.start_time<= end_date:
					answerList.append(event)
	else:
		answerList=allevents

	
	return render_to_response('all_events.html',{'info_list':answerList})
	
def date(request):
	return render_to_response('datepicker.html')
	
def maps(request):
	return render_to_response('maps.html')
	
#called when search button is clicked
def search(request):
	reload(sys)  # Reload does the trick!
	sys.setdefaultencoding('UTF8')
	answerList=[]
	category_List=[]

	searchInput=str(request.GET.get('user_search'))
	#searchInput=unicode(tempsearchInput, "utf-8")
	allevents=EventObject.objects.all()

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
	

def index(request,categ):
	path = os.path.dirname(os.path.abspath(__file__))
	path = path + "/static/rss/events.xml"
	categoy_list=str(categ).split(',')
	print(categoy_list)
	reload(sys)  # Reload does the trick!
	sys.setdefaultencoding('UTF8')
	allevents=EventObject.objects.all()
	item1=[]
	for event in allevents:
		item1.append(PyRSS2Gen.RSSItem(
				title = event.title,
				link = "http://127.0.0.1:8000/event/"+str(event.eventsID),
				description = event.description,
				guid = PyRSS2Gen.Guid("http://127.0.0.1:8000/event/"+str(event.eventsID)),
				#pubDate = datetime.datetime(2003, 9, 6, 21, 31))
				))	
	
	
	rss = PyRSS2Gen.RSS2(
	title = "PartaEvent's feed",
	link = "http://127.0.0.1:8000",
	description = "The latest news about Patra's Events .",
	items = item1)
				
	
		
	rss.write_xml(open(path, "w"))
	

	return render(request, 'index.html')



