from django import forms
from .models import SolarPlant, Zone, SolarPanel

class SolarPlantForm(forms.ModelForm):
    class Meta:
        model = SolarPlant
        fields = ['name', 'location', 'capacity']


class ZoneForm(forms.ModelForm):
    class Meta:
        model = Zone
        fields = ['name', 'plant']


class SolarPanelForm(forms.ModelForm):
    class Meta:
        model = SolarPanel
        fields = ['panel_id', 'zone', 'performance']
