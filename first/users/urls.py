from django.urls import path
from . import views

urlpatterns = [
    path('register', views.reg),
    path('login', views.index),
    path('users/new', views.reg),
    path('users', views.show),
]