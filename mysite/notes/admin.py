from django.contrib import admin
from .models import UserTable, Activities


# Registra los modelos en el interfaz admin de django
# crear el usuario para admin --> python manage.py createsuperuser

admin.site.register(UserTable)
admin.site.register(Activities)

