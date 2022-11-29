#Add URL maps to redirect the base URL to our application
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),    
]