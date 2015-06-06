from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
#from django.core.signals import Page_save
import facebook, json
import requests, sys
import sqlite3
import codecs
from django.dispatch import receiver


global token
token ='CAAO7ZBEZBU2qcBAAiM7WuiUCsfOdOjlwgyDrfDncpib6DI1ZCoayFIWCBpmZB52ABcVwyxCkm3xFYLzT7MNdK8ZAZAPDbluugkd5MAiUGZBO09EUYKZAV6PHzDG4BtZAI1V8PJdFLYKYUreuMQoyZB3WEpTSnHuDtO48wdHr1YWiV10NKJ5MxcI2Cw7z4PUkxEzoAiUXdb14gPqeVBlzRLmAwhqnkVexOLnxMZD'

# Create your models here.

#reload(sys)  # Reload does the trick!
#sys.setdefaultencoding('UTF8')

class EventObject(models.Model):
	title = models.CharField(max_length = 300 , default='')
	start_time = models.DateTimeField('date', blank=True , null=True )
	owner_name=models.CharField(max_length=200 ,  default='')	
	place=models.CharField(max_length=200 , default='')
	category=models.CharField(max_length=200 , default='')
	photoUrl = models.URLField(max_length=500, default='')

	def __unicode__(self):
		return self.title

class Url(models.Model):
	url = models.CharField(max_length = 200,default='')
	
	def __unicode__(self):
		return self.url


	#adding extra argument to signal
	def save(self,*args, **kwargs):
		super(Url, self).save(*args, **kwargs)
		#self.page_name=self.url




@receiver(post_save, sender=Url)
def insertPage(sender, instance, *args, **kwargs):
	page_name = instance.url
	global token

	#construct link for request
	requestGET='https://graph.facebook.com/v2.3/' + page_name +'?fields=events,category&access_token='+token
	 #make request
	r=requests.get(requestGET)
	
	#checking for URL validation
	if (r.status_code==404):
		print("URL not valid")
		#ctypes.windll.user32.MessageBoxA(0, "URL not valid .", "404 error", 1)
		Url.objects.latest('id').delete()
	elif(r.status_code==200):
		print("URL is Valid, proceeding...")
		fileJson = (r.json())
		#keep data that are useful
		page_category=fileJson["category"]
		fileJson=fileJson["events"]["data"]
		
		
		#creating list with events ids
		for i in range(len(fileJson)):
			eventsID= fileJson[i]["id"]
			eventRequest='https://graph.facebook.com/v2.3/'+eventsID+'?fields=name,place,start_time,owner,picture'+'&access_token='+token
			#eventAnswer is a json file with the required values: name etc
			eventAnswer=requests.get(eventRequest)
			json_event = eventAnswer.json()
			event_name =  json_event["name"]
			photo_url = json_event["picture"]["data"]["url"]
			

			Page_obj = EventObject(title=event_name,place = json_event["place"]["name"],start_time =json_event["start_time"],owner_name=json_event['owner']['name'],category = page_category, photoUrl=photo_url)
			print json_event["name"]
			Page_obj.save()
			#print(jsona['name'])
			#print(eventAnswer.text)



