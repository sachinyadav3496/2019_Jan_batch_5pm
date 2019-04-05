from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,"index.html")


def data(request):

    page = """
    <a href="/">Home</a>
    <a href="/data/">Data</a>
    <a href="/app1/">App1</a>
    <h1 style='color:red'>App1's Data Page</h1>
    """
    return HttpResponse(page)