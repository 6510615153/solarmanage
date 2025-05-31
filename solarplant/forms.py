from django import forms
from mainapp.models import SolarPlant, Zone, SolarPanel

class SolarPlantForm(forms.ModelForm):
    class Meta:
        model = SolarPlant
        fields = ['plant_name', 'plant_owner', 'plant_address', 'plant_staffs']


class ZoneForm(forms.ModelForm):
    class Meta:
        model = Zone
        fields = ['zone_plant', 'zone_panels']


class SolarPanelForm(forms.ModelForm):
    class Meta:
        model = SolarPanel
        fields = ['panel_energy', 'panel_condition']
