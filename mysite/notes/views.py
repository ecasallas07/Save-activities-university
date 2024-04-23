from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import UserTable, Activities , Documents  
from notes.forms import DocumentsForm
from django.db import IntegrityError
#--------------------------------- not used libraries --------------------------------
# from django.template import loader
# from django.contrib.message import message
# from django.contrib.auth import authenticate, login
# from django.contrib.sessions.models import Session
# from django.contrib.auth.forms import UserCreationForm --> create form for defaul
#--------------------------------------------------------------------------------------

def test(request):
    return render(request,'home_user/index.html')

def home(request):
    return render(request,'home/index.html')


def validate(request):
    return render(request,'login/index.html') 
 
def register(request):
    # this form is whean is not used forms.py of user
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
        #    messages.success(request,'Registro exitoso. Ahora puedes iniciar sesión.') 
           return render(request,'login/index.html') 
       except IntegrityError:
        #    error_message= str(e)
           pass 
        #    messages.error(request,f'Error de integridad {error_message}') 
    else:
        # messages.error(request,'Las contraseñas no coinciden.')
        pass

def loguin(request):
    if request.method == 'POST':
       username = request.POST['email']
       password = request.POST['password']
       print(username)
       user = UserTable.objects.get(user_email= username,user_password=password)

       if user is not None:
          request.session['user_id'] = user.id
          request.session['username'] = username
          request.session.save()
          act = Activities.objects.filter(act_user_id=request.session.get('user_id'))
          return render(request,'home_user/activities.html',{ 'session_id':request.session.get('user_id', 'Invitado') , 'act':act})
       else:
          HttpResponse("No funciona")
    else:
        HttpResponse("No funciona, metodo") 

def home_user(request):
    return render(request,'home_user/home.html')

def activities(request):
    if request.method == 'POST':
        name =request.POST['act_name']
        date = request.POST['act_date_delivery']
        score = request.POST['act_score']
        priority = request.POST['act_priority']
        user_id = request.session['user_id']
        category = request.POST['act_category']
        description = request.POST['act_description']
    
        try:
            activity = Activities(act_name=name,act_date_delivery=date,act_score=score,act_priority=priority,act_user_id=user_id,act_category=category,act_description=description)
            activity.save()
            act = Activities.objects.filter(act_user_id=request.session.get('user_id'))
            # return redirect("home_user/activities.html", act= acties)
            return render(request,'home_user/activities.html',{'act':act}) 
        except IntegrityError:
            pass
            # error_message= str(e) 
            # messages.error(request,f'Error de integridad {error_message}')  
    else:
        #filter activities for user_id of session with filter
        activities=Activities.objects.filter(act_user_id=request.session.get('user_id'))           
        return render(request,'home_user/activities.html',{'act':activities})

def documents(request):
    if request.method == 'POST':
        form_docu = DocumentsForm(request.POST,request.FILES)
        if form_docu.is_valid():
            form_docu.save()
            return redirect('home_user/documents')
    else:        
        form = DocumentsForm()
        return render(request,'home_user/documents.html',{'form':form})

def notes(request):
    return render(request,'home_user/notes.html')