from django import forms 

class Login(forms.Form):

    email = forms.EmailField()
    password  = forms.CharField(min_length=5,
    widget=forms.PasswordInput)

