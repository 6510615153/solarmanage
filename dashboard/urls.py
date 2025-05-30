from django.urls import path
from . import views

app_name = "dashboard"

urlpatterns = [
    path('<int:plant_id>/', views.dashboard_main, name='dashboard_main'),
    path('customize/', views.dashboard_customize, name='dashboard_customize'),
]
