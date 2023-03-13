from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('process_money', views.p_m),
    path('destroy', views.killit)
]