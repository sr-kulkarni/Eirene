from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
#from rest_framework.renderers import JSONRenderer
#from rest_framework.parsers import JSONParser

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from serviceagent.models import Serviceagent,Service
from serviceagent.serializers import ServiceagentSerializer, ServiceSerializer


@api_view(['GET','POST'])
def service_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        services = Service.objects.all()
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        #data = JSONParser().parse(request)
        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return JSONResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def service_detail(request,pk):
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

    elif request.method == 'PUT':
        #data = JSONParser().parse(request)
        serializer = ServiceSerializer(service, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        service.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET','POST'])
def agent_list(request):
    if request.method == 'GET':
        agents = Serviceagent.objects.all()
        serializer = ServiceagentSerializer(agents, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        #data = JSONParser().parse(request)
        serializer = ServiceagentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def agent_detail(request,pk):
    """
    Retrieve, update or delete a service
    """
    try:
        #print name
        agent = Serviceagent.objects.get(pk=pk)
    except Serviceagent.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ServiceagentSerializer(agent)
        return Response(serializer.data)

    elif request.method == 'PUT':
        #data = JSONParser().parse(request)
        serializer = ServiceagentSerializer(agent, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        agent.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

