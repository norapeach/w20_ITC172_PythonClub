from django.shortcuts import render, get_object_or_404
#import models from models.py
from .models import Meeting, MeetingMinutes, Resource, Event

# Create your views here:
# first view is a basic function that returns the rendered index.html page 
# when requested

# method to create a view named index that directs the request to the index.html webpage
def index (request):
    return render(request, 'Club/index.html')

# method to retrieve the Resource class data to display on webpage
def getResource(request):
    # context is a list to contain all the Resource data as a list of objects
    resource_list = Resource.objects.all()
    return render(request, 'club/resource.html', {'resource_list': resource_list})

# view to return all the meetings
def getMeetings(request):
    meeting_list = Meeting.objects.all()
    return render(request, 'Club/meetings.html', {'meeting_list': meeting_list})

def getMeetingDetails(request, id):
    meet = get_object_or_404(Meeting, pk=id)
    return render(request, 'Club/meetingdetail.html', {'meet': meet})

