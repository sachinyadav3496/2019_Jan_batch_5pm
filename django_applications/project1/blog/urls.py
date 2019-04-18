
from django.urls import path 
from blog import views 
urlpatterns = [

    path('',views.Blog.as_view()),
    path('update_blog/',views.UpdateBlog.as_view(),name='post_blog'),
    path('<str:error>/',views.Blog.as_view()),
]