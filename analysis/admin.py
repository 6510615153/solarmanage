from django.contrib import admin
from .models import Report

# Register your models here.


# Register your models here.

class ReportAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "timestamp", "solarplant")

admin.site.register(Report, ReportAdmin)