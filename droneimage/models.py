from django.db import models
from mainapp.models import SolarPlant

# Create your models here.

class Image(models.Model):
    image = models.ImageField(upload_to='storage/')  
    timestamp = models.DateTimeField(auto_now_add=True)  
    solarplant = models.ForeignKey(SolarPlant, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return f"Image {self.id} uploaded on {self.timestamp} for {self.solarplant}"