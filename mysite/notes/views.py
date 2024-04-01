from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import UserTable, Activities    
from django.contrib import messages
from django.db import IntegrityError
# from django.contrib.auth.forms import UserCreationForm --> create form for defaul

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
       try:
           user = UserTable(user_name=username,user_email=email,user_university=university,user_carrer=carrer,user_graduated=graduation,user_password=password)
           user.save()
           print('success') 
           messages.success(request,'Registro exitoso. Ahora puedes iniciar sesión.') 
           return render(request,'login/index.html') 
       except IntegrityError as e:
           error_message= str(e) 
           messages.error(request,f'Error de integridad {error_message}') 
    else:
        messages.error(request,'Las contraseñas no coinciden.')





