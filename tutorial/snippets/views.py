from django.shortcuts import render
from django.http import HttpResponse

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import generics

# Create your views here.
#@api_view(['GET', 'POST'])

def index(request):
        return HttpResponse("Snippets says hey there world!")


# Create your views here.


class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
