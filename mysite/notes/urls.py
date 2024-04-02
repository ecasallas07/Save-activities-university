from django.urls import path
from . import views

app_name = "notes"
urlpatterns = [
    path("", views.home, name="home"),
    path("login/",views.validate, name="validate"),
    path("register/",views.register, name="register" ),
    path("login/",views.login, name="login")

]
