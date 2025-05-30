from django.shortcuts import render, redirect
from .forms import SolarPlantForm, ZoneForm, SolarPanelForm
from .models import SolarPlant, Zone, SolarPanel

# Create your views here.

def create_plant(request):
    if request.method == 'POST':
        form = SolarPlantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('plant_list')
    else:
        form = SolarPlantForm()
    return render(request, 'solarplant/create_plant.html', {'form': form})


def create_zone(request):
    if request.method == 'POST':
        form = ZoneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('plant_list')
    else:
        form = ZoneForm()
    return render(request, 'solarplant/create_zone.html', {'form': form})


def create_panel(request):
    if request.method == 'POST':
        form = SolarPanelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('plant_list')
    else:
        form = SolarPanelForm()
    return render(request, 'solarplant/create_panel.html', {'form': form})


def plant_list(request):
    plants = SolarPlant.objects.all()
    return render(request, 'solarplant/plant_list.html', {'plants': plants})