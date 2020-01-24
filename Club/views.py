from django.shortcuts import render

# Create your views here:
# first view is a basic function that returns the rendered index.html page 
# when requested

# method to create a view named index that directs the request to the index.html webpage
#   
def index (request):
    return render(request, 'Club/index.html')

