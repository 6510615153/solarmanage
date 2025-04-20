from django.db import models
from users.models import Member

# Create your models here.

class SolarPanel(models.Model):

    panel_code = models.CharField(max_length=20, blank=True)
    panel_energy = models.IntegerField()
    panel_condition = models.CharField(max_length=5, blank=True)

    def __str__(self):
        return f"{self.panel_code}"
    

class SolarPlant(models.Model):

    plant_code = models.CharField(max_length=20, blank=True)
    plant_name = models.CharField(max_length=32)
    plant_owner = models.ForeignKey(Member, on_delete=models.CASCADE)
    plant_address = models.CharField(max_length=128, blank=True)

    plant_panels = models.ManyToManyField(SolarPanel)

    def __str__(self):
        return f"{self.plant_name}"