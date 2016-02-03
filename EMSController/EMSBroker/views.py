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



def putService(servDict):
	c = consul.Consul()
	try:
		for item in servDict.items():
			c.agent.service.register(name=item[0],address=item[1])
	except:
		raise Exception("Some problem with Consul!")

def getService():
	c = consul.Consul()
	sDict = {}
	serviceList = c.agent.services()
	for item in serviceList.items():
		sDict[item[0]] = item[1]['Address']

	return sDict	






@api_view(['GET','POST'])
def service_list(request,format=None):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        #services = Service.objects.all()
        sDict = getService()
	services = []
	for item in sDict.items():
		#print item[0] + "address : " +item[1]
		tempService = Service(name=item[0],address=item[1])
		services.append(tempService)

	serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        #data = JSONParser().parse(request)
        serviceDict = {}
	serviceDict[request.data['name']]=request.data['address']
        
	putService(serviceDict)
	
	#if s1Serializer.is_valid():
	#    	 s1Serializer.save()
        return Response(serviceDict, status=status.HTTP_201_CREATED)
        #return Response(s1Serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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

