from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Service(models.Model):
	name = models.CharField(max_length=50)
	address = models.CharField(max_length=80)
	

class ServiceHelper(models.Model):
	service = models.OneToOneField(Service, on_delete=models.CASCADE, primary_key=True,)
	specifics = models.CharField(max_length=200)









