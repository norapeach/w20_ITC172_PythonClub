from django.contrib import admin
from .models import Meeting, MeetingMinutes, Resource, Event #imports the newly created models in models.py

# Register your models here.
admin.site.register(Meeting)
admin.site.register(MeetingMinutes)
admin.site.register(Resource)
admin.site.register(Event)