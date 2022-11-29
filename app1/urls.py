from django.urls import path
from app1.views import *
app_name='brock'

urlpatterns = [
    path('brock/',brock,name='brock')
]
