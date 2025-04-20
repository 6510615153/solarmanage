from django import forms
from .models import Image
from mainapp.models import SolarPlant

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['solarplant', 'image', 'weather', 'location', 'temperature', 'date'] 

        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),  # Ensure a date picker appears for the date field
        }
