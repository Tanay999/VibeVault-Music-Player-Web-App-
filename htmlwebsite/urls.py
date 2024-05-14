from django.contrib import admin
from django.urls import include, path
from htmlwebsite import views

urlpatterns = [
   path('', views.home, name='home'),
   path('login', views.login, name='login'),
   path('signup', views.signup, name='signup'),
]