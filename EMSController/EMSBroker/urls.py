from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from EMSBroker import views

urlpatterns = [
    url(r'^services/(?P<pk>[0-9]+)$', views.service_detail),
    url(r'^services/$', views.service_list),
]

urlpatterns = format_suffix_patterns(urlpatterns)
