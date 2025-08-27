from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=100)
    #creamos descripcion mas larga
    description = models.TextField(blank=True) #blank = true: si es vacia se guarda asi
    created = models.DateTimeField(auto_now_add=True) #fecha por defecto
    datecompleted = models.DateTimeField(null=True, blank=True) #vacio inicialmente
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    #devuelve el titulo como el nombre del objeto
    def __str__(self):
        return self.title +" by - " + self.user.username
    