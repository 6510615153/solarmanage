from django.db import models
from mainapp.models import SolarPlant

# Create your models here.

class Image(models.Model):

    SKY = [
        ('cloudy', 'Cloudy'),
        ('clear', 'Clear'),
        ('rain', 'Rain'),
        ('fog', 'Fog'),
        ('other', 'Other'),
    ]

    image = models.ImageField(upload_to='storage/')  
    timestamp = models.DateTimeField(auto_now_add=True)  
    solarplant = models.ForeignKey(SolarPlant, on_delete=models.CASCADE, related_name='images')

    weather = models.CharField(max_length=20, choices=SKY, default='clear')

    location = models.CharField(max_length=255) 
    temperature = models.FloatField()  
    date = models.DateField()  

    def __str__(self):
        return f"Image {self.id} uploaded on {self.date} for {self.solarplant}"