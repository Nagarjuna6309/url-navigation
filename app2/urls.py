from django.urls import path
from app2.views import *
app_name='roman'
urlpatterns = [
    path('roman/',roman,name='roman'),
]
