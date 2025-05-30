from django.shortcuts import render, redirect
from datetime import datetime, timedelta
from mainapp.models import SolarPanel, SolarPlant, Member

class Dashboard:
    def can_user_view(self, user, plant_id):
        return True

    def show_plant_performance(self, plant_id):
        plant = SolarPlant.objects.get(id=plant_id)
        # energy_generated = plant.total_energy_generated()
        return {
                    "efficiency": plant.average_efficiency(), 
                    "output": plant.total_energy_generated(),
                }

    def show_energy_forecast(self, plant_id):
        return {"forecast_kWh": 13500, "date": datetime.now().date()}

    def show_alerts(self, plant_id):
        return [
            {"timestamp": datetime.now() - timedelta(hours=1), "level": "warning", "message": "Low Voltage"},
            {"timestamp": datetime.now() - timedelta(days=1), "level": "info", "message": "Completed Checking"}
        ]

    def get_latest_images(self, plant_id):
        return [
            {"url": "https://via.placeholder.com/300x200?text=Drone+Image+1", "captured_at": datetime.now()}
        ]

    def customize_view(self, options):
        print("Customization options received:", options)

dashboard = Dashboard()

# def dashboard_main(request, plant_id):
#     if not dashboard.can_user_view(request.user, plant_id):
#         return redirect('no_permission')

#     # plant = {
#     #     "id": plant_id,
#     #     "name": f"Solar Plant #{plant_id}",
#     #     "location": "Chiang Mai, Thailand"
#     # }

#     plant = SolarPlant.objects.get(id=plant_id)

#     current_image = plant.get_latest_image()

#     all_panels = plant.plant_panels.all()

#     # return render(request, "mainapp/plant_details.html", {
#     #     "plant": current_plant,
#     #     "pic": current_image,
#     #     "panels": all_panels,
#     # })

#     return render(request, 'dashboard/dashboard.html', {
#         'plant': plant,
#         'performance': dashboard.show_plant_performance(plant_id),
#         'forecast': dashboard.show_energy_forecast(plant_id),
#         'alerts': dashboard.show_alerts(plant_id),
#         'images': dashboard.get_latest_images(plant_id),
#         "pic": current_image,
#         "panels": all_panels,
#     })

def dashboard_customize(request):
    if request.method == 'POST':
        options = {
            'theme': request.POST.get('theme'),
            'show_images': request.POST.get('show_images')
        }
        dashboard.customize_view(options)
        return redirect('dashboard_main', plant_id=1)

    return render(request, 'dashboard/customize.html')

def dashboard_main(request, plant_id):
    dashboard = Dashboard()
    plant = SolarPlant.objects.get(id=plant_id)
    performance = dashboard.show_plant_performance(plant_id)
    forecast = dashboard.show_energy_forecast(plant_id)
    alerts = dashboard.show_alerts(plant_id)
    # activities = dashboard.get_recent_activities()
    images = dashboard.get_latest_images(plant_id)

    current_image = plant.get_latest_image()

    all_panels = plant.plant_panels.all()


    # Mock: อุณหภูมิแผงโซลาร์เซลล์รายชั่วโมง
    solar_temp_data = {
        'time_labels': ['06:00', '07:00', '08:00', '09:00', '10:00',
                        '11:00', '12:00', '13:00', '14:00', '15:00',
                        '16:00', '17:00', '18:00'],
        'temperatures': [28.0, 30.5, 33.0, 36.2, 40.1,
                         44.5, 47.8, 49.3, 48.6, 46.0,
                         42.2, 38.1, 33.7]
    }

    return render(request, 'dashboard/dashboard.html', {
        'plant': plant,
        'performance': performance,
        'forecast': forecast,
        'alerts': alerts,
        # 'activities': activities,
        'pic': current_image,
        'panels': all_panels,
        'solar_temp_data': solar_temp_data,
    })
