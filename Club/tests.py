from django.test import TestCase
from .models import Meeting, MeetingMinutes, Resource, Event
from django.urls import reverse
from django.contrib.auth.models import User

class MeetingTest(TestCase):
    # test if running str() will return meeting_title value
    def test_string(self):
        meet = Meeting(meeting_title='study group', meeting_date='2019-04-05', 
                       meeting_time='18:00', meeting_location='Seatte', 
                       meeting_agenda='test')
        self.assertEqual(str(meet), meet.meeting_title)
        
    def test_table(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')

class MeetingMinutesTest(TestCase):
    def test_string(self):
        mintext = MeetingMinutes(minutes_text = "test test test")
        self.assertEqual(str(mintext), mintext.minutes_text)
        
    def test_table(self):
        self.assertEqual(str(MeetingMinutes._meta.db_table), 'meeting_minutes')

class ResourceTest(TestCase):
    def test_string(self):
        res = Resource(resource_name = "DjangoGirls")
        self.assertEqual(str(res), res.resource_name)
    
    def test_table(self):
        self.assertEqual(str(Resource._meta.db_table), 'resource')

class EventTest(TestCase):
    def test_string(self):
        ev = Event(event_title = "Midterm")
        self.assertEqual(str(ev), ev.event_title)
    
    def test_table(self):
        self.assertEqual(str(Event._meta.db_table), 'event')

####### BASIC VIEW TESTS ######
class IndexTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

class GetResourceTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('resource'))
        self.assertEqual(response.status_code, 200)

class GetMeetingsTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('meetings'))
        self.assertEqual(response.status_code, 200)

####### DETAIL VIEW TEST #######
class GetMeetingDetailTest(TestCase):
    # create sample data to generate meeting object with id
    def setUp(self):
        self.meet = Meeting.objects.create(meeting_title='study group', meeting_date='2019-04-05', 
                       meeting_time='18:00', meeting_location='Seatte', 
                       meeting_agenda='test')
    # test if getMeetingDetails view can be located by name
    # and passing sample data pk id as argument
    def test_meeting_detail_succes(self):
        response = self.client.get(reverse('meetingdetail', args=(self.meet.id,)))
        # assert that self.post is actually returned by the post_detail view
        self.assertEqual(response.status_code, 200)