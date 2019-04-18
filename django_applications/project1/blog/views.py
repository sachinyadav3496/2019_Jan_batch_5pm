from django.shortcuts import render,redirect 
from django.views.generic import ListView 
from django.http import HttpResponse
from blog.models import Story
from blog.forms import Blog_Form
# Create your views here.

class Blog(ListView) : 
    def get(self,request,error=None):
        print('\n\n',error,"\n\n")
        data = Story.objects.all().order_by("-pub_date")
        all_blogs = []
        for each_post in data :
            tmp = { 
                'title': each_post.title,
                'topic' : each_post.topic,
                'pub_date' : each_post.pub_date,
                'author' : each_post.author.username, 
                'content' : each_post.content, 
            } 
            all_blogs.append(tmp)

        return render(request,'blog/index.html',{'data':all_blogs,'error':error})

class UpdateBlog(ListView):
    def get(self,request):
        form = Blog_Form()

        return render(request,"blog/update_blog.html",{ 'form':form })
        
    def post(self,request):
        return redirect(to='/blog/',error="We handle only Post Request to this page")
    