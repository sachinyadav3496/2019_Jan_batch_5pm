
from django import forms


class Blog_Form(forms.Form):
    title = forms.CharField(max_length=250)
    topic = forms.CharField(max_length=100)
    content = forms.CharField(widget=forms.Textarea)