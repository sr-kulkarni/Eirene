from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
	context_dict = {'boldmessage': "This is the bold font from context"}
	return render(request,'app1/index.html',context_dict)
	#return HttpResponse("App1 says hey there world! Here's more <a href='/app1/about'>about</a> this.")
 
def about(request):
	context_dict = {'boldmessage': "Supremely Awesome!!"}
	return render(request,'app1/about.html',context_dict)
	#return HttpResponse("This is the about page. Do you wanna go back to the <a href='/app1/'>main page?</a>")