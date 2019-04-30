from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from . import forms 
#from app1.models import User 
from django.contrib.auth.models import User
from random import randint 
from django.core.mail import send_mail 
def index(request):
    if 'email' in request.session :
        email = request.session['email'] 
        u1 = User.objects.get(email=email)
        data = { 
                        'First Name': u1.first_name,
                        'Last Name' : u1.last_name,
                        'Email' : u1.email,
                    }
        return render(request,'app1/profile.html',{'data':data,'title':'Profile','flag':True})

    else : 
        e = "Please Sign In to Enjoy Our Services"
        return render(request,'app1/index.html',{'error':e,'title':'HOME'})


def data(request):
    return render(request,'app1/data.html',{'title':"data"})

def signup(request):
    return render(request,"app1/signup.html",{'title':'Signup'})


from django.contrib.auth import authenticate
def login(request):
    if request.method == "POST" : 
        form = forms.Login(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try : 
                u1 = User.objects.get(email=email)
            except User.DoesNotExist as e :
                e = "NO such User Exists"
                messages.add_message(request, messages.ERROR, e)
                return redirect(to="index")    
                #return render(request,"app1/index.html",{'error':e,'title':'LOGIN'})
            else :
                u1 = authenticate(username=u1.username,password=password)
                if u1 is not None : 
                
                    data = { 
                        'First Name': u1.first_name,
                        'Last Name' : u1.last_name,
                        'Email' : u1.email,
                    }
                    request.session['email'] = u1.email 
                    return render(request,'app1/profile.html',{'data':data,'title':'Profile','flag':True})
                else : 
                    e = "Invaid Password Try Again"
                    messages.add_message(request, messages.ERROR, e)
                    return redirect(to="index")
                    #return render(request,'app1/index.html',{'error':e,'title':'HOME'})  

        else : 
            e = "Invalid Data Provided..Please Mind your Input"
            messages.add_message(request, messages.ERROR, e)
            return redirect(to="index")
                    
            #return render(request,'app1/index.html',{'error':e,'title':'HOME'})       
    else : 
        e = "Request Method Does Not Allowed"
        messages.add_message(request, messages.ERROR, e)
        return redirect(to="index")
                    
        #return render(request,'app1/index.html',{'error':e,'title':'HOME'})

def mksignup(request):
    if request.method == "POST" : 
        form  = forms.Signup(request.POST)
        if form.is_valid() : 
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            fname = form.cleaned_data['fname']
            lname = form.cleaned_data['lname']
            password  = form.cleaned_data['password']
            try : 
                User.objects.get(email=email)
            except User.DoesNotExist as e : 
                user = User(username=username,email=email,first_name=fname,last_name=lname)
                user.set_password(password)
                user.save()
                return render(request,"app1/index.html",{'error':"Account sucessfully created please login to use our services",'title':'HOME'})
            else : 
                error = "User Already Exists"
                return render(request,'app1/index.html',{'error':error,'title':"HOME"})
        else : 
            error = "Invalid Form DATA"
            return render(request,'app1/index.html',{'error':error,'title':"HOME"})
        

    else : 
        error = "Invalid Form Method, We only accept POST"
        return render(request,'app1/index.html',{'error':error,'title':"HOME"})
        
def logout(request):
    e = "...Thanks for Being Here...."
    messages.add_message(request, messages.INFO, e)
    del request.session['email']
    return redirect(to='index')

def forgot(request): 
    form = forms.ForgotPassword()
    return render(request,'app1/forgot.html',{'form':form,'title':"RESET PASSWORD"})

def reset_password(request):
    if request.method == "POST" : 
        form = forms.ForgotPassword(request.POST)
        if form.is_valid() : 
            email = form.cleaned_data['email']
            try : 
                u1 = User.objects.get(email=email)
            except User.DoesNotExist as e : 
                error = "No such User Exists"
                messages.add_message(request, messages.ERROR, error)
            else : 
                form = forms.ResetPassword()
                #logic to generate otp
                otp = str(randint(111111,999999))
                request.session['otp'] = otp 
                request.session['otp_email'] = email
                to = email 
                mail_from = "Grras Solutions"
                subject = "OTP Verification"
                messege = f"Please Provide This OTP {otp} to reset your Password."

                send_mail(
                    subject,
                    messege,
                    mail_from,
                    [to,],
                    fail_silently=False,)
                
                return render(request,"app1/reset.html",{'form':form,'error':'Please Provide OTP To RESET Password'})
        else : 
            error = "Invalid DATA Provided"
            messages.add_message(request, messages.ERROR, error)

    else : 
        error = "Invalid Method Provided"
        messages.add_message(request, messages.ERROR, error)
    return redirect(to='index')



def verify_otp(request):
    if request.method == 'POST' : 
        form = forms.ResetPassword(request.POST)
        form.is_valid()
        otp = form.cleaned_data['otp']
        otp_verify = request.session['otp']
        password = form.cleaned_data['password']
        email = request.session['otp_email']
        if otp == otp_verify : 
            u1 = User.objects.get(email=email)
            u1.set_password(password)
            u1.save()
            error = "Password Updated Sucessfully...Login to enjoy your services"
            messages.add_message(request, messages.ERROR, error)
            return redirect(to='index')

        else :
            return render(request,"app1/reset.html",{'form':form,'error':'Invaid OTP Try Again'})

    else : 
        error = "Invalid Method Provided"
        messages.add_message(request, messages.ERROR, error)
        return redirect(to='index')
