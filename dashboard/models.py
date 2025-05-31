from django.db import models
from django.contrib.auth.models import User

class SolarPlant(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    efficiency = models.FloatField()
    output = models.IntegerField()

    def __str__(self):
        return self.name

class Notification(models.Model):
    plant = models.ForeignKey(SolarPlant, on_delete=models.CASCADE)
    message = models.TextField()
    level = models.CharField(max_length=50)  # e.g. 'warning', 'critical'
    timestamp = models.DateTimeField(auto_now_add=True)

class DroneImage(models.Model):
    plant = models.ForeignKey(SolarPlant, on_delete=models.CASCADE)
    image_url = models.URLField()
    captured_at = models.DateTimeField()

class DashboardPermission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plant = models.ForeignKey(SolarPlant, on_delete=models.CASCADE)
    can_view = models.BooleanField(default=True)
