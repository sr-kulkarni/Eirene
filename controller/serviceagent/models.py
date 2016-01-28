from django.db import models

# Create your models here.
from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

class Serviceagent(models.Model):
	agent = models.CharField(max_length=128, unique=True)

class Service(models.Model):
	name = models.CharField(max_length=128, unique=True)
	serviceagent = models.ForeignKey(Serviceagent)



