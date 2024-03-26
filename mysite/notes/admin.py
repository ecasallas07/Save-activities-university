from django.contrib import admin
from .models import User, Activities


# Registra los modelos en el interfaz admin de django
# crear el usuario para admin --> python manage.py createsuperuser

admin.site.register(User)
admin.site.register(Activities)

