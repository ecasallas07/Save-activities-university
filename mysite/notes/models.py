from django.db import models


class UserTable(models.Model):
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
    user_password = models.CharField(max_length=20)
    user_status = models.CharField(max_length=20,choices=ESTADO_CHOICES,default=ACTIVO)
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
    act_date_delivery = models.DateTimeField()
    act_score = models.IntegerField(default=00)
    act_priority = models.CharField(max_length=20,choices=PRIORITY_CHOICES,default=MEDIA)
    act_description = models.TextField(max_length=255)
    act_category = models.CharField(max_length=255, default='undefined')
    act_user = models.ForeignKey(UserTable,on_delete=models.CASCADE,default=1)
    
class Documents(models.Model):
    
    docu_title = models.CharField(max_length=255)
    docu_description = models.TextField(max_length=255)
    docu_link = models.TextField(max_length=255)
    docu_file = models.FileField(upload_to='documents/')
    docu_image = models.FileField(upload_to='images/')
    create_at = models.DateTimeField(auto_now_add=True)
    docu_user = models.ForeignKey(UserTable,on_delete=models.CASCADE,default=1)
    
