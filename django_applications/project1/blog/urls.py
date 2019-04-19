
from django.urls import path 
from blog import views 
urlpatterns = [

    path('',views.Blog.as_view()),
    path('update_blog/',views.UpdateBlog.as_view(),name='post_blog'),
    path('update/',views.PostBlog.as_view()),
    path('<str:error>/',views.Blog.as_view()),
]