from django.contrib import admin
from event.models import EventObject, Url

# Register your models here.
admin.site.register(EventObject)
admin.site.register(Url)