from rest_framework import serializers
from EMSBroker.models import Service, ServiceHelper

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('name','address',)


class ServiceHelperSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceHelper
        fields = ('service','specifics',)
