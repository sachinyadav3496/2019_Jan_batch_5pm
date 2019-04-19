from django.shortcuts import render,redirect 
from django.views.generic import ListView 
from django.http import HttpResponse
from blog.models import Story
from blog.forms import Blog_Form
from django.contrib.auth.models import User 
from django.utils import timezone
from django.contrib import messages 
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
        if 'email' in request.session : 
            form = Blog_Form()
            return render(request,"blog/update_blog.html",{ 'form':form })
        else : 
            e = "Please Login to Post your Blogs"
            messages.add_message(request, messages.ERROR, e)
            return redirect(to="index")

    def post(self,request):
        return redirect(to='/blog/',error="We handle only get Request to this page")
    

class PostBlog(ListView):
    def get(self,request):
        return redirect(to='/blog/',error='only post method allowed to post a new blog')
        
    def post(self,request):
        form = Blog_Form(request.POST)
        form.is_valid()
        title = form.cleaned_data['title']
        topic = form.cleaned_data['topic']
        content= form.cleaned_data['content']
        author = User.objects.get(email=request.session['email'])
        pub_date = timezone.now().date()
        s1 = Story(title=title,topic=topic,pub_date=pub_date,content=content,author=author)
        s1.save()
        return redirect(to='/blog/',error="Post Published Sucessfully")
