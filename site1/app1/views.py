from django.shortcuts import render
from django.http import HttpResponse
from app1.models import Category


# Create your views here.
def index(request):
	category_list = Category.objects.order_by('likes')[:5]
	context_dict = {'categories': category_list}
	return render(request,'app1/index.html',context_dict)
	#return HttpResponse("App1 says hey there world! Here's more <a href='/app1/about'>about</a> this.")
 
def about(request):
	context_dict = {'boldmessage': "Supremely Awesome!!"}
	return render(request,'app1/about.html',context_dict)
	#return HttpResponse("This is the about page. Do you wanna go back to the <a href='/app1/'>main page?</a>")