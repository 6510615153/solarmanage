from django import forms
from .models import Image
from mainapp.models import SolarPlant

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['solarplant', 'image'] 
