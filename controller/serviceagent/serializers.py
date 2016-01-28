from rest_framework import serializers
from serviceagent.models import Serviceagent, Service

class ServiceagentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Serviceagent
        fields = ('agent',)


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('name','serviceagent')


