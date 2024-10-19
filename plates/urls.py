#plates/urls.py
from django.urls import path
from .views import capture_from_ip_camera
from . import views

urlpatterns = [
    path('capture/', capture_from_ip_camera, name='capture_from_ip_camera'),
    path('', views.home, name='home'),

]

