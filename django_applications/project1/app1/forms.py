from django import forms 


class Login(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(min_length=5,
        widget=forms.PasswordInput)


class Signup(forms.Form): 
    email = forms.EmailField()
    password = forms.CharField(
        widget=forms.PasswordInput
    )
    fname = forms.CharField()
    lname = forms.CharField()


class ForgotPassword(forms.Form):
    email = forms.EmailField()

class ResetPassword(forms.Form):
    otp = forms.CharField(max_length=6)
    password = forms.CharField(widget=forms.PasswordInput)
