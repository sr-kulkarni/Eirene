from django.shortcuts import render

# Create your views here.

#from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
#from rest_framework.parsers import JSONParser

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from EMSBroker.models import ServiceHelper,Service
from EMSBroker.serializers import ServiceHelperSerializer, ServiceSerializer

import consul 

@api_view(['GET','POST'])
def service_list(request,format=None):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        services = Service.objects.all()
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        #data = JSONParser().parse(request)
        serviceDict = {}
	shDict = {}

	name = request.data['name']
	address = request.data['address']
	serviceDict['name'] = name
	serviceDict['address'] = address
	s1 = Service(name=name, address=address)
	s1Serializer = ServiceSerializer(data=serviceDict)
        
	if s1Serializer.is_valid():
	    	 s1Serializer.save()
		 return Response(s1Serializer.data, status=status.HTTP_201_CREATED)
        return Response(s1Serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#Some work required here
@api_view(['GET','PUT','DELETE'])
def service_detail(request,pk,format=None):
    """
    Retrieve, update or delete a service
    """
    try:
	#print name
        service = Service.objects.get(pk=pk)
    except Service.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ServiceSerializer(service)
        return Response(serializer.data)
    #Some changes required Here. 
    elif request.method == 'PUT':
        #data = JSONParser().parse(request)
        serializer = ServiceHelperSerializer(service, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        service.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

