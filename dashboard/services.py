from .models import SolarPlant, Notification, DroneImage, DashboardPermission
from django.contrib.auth.models import User
from datetime import datetime

class PerformanceData:
    def __init__(self, plant_id, efficiency, output):
        self.plant_id = plant_id
        self.efficiency = efficiency
        self.output = output

class ForecastData:
    def __init__(self, plant_id, forecast_kWh, date):
        self.plant_id = plant_id
        self.forecast_kWh = forecast_kWh
        self.date = date

class Alert:
    def __init__(self, message, level, timestamp):
        self.message = message
        self.level = level
        self.timestamp = timestamp

class Activity:
    def __init__(self, user, action, timestamp):
        self.user = user
        self.action = action
        self.timestamp = timestamp

class ImageData:
    def __init__(self, url, captured_at):
        self.url = url
        self.captured_at = captured_at

class Dashboard:

    def can_user_view(self, user: User, plant_id: int) -> bool:
        return DashboardPermission.objects.filter(user=user, plant_id=plant_id, can_view=True).exists()

    def show_plant_performance(self, plant_id: int) -> PerformanceData:
        plant = SolarPlant.objects.get(pk=plant_id)
        return PerformanceData(plant.id, plant.efficiency, plant.output)

    def show_energy_forecast(self, plant_id: int) -> ForecastData:
        # Sample logic — use real forecast model in production
        plant = SolarPlant.objects.get(pk=plant_id)
        forecast = plant.output * 1.1  # 10% increase forecast
        return ForecastData(plant.id, forecast, datetime.today().date())

    def show_alerts(self, plant_id: int) -> list[Alert]:
        alerts = Notification.objects.filter(plant_id=plant_id).order_by('-timestamp')[:10]
        return [Alert(a.message, a.level, a.timestamp) for a in alerts]

    def get_recent_activities(self, limit: int) -> list[Activity]:
        return [Activity("admin", "Viewed dashboard", datetime.now())][:limit]

    def get_latest_images(self, plant_id: int) -> list[ImageData]:
        images = DroneImage.objects.filter(plant_id=plant_id).order_by('-captured_at')[:5]
        return [ImageData(i.image_url, i.captured_at) for i in images]

    def customize_view(self, options: dict) -> None:
        print("Customizing dashboard with options:", options)
