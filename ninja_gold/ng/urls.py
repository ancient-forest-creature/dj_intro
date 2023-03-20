from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('process_money/<str:loc>', views.process_money, name='pm'),
    path('reset', views.killit, name='reset')
]