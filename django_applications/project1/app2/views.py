from django.shortcuts import render
from . import forms 
# Create your views here.
def index(request):
    form = forms.Login()
    return render(request,"app2/index.html",{'form':form})


def login(request):
    if request.method == "POST" : 
        form = forms.Login(request.POST)
        if form.is_valid(): 
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            return render(request,"app2/profile.html",
                        {'email':email,'password':password})
        else : 
            error = "Invalid Form Data" 
            form = forms.Login()
            return render(request,"app2/index.html",
                    {'form':form,'error':error})

    else :
        error = "Only Post Method Allowed" 
        form = forms.Login()
        return render(request,"app2/index.html",
                    {'form':form,'error':error})


from app1.forms import Signup
def signup(request):
    form = Signup()
    return render(request,"app2/signup.html",{'form':form})