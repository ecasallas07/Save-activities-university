from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import User, Activities    


def home(request):
    return render(request,'home/index.html')


def login(request):
    return render(request,'home/index.html') 
 
def register(request):
    return HttpResponse("register")


