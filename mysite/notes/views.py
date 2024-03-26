from django.shortcuts import render
from django.http import HttpResponse
# from .mod



def index(request):
    return HttpResponse("Hello, world. You're at the notes index.")
    
def login(request):
    return HttpResponse("Login")

def register(request):
    return HttpResponse("register")


