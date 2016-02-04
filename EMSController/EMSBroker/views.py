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
from EMSBroker.plugins import ConsulPlugin







@api_view(['GET','POST'])
def service_list(request,format=None):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        plugin = ConsulPlugin()
	sDict = plugin.getService()
	if any(sDict):
		services = []
		for item in sDict.items():
			#print item[0] + "address : " +item[1]
			tempService = Service(name=item[0],address=item[1])
			services.append(tempService)
	
		serializer = ServiceSerializer(services, many=True)
        	return Response(serializer.data)
	else: return Response(status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'POST':
        serviceDict = {}
	serviceDict[request.data['name']]=request.data['address']
	plugin = ConsulPlugin()        
	plugin.putService(serviceDict)
	return Response(serviceDict, status=status.HTTP_201_CREATED)
       


#Some work required here
@api_view(['GET','PUT','DELETE'])
def service_detail(request,pk,format=None):
    """
    Retrieve, update or delete a service
    """
    #print pk
    
    try:
	plugin = ConsulPlugin()
        service = plugin.getServiceDetails(name=pk)
	#print service
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        tempService = Service(name=pk,address=service[pk])
	serializer = ServiceSerializer(tempService)
        return Response(serializer.data)
    #Some changes required Here. Update changes pending 
    elif request.method == 'PUT':
        #data = JSONParser().parse(request)
        serializer = ServiceHelperSerializer(service, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        plugin.deleteService(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)
   
