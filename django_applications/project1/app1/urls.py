from django.urls import path
from . import views 
urlpatterns = [
    path('',views.index,name='index'),
    path('data/',views.data),
    path('signup/',views.signup),
    path('login/',views.login),
    path('mk_signup/',views.mksignup),
    path('logout/',views.logout),
    path('forgot/',views.forgot),
    path("reset_password/",views.reset_password),
    path("verify_otp/",views.verify_otp),

]
