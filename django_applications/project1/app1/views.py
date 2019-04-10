from django.shortcuts import render
from django.http import HttpResponse
from . import forms 
def index(request):
    e = "Please Sign In to Enjoy Our Services"
    return render(request,'app1/index.html',{'error':e})


def data(request):
    return render(request,'app1/data.html')

def signup(request):
    return render(request,"app1/signup.html")

def login(request):
    if request.method == "POST" : 
        form = forms.Login(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            e = f"User = {email} and Password = {password}"
            return render(request,'app1/index.html',{'error':e})
            
        else : 
            e = "Invalid Data Provided..Please Mind your Input"
            return render(request,'app1/index.html',{'error':e})

           
    else : 
        e = "Request Method Does Not Allowed"
        return render(request,'app1/index.html',{'error':e})

def mksignup(request):
    return HttpResponse("Sucess")