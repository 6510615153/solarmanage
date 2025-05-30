from django.urls import path
from . import views

app_name = "analysis"

urlpatterns = [
    path('report/upload/', views.upload_report, name='upload_report'),
    path('report/upload/success', views.success, name='success'),
    path('report/details/<int:report_id>', views.details, name='details'),
]