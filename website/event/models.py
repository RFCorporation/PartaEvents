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
global API_KEY
token ='CAAO7ZBEZBU2qcBAAiM7WuiUCsfOdOjlwgyDrfDncpib6DI1ZCoayFIWCBpmZB52ABcVwyxCkm3xFYLzT7MNdK8ZAZAPDbluugkd5MAiUGZBO09EUYKZAV6PHzDG4BtZAI1V8PJdFLYKYUreuMQoyZB3WEpTSnHuDtO48wdHr1YWiV10NKJ5MxcI2Cw7z4PUkxEzoAiUXdb14gPqeVBlzRLmAwhqnkVexOLnxMZD'
API_KEY='AIzaSyCU6FjOMEiGHpolpYDmEJV6pTE27f7J5uA'
# Create your models here.

reload(sys)  # Reload does the trick!
sys.setdefaultencoding('UTF8')

class EventObject(models.Model):
	eventsID=models.IntegerField(default=0)
	title = models.CharField(max_length = 300 , default='')
	description=models.CharField(max_length=2000, default='')
	start_time = models.DateTimeField('date', blank=True , null=True )
	owner_name=models.CharField(max_length=200 ,  default='')	
	place=models.CharField(max_length=200 , default='')
	category=models.CharField(max_length=200 , default='')
	photoUrl = models.URLField(max_length=500, default='')
	longitude = models.FloatField(default=0.0)
	latitude =  models.FloatField(default=0.0)
	
	def __unicode__(self):
		return self.title

class Url(models.Model):
	url = models.CharField(max_length = 200,default='')
	
	def __unicode__(self):
		return self.url


	#adding extra argument to signal
	def save(self,*args, **kwargs):
		super(Url, self).save(*args, **kwargs)
		self.page_name=self.url




@receiver(post_save, sender=Url)
def insertPage(sender, instance, *args, **kwargs):
	#page_name holds the url admin entered
	page_name = instance.url
	
	#insert comment here
	page_name=page_name.rsplit('/',1)[1]
	 
	global token

	#needed for pages with non english characters
	reload(sys)
	sys.setdefaultencoding('UTF8')

	#flag is True if page already exists in database
	flag=False
    
	#construct link for request
	requestGET='https://graph.facebook.com/v2.3/' + page_name +'?fields=events,category&access_token='+token
	 #make request
	r=requests.get(requestGET)
	
	#checking for URL validation
	if (r.status_code==404):
		print("URL not valid")
		Url.objects.latest('id').delete()

	elif(r.status_code==200):
		print("URL is Valid, proceeding...")
		fileJson = (r.json())
		allpages=list(Url.objects.all())
		allpages.pop()
		#checking if page already exists in database, then flag=True
		for page in allpages:
			if page_name==page.url:
				flag=True
				print('page already exists')

				#delete page that already exists
				Url.objects.latest('id').delete()

		#if page does not already exist in database
		if flag==False:
			#keep data that are useful
			page_category=fileJson["category"]

			#checking if page has any eventss
			if 'events' in fileJson.keys():
					fileJson=fileJson["events"]["data"]
						
						
					#creating list with event ids
					for i in range(len(fileJson)):
						eventsID= fileJson[i]["id"]
						
						eventRequest = 'https://graph.facebook.com/v2.3/'+eventsID+'?fields=name,place,start_time,owner,cover,description'+'&access_token='+token
						#eventAnswer is a json file with the required values: name etc
						eventAnswer=requests.get(eventRequest)
						json_event = eventAnswer.json()
						if 'name' in json_event.keys():
							event_name =  json_event["name"]
							
							#checking if all values exist
							if 'place' and 'start_time' and 'owner'  in json_event.keys():
								photo_url = json_event["cover"]["source"]
								if 'location' in  json_event['place']:
									longlat_json = json_event["place"]["location"]
									
								else:
									longlat_json = json_event["place"]
									
									
								if 'longitude' and 'latitude' in longlat_json.keys():
									
									Page_obj = EventObject(latitude=longlat_json["latitude"],longitude=longlat_json["longitude"],eventsID=eventsID,title=event_name,description=json_event["description"],place = json_event["place"]["name"],start_time =json_event["start_time"],owner_name=json_event['owner']['name'],category = page_category, photoUrl=photo_url)
									print(longlat_json["latitude"])
								else:
									Page_obj = EventObject(eventsID=eventsID,title=event_name,description=json_event["description"],place = json_event["place"]["name"],start_time =json_event["start_time"],owner_name=json_event['owner']['name'],category = page_category, photoUrl=photo_url)
								#print json_event["name"]
								Page_obj.save()
			else:
				print('This page has no events')




