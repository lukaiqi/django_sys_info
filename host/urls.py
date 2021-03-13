from django.contrib import admin
from django.urls import path, include
from .views import *
urlpatterns = [
    path('', index, name='index'),
    path('user/', user, name='user'),
    path('cpu/', cpu, name='cpu'),
    path('cpu/<str:chart>/', cpu, name='cpu'),
    path('memory/', memory, name='memory'),
    path('disk/', disk, name='disk'),
    path('network/', network, name='network'),
    ]
