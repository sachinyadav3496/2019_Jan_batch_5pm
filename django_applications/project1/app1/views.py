from django.shortcuts import render

def index(request):
    return render(request,'app1/index.html')


def data(request):
    return render(request,'app1/data.html')