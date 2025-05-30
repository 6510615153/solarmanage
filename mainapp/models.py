from django.db import models
from users.models import Member
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class SolarPanel(models.Model):

    panel_code = models.CharField(max_length=20, blank=True)
    panel_energy = models.IntegerField()
    panel_condition = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(100.0)],
        help_text="Percentage value from 0.0 to 100.0"
    )

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
    
    def get_latest_image(self):
        return self.images.order_by('-id').first()
    
    def total_energy_generated(self):
        return sum(panel.panel_energy for panel in self.plant_panels.all())