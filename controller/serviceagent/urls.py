from django.conf.urls import url
from serviceagent import views

urlpatterns = [
    url(r'^services/$', views.service_list),
    url(r'^agents/$', views.agent_list),
]
