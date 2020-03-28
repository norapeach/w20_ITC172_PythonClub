from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class (table) to track Meetings with fields (rows) for meeting_title, meeting_date, meeting_time
#   meeting_location, meeting_agenda
class Meeting(models.Model):
    meeting_title = models.CharField(max_length=255)
    meeting_date = models.DateField() 
    meeting_time = models.TimeField()
    meeting_location = models.CharField(max_length=255)
    meeting_agenda = models.TextField()
     
    # overrides function to return meeting_title value
    def __str__(self):
        return self.meeting_title
    
    # sets properties for how the class will appear in the database and ADMIN app
    class Meta:
        db_table = 'meeting'
        verbose_name_plural = 'meetings'

# MeetingMinutes tracks data relating to attedence (linked to User) and meeting minutes content, linked to meeting class by FK
class MeetingMinutes(models.Model):
    meeting = models.ForeignKey(Meeting, on_delete=models.DO_NOTHING) # record of meeting and related data will be kept here even if meeting is deleted
    attendance = models.ManyToManyField(User) # django resolves this with linking table - in DB: table meeting_minutes_attendance
    minutes_text = models.TextField()
    
    def __str__(self):
        return self.minutes_text
    
    class Meta:
        db_table = 'meeting_minutes'
        verbose_name_plural = 'meeting_minutes'

# Resources tracks resource data - name, type, url, date entered, user id who entered (FK with User) and description
class Resource(models.Model):
    resource_name = models.CharField(max_length=255)
    resource_type = models.CharField(max_length=255)
    resource_URL = models.URLField(null=True, blank=True)
    resource_date_entered = models.DateField()
    resource_added_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    resource_description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.resource_name
    
    class Meta:
        db_table = 'resource'
        verbose_name_plural = 'resources'

# Event tracks related data title, location, date, time, description and user id of member that posted
class Event(models.Model):
    event_title = models.CharField(max_length=255)
    event_location = models.CharField(max_length=255)
    event_date = models.DateField()
    event_time = models.TimeField()
    event_added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    event_description = models.TextField()
    
    def __str__(self):
        return self.event_title
    
    class Meta:
        db_table = 'event'
        verbose_name_plural = 'events'