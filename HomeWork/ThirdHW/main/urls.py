
from .views import input_Salespeople, get_Salespeople
from django.urls import path

urlpatterns = [
    path('', input_Salespeople, name='input_Salespeople'),
    path('Salespeople', get_Salespeople, name='get'),
]
