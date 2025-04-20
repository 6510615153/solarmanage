from django.contrib import admin
from .models import Image

# Register your models here.


# Register your models here.

class SolarPlantAdmin(admin.ModelAdmin):
    list_display = ("id", "image", "timestamp", "solarplant")

admin.site.register(Image, SolarPlantAdmin)