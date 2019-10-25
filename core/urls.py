
from django.contrib import admin
from django.urls import path
from core.views import home


# Update urls
app_name='core' 

urlpatterns = [
    path('', home, name='home'), 
]
