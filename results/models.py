from django.db import models

# Create your models here.
from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()