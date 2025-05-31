from django.db import models

from mainapp.models import SolarPlant

# Create your models here.

class Notification(models.Model):
    plant = models.ForeignKey(SolarPlant, on_delete=models.CASCADE)
    message = models.TextField()
    level = models.CharField(max_length=50)  # e.g. 'warning', 'critical'
    timestamp = models.DateTimeField(auto_now_add=True)
