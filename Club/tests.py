from django.test import TestCase
from .models import Meeting, MeetingMinutes, Resource, Event
from .forms import MeetingForm, MeetingMinutesForm
from .views import addMeeting
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

####### FORM TESTS #######
class MeetingForm_Test(TestCase):
    def test_meetingform_is_valid(self):
        form = MeetingForm(data={'meeting_title': "test", 'meeting_date': "2020-02-27", 
                                 'meeting_time': "16:36", 'meeting_location': "Leipzig", 
                                 'meeting_agenda': "Die Zukunft planen."})
        self.assertTrue(form.is_valid())
    
    def test_meetingform_empty(self):
        form = MeetingForm(data={'meeting_title': "", 'meeting_date': "", 
                                 'meeting_time': "", 'meeting_location': "", 
                                 'meeting_agenda': ""})
        self.assertFalse(form.is_valid())

class MeetingMinutes_FormTest(TestCase):
    # method to instatialize user object and meeting to be passed to test for validation
    def setUp(self):
        self.user = User.objects.create(username='Katja')
        self.meeting = Meeting.objects.create(meeting_title='study group', meeting_date='2019-04-05', 
                       meeting_time='18:00', meeting_location='Tacoma', 
                       meeting_agenda='test')
    #### THIS TEST IS FAILING, NEEDS TO BE REFACTORED ####
    def test_minutesform_is_valid(self):
        form = MeetingMinutesForm(data={'meeting_id': self.meeting, 'attendance': self.user, 'minutes_text': 'test'}) 
        self.assertTrue(form.is_valid())

######### LOGIN TESTS #########
class New_meeting_authentication_test(TestCase):
    #setUp function gets user object, and creates test Meeting instance
    def setUp(self):
        self.test_user = User.objects.create_user(username='testuser1', 
                                              password='P@ssw0rd1')
        self.meeting = Meeting.objects.create(meeting_title='study group',
                                          meeting_date='2019-04-05', meeting_time='18:00', meeting_location='Tacoma',     meeting_agenda='test')
    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('addmeeting'))
         # below tests that not logged in client is redirected to login then to the add meeting page
        self.assertRedirects(response, '/accounts/login/?next=/Club/addMeeting/') 
        
    # logs in the test user instance & checks that user can access form
    # returns true if correct template is returned when form is accessed
    def test_logged_in_uses_correct_template(self):
        login = self.client.login(username ='testuser1', password='P@ssw0rd1')
        response = self.client.get(reverse('addmeeting'))
        self.assertEqual(str(response.context['user']), 'testuser1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Club/addmeeting.html')