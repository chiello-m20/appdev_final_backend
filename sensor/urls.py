from django.urls import path
from . import views

urlpatterns = [
    path('api/sensor/', views.receive_data, name='receive_data'),
    path('api/sensor/clear/', views.clear_sensor_data, name='clear_sensor_data'),
]
