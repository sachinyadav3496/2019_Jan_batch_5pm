from django.shortcuts import render
from django.http import HttpResponse
from . import forms
from .models import User
# Create your views here.

def index(request):
    form = forms.Login()
    return render(request,"app1/index.html",{'form':form})

def signup(request):
    form = forms.Signup()
    return render(request,"app1/signup.html",{'form':form})

def mk_signup(request):
    form = forms.Signup(request.POST)
    if form.is_valid(): 
        # logic to create a user
        # check if user already exist or not
        try : 
            u = User.objects.get(email=form.cleaned_data['email'])
        except User.DoesNotExist as e : 
            # user not exist so create a user
            u = User(email=form.cleaned_data['email'],
                    first_name=form.cleaned_data['first_name'],
                    last_name=form.cleaned_data['last_name'],
                    password=form.cleaned_data['password'])
            u.save()
            return HttpResponse("User Created Sucessfully")
        else : 
            return HttpResponse("Error!!! User already Exists Please Sign_in")
        

    else : 
        return  HttpResponse("Errorr!! Invalid DATA")


def all_users(request):
    users = User.objects.all()
    data = [] 
    for each_user in users : 
        d = { 
                'First Name': each_user.first_name,
                'Last Name' : each_user.last_name,
                'Email' : each_user.email,
                'Password' : each_user.password,
                }
        data.append(d)
    return render(request,"app1/users.html",{'data':data})

def login(request):
    form = forms.Login(request.POST)
    if form.is_valid():
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        try : 
            u = User.objects.get(email=email)
        except User.DoesNotExist as e : 
            return HttpResponse("No such User Exists Please Signup")
        else : 
            if u.password == password : 
                page = f"""
                <br>
                First Name = {u.first_name} <br>
                Last Name = {u.last_name} <br>
                Email = {u.email} </br>
                Password = {u.password} </br>
                """
                return HttpResponse(page)
            else : 
                return HttpResponse("Invaid Password")
    else : 
        return HttpResponse("Invalid DATA")
