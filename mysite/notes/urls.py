from django.urls import path
from . import views

app_name = "notes"
urlpatterns = [
    path("", views.home, name="home"),
    path("login/",views.validate, name="validate"),
    path("register/",views.register, name="register" ),
    path("verification/",views.loguin, name="login"),
    path("home/",views.home_user,name="home_user"),
    path("activities/",views.activities, name="activities"),
    path("documents/",views.documents, name="documents"),
    path("notes/",views.notes, name="notes"),
    path("activities/update",views.edit_activities, name="activities_update"),
    
]
