from django.db import models
from django.utils import timezone

# Create your models here.

# class SolarPlant(models.Model):
#     name = models.CharField(max_length=100)
#     location = models.CharField(max_length=200)
#     capacity = models.FloatField()

#     def __str__(self):
#         return self.name

#     def get_zones(self):
#         return self.zone_set.all()

#     def get_total_output(self):
#         return sum(zone.get_zone_performance() for zone in self.get_zones())

#     def daily_forecast(self):
#         # Placeholder - in real case integrate with an energy forecast system
#         return {"expected_output_kWh": self.capacity * 5}  # Simplified example


# class Zone(models.Model):
#     name = models.CharField(max_length=100)
#     plant = models.ForeignKey(SolarPlant, on_delete=models.CASCADE)
#     panel_count = models.IntegerField(default=0)

#     def __str__(self):
#         return f"{self.name} ({self.plant.name})"

#     def add_panel(self, panel_data):
#         panel = SolarPanel.objects.create(
#             zone=self,
#             panel_id=panel_data.get('panel_id', f"Panel-{timezone.now().timestamp()}"),
#             performance=panel_data.get('performance', 100.0),
#             last_check=timezone.now()
#         )
#         self.panel_count = self.get_panels().count()
#         self.save()
#         return panel

#     def get_panels(self):
#         return self.solarpanel_set.all()

#     def get_zone_performance(self):
#         panels = self.get_panels()
#         if not panels.exists():
#             return 0
#         return sum(p.performance for p in panels) / panels.count()


# class SolarPanel(models.Model):
#     panel_id = models.CharField(max_length=50)
#     zone = models.ForeignKey(Zone, on_delete=models.CASCADE)
#     performance = models.FloatField(default=100.0)
#     last_check = models.DateTimeField(default=timezone.now)

#     def __str__(self):
#         return self.panel_id

#     def check_status(self):
#         return "Alert" if self.performance < 80.0 else "OK"

#     def get_voltage(self):
#         # Placeholder for actual voltage logic
#         return round(self.performance * 0.6, 2)

#     def get_current(self):
#         # Placeholder for actual current logic
#         return round(self.performance * 0.4, 2)
