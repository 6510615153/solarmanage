from django.shortcuts import render, redirect
from .forms import SolarPlantForm, ZoneForm, SolarPanelForm
from mainapp.models import SolarPlant, Zone, SolarPanel

from users.models import Member

from django.contrib.auth.decorators import login_required

import secrets

def code_generate_plant():
    while True:
        plant_code = secrets.token_hex(10)
        if not SolarPlant.objects.filter(plant_code=plant_code).exists():
            return plant_code
        
def code_generate_panel():
    while True:
        panel_code = secrets.token_hex(10)
        if not SolarPanel.objects.filter(panel_code=panel_code).exists():
            return panel_code

# Create your views here.

@login_required(login_url='/login')
def create_plant(request):
    current_member = Member.objects.get(member_user=request.user)
    if current_member.member_role not in ["manager"]:
        return redirect("users:unauthorized")
    if request.method == 'POST':
        form = SolarPlantForm(request.POST)
        if form.is_valid():
            plant = form.save(commit=False)
            plant.plant_code = code_generate_plant()
            plant.save()
            return redirect('mainapp:solarplant')
    else:
        form = SolarPlantForm()
    return render(request, 'solarplant/create_plant.html', {'form': form})

@login_required(login_url='/login')
def create_zone(request):
    current_member = Member.objects.get(member_user=request.user)
    if current_member.member_role not in ["manager"]:
        return redirect("users:unauthorized")
    if request.method == 'POST':
        form = ZoneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mainapp:solarplant')
    else:
        form = ZoneForm()
    return render(request, 'solarplant/create_zone.html', {'form': form})

@login_required(login_url='/login')
def create_panel(request):
    current_member = Member.objects.get(member_user=request.user)
    if current_member.member_role not in ["manager"]:
        return redirect("users:unauthorized")
    if request.method == 'POST':
        form = SolarPanelForm(request.POST)
        if form.is_valid():
            panel = form.save(commit=False)
            panel.panel_code = code_generate_panel()
            panel.save()
            return redirect('mainapp:solarplant')
    else:
        form = SolarPanelForm()
    return render(request, 'solarplant/create_panel.html', {'form': form})


# def plant_list(request):
#     plants = SolarPlant.objects.all()
#     return render(request, 'solarplant/plant_list.html', {'plants': plants})