from django.urls import path
from .views import receive_data

urlpatterns = [
    path('api/sensor/', receive_data),
]
