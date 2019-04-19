
from django.urls import path 
from blog import api_views 

urlpatterns = [

    path('',api_views.index),
]