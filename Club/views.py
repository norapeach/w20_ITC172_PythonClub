from django.shortcuts import render, get_object_or_404
#import models from models.py
from .models import Meeting, MeetingMinutes, Resource, Event
from .forms import MeetingForm, MeetingMinutesForm, ResourceForm, EventForm
from django.contrib.auth.decorators import login_required

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

def getMeetingDetails(request, id): # could add an extended context to include meeting minutes
    meet = get_object_or_404(Meeting, pk=id)
    try: # like a clause for exceptions/errors for models
        meetingMinutes = MeetingMinutes.objects.get(meeting_id=id)
    except MeetingMinutes.DoesNotExist: # django exception 
        meetingMinutes = None
    details = {
        'meet': meet,
        'meetingMinutes': meetingMinutes,
    }
    return render(request, 'Club/meetingdetail.html', context=details)

def getEvent(request):
    event = Event.objects.all()
    return render(request, 'Club/event.html', {'event': event})

######### FORM VIEWS ##########
@login_required
def addMeeting(request):
    form = MeetingForm
    if request.method == 'POST':
        form = MeetingForm(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            post.save()
            form = MeetingForm() # after form values are saved, return to empty form
    else: 
        form = MeetingForm() # if not POST or is_valid() == false, django returns empty form
    return render(request, 'Club/addmeeting.html', {'form': form})

@login_required
def addMeetingMinutes(request):
    minutes_f = MeetingMinutesForm # reference to Meeting
    if request.method == 'POST':
        minutes_f = MeetingMinutesForm(request.POST)
        if minutes_f.is_valid():
            minutesPost = minutes_f.save(commit=True)
            minutesPost.save()
            minutes_f = MeetingMinutesForm() # was missing ()
    else:
        minutes_f = MeetingMinutesForm()
    return render(request, 'Club/addmeetingmins.html', {'minutes_f': minutes_f})

@login_required
def addResource(request):
    resource= ResourceForm
    if request.method == 'POST':
        resource=ResourceForm(request.POST)
        if resource.is_valid():
            resourcePost = resource.save(commit=True)
            resourcePost.save()
            resource=ResourceForm() # was missing ()
    else:
        resource=ResourceForm()
    return render(request, 'Club/addresource.html', {'resource': resource})


######## Log-in/log-out message Views ########
def loginmessage(request):
    return render(request, 'club/loginmessage.html')

def logoutmessage(request):
    return render(request, 'club/logoutmessage.html')


