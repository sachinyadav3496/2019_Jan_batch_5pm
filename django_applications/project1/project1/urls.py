from django.contrib import admin
from django.urls import path,include 
from . import views 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('app1/',include('app1.urls')),
    path('app2/',include("app2.urls")),
]
