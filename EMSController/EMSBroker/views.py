from django.shortcuts import render
# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from EMSBroker.models import Service
from EMSBroker.serializers import ServiceSerializer
from EMSBroker.plugins import ConsulPlugin
import os
import ConfigParser


#onsulPlugin shouldbe defined in a conf file. No explicit imports


@api_view(['GET','POST'])
def service_list(request,format=None):
    """
    List all services, or create a new service.
    """
    if request.method == 'GET':
        pluginFile = os.getcwd()
	#print pluginFile	
	pluginFile += '/config/plugins.conf'
	#print pluginFile
	config = ConfigParser.ConfigParser()
	config.read(pluginFile)
	print config.get('services','plugin')
	
	
	plugin = ConsulPlugin()
	sDict = plugin.getService()
	if any(sDict):
		services = []
		for item in sDict.items():
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
       
#More plumbing required.
@api_view(['GET','DELETE'])
def service_detail(request,pk,format=None):
    """
    Retrieve, update or delete a service
    """
    try:
	plugin = ConsulPlugin()
        service = plugin.getServiceDetails(name=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
	
    if any(service):
    	if request.method == 'GET':
        	tempService = Service(name=pk,address=service[pk])
		serializer = ServiceSerializer(tempService)
        	return Response(serializer.data)

    	elif request.method == 'DELETE':
        	plugin.deleteService(pk)
        	return Response(status=status.HTTP_204_NO_CONTENT)
    else:return Response(status=status.HTTP_404_NOT_FOUND)
