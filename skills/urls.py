# skills/urls.py

from django.urls import path
from skills import views

urlpatterns = [
    path('', views.employee_list, name='employee_list'),  # Add this or any other URL patterns needed
]
