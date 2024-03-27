from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import User, Activities    
from django.contrib import messages

def home(request):
    return render(request,'home/index.html')


def validate(request):
    return render(request,'login/index.html') 
 
def register(request):
    if request.method == 'POST':
       username= request.POST['username'] 
       email = request.POST['email']   
       university = request.POST['university'] 
       carrer = request.POST['carrer']  
       graduation = request.POST['graduation']
       password = request.POST['password'] 
       confirm_password = request.POST['confirm_password'] 

    if password == confirm_password:
       user = User(user_name=username,user_email=email,user_university=university,user_carrer=carrer,user_graduated=graduation,password=password)
       user.save()
       messages.success(request,'Registro exitoso. Ahora puedes iniciar sesión.') 
       return redirect('validate') 
    else:
        messages.error(request,'Las contraseñas no coinciden.')





