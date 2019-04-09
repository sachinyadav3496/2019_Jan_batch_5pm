from django.urls import path
from . import views 
urlpatterns = [
    path('',views.index),
    path('data/',views.data),
    path('signup/',views.signup),
    path('login/',views.login),
    path('mk_signup/',views.mksignup),
]
