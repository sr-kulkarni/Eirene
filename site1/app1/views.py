from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
	return HttpResponse("App1 says hey there world! Here's more <a href='/app1/about'>about</a> this.")

def about(request):
	return HttpResponse("This is the about page. Do you wanna go back to the <a href='/app1/'>main page?</a>")