from django.urls import path
from . import views

app_name = "solarplant"

urlpatterns = [
    # path('plants/', views.plant_list, name='plant_list'),
    path('plants/create/', views.create_plant, name='create_plant'),
    path('zones/create/', views.create_zone, name='create_zone'),
    path('panels/create/', views.create_panel, name='create_panel'),
]
