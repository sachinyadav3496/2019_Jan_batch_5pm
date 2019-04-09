from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    e = "Please Sign In to Enjoy Our Services"
    return render(request,'app1/index.html',{'error':e})


def data(request):
    return render(request,'app1/data.html')

def signup(request):
    return render(request,"app1/signup.html")

def login(request):
    return HttpResponse("Sucess")

def mksignup(request):
    return HttpResponse("Sucess")