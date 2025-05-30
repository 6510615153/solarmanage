from django.db import models
from mainapp.models import SolarPlant
from droneimage.models import Image
from users.models import Member

# Create your models here.

class Report(models.Model):

    timestamp = models.DateTimeField(auto_now_add=True)  
    solarplant = models.ForeignKey(SolarPlant, on_delete=models.CASCADE, related_name='reports')

    writer = models.ForeignKey(Member, on_delete=models.CASCADE)

    image =  models.ForeignKey(Image, on_delete=models.CASCADE)

    title = models.CharField(max_length=99)
    text = models.TextField()

    date = models.DateField()  

    def __str__(self):
        return f"Report {self.title} uploaded on {self.timestamp} for {self.solarplant} "