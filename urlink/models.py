from django.db import models
from django.db.models import Model


# Create your models here.

class urlMod(Model):
    basicurl = models.URLField(max_length=200, unique=True)
    basiccontent = models.TextField()



