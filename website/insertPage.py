import facebook, json
import requests, sys
import sqlite3
from django.dispatch import receiver
#from django.db.models.signals import post_save
from django.core.signals import post_save
from django.dispatch import receiver
from event.models import AddUrl

token ='CAAO7ZBEZBU2qcBAAiM7WuiUCsfOdOjlwgyDrfDncpib6DI1ZCoayFIWCBpmZB52ABcVwyxCkm3xFYLzT7MNdK8ZAZAPDbluugkd5MAiUGZBO09EUYKZAV6PHzDG4BtZAI1V8PJdFLYKYUreuMQoyZB3WEpTSnHuDtO48wdHr1YWiV10NKJ5MxcI2Cw7z4PUkxEzoAiUXdb14gPqeVBlzRLmAwhqnkVexOLnxMZD'


@receiver(post_save, sender=AddUrl)
def insertPage(sender, instance, *args, **kwargs):

    page_name = instance.page_name
	global token

	#construct link for request
	requestGET='https://graph.facebook.com/v2.3/' + page_name +'?fields=events&access_token='+token
	
	 #make request
	r=requests.get(requestGET)
	
	#checking for URL calidation
	if (r.status_code==404):
		print("URL not valid")
		
	elif(r.status_code==200):
		print("URL is Valid, proceeding...")

	fileJson = (r.json())

	#keep data that are useful
	fileJson=fileJson["events"]["data"]

	#creating list with events ids
	for i in range(len(fileJson)):
		eventsID= fileJson[i]["id"]
		eventRequest='https://graph.facebook.com/v2.3/'+eventsID+'?fields=name,place,start_time,owner'+'&access_token='+token
		#eventAnswer is a json file with the required values: name etc
		eventAnswer=requests.get(eventRequest)
		print(eventAnswer.text)




def insertEvent(title, start_time, place, owner_name, category):
	#need to figure out relative path to db file
	conn = sqlite3.connect('./db.sqlite3')
	insert = 'INSERT INTO table_name (title, star_time, place, onwer_name, category) VALUES (%s, ?, %s, %s, %s);'
	data = (title, star_time, place, onwer_name, category)
	con.execute(insert,data)