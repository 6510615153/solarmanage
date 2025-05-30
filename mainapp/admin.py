from django.contrib import admin
from .models import SolarPlant, SolarPanel, Zone

# Register your models here.


# Register your models here.

class SolarPlantAdmin(admin.ModelAdmin):
    list_display = ("id", "plant_name", "plant_owner", "plant_address")

class SolarPanelAdmin(admin.ModelAdmin):
    list_display = ("id", "panel_code", "panel_energy", "panel_condition")

class ZoneAdmin(admin.ModelAdmin):
    list_display = ("id",)

admin.site.register(SolarPlant, SolarPlantAdmin)
admin.site.register(SolarPanel, SolarPanelAdmin)

admin.site.register(Zone, ZoneAdmin)