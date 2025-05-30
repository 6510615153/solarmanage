from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from users.models import Member
from .models import SolarPlant, Zone

# Create your views here.

def solarplant(request):

    current_member = Member.objects.get(member_user=request.user)

    all_plants = SolarPlant.objects.filter(plant_owner=current_member)

    # energy_generated = [plant.total_energy_generated() for plant in all_plants]

    energy_generated = []

    for plant in all_plants:
        zones = Zone.objects.filter(zone_plant=plant)
        zone_energy_generated = sum([zone.total_energy_generated() for zone in zones])

        energy_generated.append(zone_energy_generated)


    return render(request, "mainapp/solarplant.html", {
        "member": current_member,
        "plants": all_plants,
        "energy": energy_generated,
    })

# def details(request, plant_id):

#     current_plant = SolarPlant.objects.get(id=plant_id)

#     current_image = current_plant.get_latest_image()

#     all_panels = current_plant.plant_panels.all()

#     return render(request, "mainapp/plant_details.html", {
#         "plant": current_plant,
#         "pic": current_image,
#         "panels": all_panels,
#     })