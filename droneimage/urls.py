from django.urls import path
from . import views

app_name = "droneimage"

urlpatterns = [
    path('image/upload/', views.upload_image, name='upload_image'),
    path('image/upload/success', views.success, name='success'),
]