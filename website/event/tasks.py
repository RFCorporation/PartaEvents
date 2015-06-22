from __future__ import absolute_import
from event.models import EventObject , Url
from celery.decorators import periodic_task
from celery.task.schedules import crontab
import requests

token ='CAAO7ZBEZBU2qcBAAiM7WuiUCsfOdOjlwgyDrfDncpib6DI1ZCoayFIWCBpmZB52ABcVwyxCkm3xFYLzT7MNdK8ZAZAPDbluugkd5MAiUGZBO09EUYKZAV6PHzDG4BtZAI1V8PJdFLYKYUreuMQoyZB3WEpTSnHuDtO48wdHr1YWiV10NKJ5MxcI2Cw7z4PUkxEzoAiUXdb14gPqeVBlzRLmAwhqnkVexOLnxMZD'


@periodic_task(run_every=(crontab(hour="*", minute="*", day_of_week="*")))
def checkNewevents():
	global token
	#retrieving data from data
	event_entries=list(EventObject.objects.all().values_list('eventsID', flat=True))
	event_entries=[int(x) for x in event_entries]
	#print(event_entries)

	page_entries=Url.objects.all()

	#event_entries is a list of all event IDs

	#checking each page for new events
	for page in page_entries:

		page_name=(page.url).rsplit('/',1)[1]
		print(page_name)
		requestGET='https://graph.facebook.com/v2.3/' + page_name +'?fields=events,category&access_token='+token
		r=requests.get(requestGET)
	
	#checking for URL validation
		if (r.status_code==404):

			print("Could not refresh events for page")

		elif(r.status_code==200):

			fileJson = (r.json())
			page_category=fileJson["category"]

			if 'events' in fileJson.keys():

				fileJson=fileJson["events"]["data"]


				for i in range(len(fileJson)):

					#if event doesnt already exist
					print(fileJson[i]['id'])
					if int(fileJson[i]['id']) not in event_entries:
						event_id=fileJson[i]['id']
						eventRequest = 'https://graph.facebook.com/v2.3/'+str(event_id)+'?fields=name,place,start_time,owner,cover,description'+'&access_token='+token
							
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
										
									Page_obj = EventObject(latitude=longlat_json["latitude"],longitude=longlat_json["longitude"],eventsID=event_id,title=event_name,description=json_event["description"],place = json_event["place"]["name"],start_time =json_event["start_time"],owner_name=json_event['owner']['name'],category = page_category, photoUrl=photo_url)
									print(longlat_json["latitude"])
								else:
									Page_obj = EventObject(eventsID=event_id,title=event_name,description=json_event["description"],place = json_event["place"]["name"],start_time =json_event["start_time"],owner_name=json_event['owner']['name'],category = page_category, photoUrl=json_event["cover"]["source"])
									#print json_event["name"]
								print('to swnw aderfe')
								Page_obj.save()




