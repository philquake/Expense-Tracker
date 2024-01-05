from django.db import models
from datetime import date
# Create your models here.
class Tracker(models.Model):
    expense = models.CharField(max_length=255)
    amount = models.FloatField(default=0)
    cat = models.CharField(max_length=255)
    date = models.DateField()

