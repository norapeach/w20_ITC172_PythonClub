from django.urls import path
from . import views 

# within the app URLs file, each view needs it's path to be added 
#   that way it can be returned when the urls is called
# name="..." sets a 'nickname' for the view that can be used later instead of writing the entire path
#   the first parameter is blank as index is the default page rendered when "home" page of app is loaded
#   it would be a path with slashes for another file e.g. templates/club/file.html --> not sure if this is correct  
urlpatterns = [
    path('', views.index, name='index'),
    path('getResource/', views.getResource, name='resource'),
    path('getMeetings/', views.getMeetings, name='meetings'),
    path('getMeetingDetails/<int:id>', views.getMeetingDetails, name='meetingdetail'),
    path('getEvent/', views.getEvent, name='event'),
    path('addMeeting/', views.addMeeting, name='addmeeting'),
    path('addMeetingMinutes/', views.addMeetingMinutes, name='addmeetingmins'),
    path('addResource/', views.addResource, name='addresource'),
]