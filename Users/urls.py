from django.contrib import admin
from django.urls import path

from Users import views
urlpatterns = [
     path('', views.home, name='home')
]