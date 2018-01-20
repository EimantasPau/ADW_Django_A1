from django.db import models
from datetime import datetime

# Create your models here.

class Appointment(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    time = models.DateTimeField()
    location = models.CharField(max_length=50)
    patient_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=datetime.now)
