from django.shortcuts import render
from django.http import HttpResponse
#from yapsy.PluginManager import PluginManager
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import generics
from snippets.serializers import UserSerializer
from django.contrib.auth.models import User
# Create your views here.
#@api_view(['GET', 'POST'])

from rest_framework import permissions
from snippets.permissions import IsOwnerOrReadOnly
#import snippets.plugins
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import viewsets
from rest_framework import renderers
#from rest_framework.response import Response
from rest_framework.decorators import detail_route
import imp
import os

def index(request):
        return HttpResponse("Snippets says hey there world!")

PluginFolder = "/Users/Saurabh/Django/tutorial/snippets/plugins"
MainModule = "__init__"

def getPlugins():
    plugins = []
    possibleplugins = os.listdir(PluginFolder)
    for i in possibleplugins:
        location = os.path.join(PluginFolder, i)
        if not os.path.isdir(location) or not MainModule + ".py" in os.listdir(location):
            continue
        info = imp.find_module(MainModule, [location])
        plugins.append({"name": i, "info": info})
    return plugins

def loadPlugin(plugin):
    return imp.load_module(MainModule, *plugin["info"])



# Create your views here.
@api_view(('GET',))
def api_root(request, format=None):
    print "This line should be printed."
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format)
    })

class SnippetViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    print "Does it get printed?"
    #simplePluginManager = PluginManager()
# Tell it the default place(s) where to find plugins
    #simplePluginManager.setPluginPlaces(["/Users/Saurabh/Django/tutorial/snippets/plugins/"])
    #simplePluginManager.activatePluginByName('consul')
    #simplePluginManager.consul.get()
    for i in getPlugins():
    	print("Loading plugin " + i["name"])
    	plugin = loadPlugin(i)
    	plugin.run()
    queryset = User.objects.all()
    serializer_class = UserSerializer
