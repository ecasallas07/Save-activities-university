from django.db import models


class User(models.Model):
    ACTIVO = 'activo'
    DESACTIVADO = 'desactivado'
    
    ESTADO_CHOICES = [
        (ACTIVO, 'Activo'),
        (DESACTIVADO, 'Desactivado'),
    ]
        
    user_name = models.CharField(max_length=90)
    user_email = models.CharField(max_length=100,unique=True,blank=True)
    user_university = models.CharField(max_length=70)
    user_carrer = models.CharField(max_length=80)
    user_graduated = models.DateField()
    # user_password = models.
    user_status = models.CharField(max_lenght=20,choices=ESTADO_CHOICES,deault=ACTIVO)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
class Activities(models.Model):
    ALTA = 'Alta'
    MEDIA = 'Media'
    BAJA = 'Baja'
    
    PRIORITY_CHOICES = [
        (ALTA, 'Alta'),
        (MEDIA, 'Media'),
        (BAJA, 'Baja'),
    ]
    
    
    act_name = models.CharField(max_length=200)
    act_date_delivery = models.DateTime()
    act_score = models.IntegerField(default=00)
    act_priority = models.CharField(max_lenght=20,choices=PRIORITY_CHOICES,default=MEDIA)
    act_description = models.TextField(max_length=255)
    
    
    
    
    
    