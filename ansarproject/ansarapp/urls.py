from django.contrib import admin
from django.urls import path

from .views import myapp_view

urlpatterns = [
    path('', myapp_view)    
]