from django import forms
from .models import Report
from mainapp.models import SolarPlant

class ReportUploadForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['solarplant', 'image', 'title', 'text', 'date'] 

        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),  # Ensure a date picker appears for the date field
        }
