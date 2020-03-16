# w20_ITC172_PythonClub

## Project files for first Django project and app
Python Club site that acts as a hub for Python related study activities. Users can be added and they can add Python-related learning resources, events and meetings. 

### 3/15
Add login/logout functionality with links in base.html navbar. Users will be redirected to the template page if they click the add Meeting, add Resource and add Meeting Minutes links.  Move link to add new meeting form to meetings.html & link to add resource form to resource.html. 

### 3/04 
Refactor View getMeetingDetails() by adding try/except to check whether an instance of MeetingMinutes exists or not, which triggers a conditional statement in the template to display the url to the addMeetingMinutes template and Form View. Meeting minutes details can now be added once to each meeting, however the test MeetingMinutes_FormTest.test_minutesform_is_valid() is returning false.
   
### 2/27
Add forms to allow for users to create meetings and resource items that display on the respective Resources and Meetings pages.

### 2/23
Update test.py with test classes for each Model that check the str() return and table name as well as for each View. The View tests ensure that the name in the view URLconf pattern maps back to the correct View.

### 2/19
Add a display view for the Meetings model that lists each meeting with a link to a detail view for the each meetings' details. 

### 1/28
Add a display view for the Resource model with some sample resources. This page is linked in the nav bar. 

### 1/23 
Add 4 model classes for Meetings, Meeting Minutes, Resources and Events that are migrated to the Python Club database and are registered in the ADMIN app.

### 1/25 
Add landing page with first view via templates/club/index.html. 