from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from serviceagent import views

urlpatterns = [
    url(r'^services/(?P<pk>[0-9]+)$', views.service_detail),
    url(r'^services/$', views.service_list),
    url(r'^agents/$', views.agent_list),
    url(r'^agents/(?P<pk>[0-9]+)$', views.agent_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
