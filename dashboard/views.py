from django.shortcuts import render, redirect
from datetime import datetime, timedelta

class Dashboard:
    def can_user_view(self, user, plant_id):
        return True

    def show_plant_performance(self, plant_id):
        return {"efficiency": 88.5, "output": 12500}

    def show_energy_forecast(self, plant_id):
        return {"forecast_kWh": 13500, "date": datetime.now().date()}

    def show_alerts(self, plant_id):
        return [
            {"timestamp": datetime.now() - timedelta(hours=1), "level": "warning", "message": "Low Voltage"},
            {"timestamp": datetime.now() - timedelta(days=1), "level": "info", "message": "Completed Checking"}
        ]

    def get_latest_images(self, plant_id):
        return [
            {"url": "https://via.placeholder.com/300x200?text=Drone+Image+1", "captured_at": datetime.now()},
            {"url": "https://via.placeholder.com/300x200?text=Drone+Image+2", "captured_at": datetime.now() - timedelta(hours=2)}
        ]

    def customize_view(self, options):
        print("Customization options received:", options)

dashboard = Dashboard()

def dashboard_main(request, plant_id):
    if not dashboard.can_user_view(request.user, plant_id):
        return redirect('no_permission')

    plant = {
        "id": plant_id,
        "name": f"Solar Plant #{plant_id}",
        "location": "Chiang Mai, Thailand"
    }

    return render(request, 'dashboard_app/dashboard.html', {
        'plant': plant,
        'performance': dashboard.show_plant_performance(plant_id),
        'forecast': dashboard.show_energy_forecast(plant_id),
        'alerts': dashboard.show_alerts(plant_id),
        'images': dashboard.get_latest_images(plant_id)
    })

def dashboard_customize(request):
    if request.method == 'POST':
        options = {
            'theme': request.POST.get('theme'),
            'show_images': request.POST.get('show_images')
        }
        dashboard.customize_view(options)
        return redirect('dashboard_main', plant_id=1)
    return render(request, 'dashboard_app/customize.html')
