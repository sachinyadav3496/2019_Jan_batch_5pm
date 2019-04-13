from django.urls import path 
from . import views

urlpatterns  = [

            path('',views.index),
            path('signup/',views.signup),
            path('login/',views.login),
            path('mk_signup/',views.mk_signup),
            path('all_users/',views.all_users),

        ]
