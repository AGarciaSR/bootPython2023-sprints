import datetime
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Prioridad(models.Model):
    priority = models.IntegerField(null=False, blank=True, primary_key=True)
    name = models.CharField(max_length=80, null=False)
    
    def __str__(self):
        return self.name
    
    
# Create your models here.
class Tarea(models.Model):
    class Etiqueta(models.TextChoices):
        TRABAJO = "Trabajo", "Trabajo"
        PERSONAL = "Personal", "Personal"
        ESTUDIO = "Estudio", "Estudio"
    user_id = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE)
    nombre = models.CharField(max_length=400, null=False)
    descripcion = models.TextField()
    etiqueta = models.CharField(choices=Etiqueta.choices, null=True)
    prioridad = models.ForeignKey(Prioridad, related_name="prioridad", null=True, on_delete=models.SET_NULL)
    fecha_origen = models.DateField(default=datetime.date.today, editable=False)
    fecha_limite = models.DateField(null=True)
    completada = models.BooleanField()
    fecha_completada = models.DateField(blank=True, null=True,auto_now_add=False)
    observacion = models.TextField(null=True)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        ordering = ["fecha_limite", "prioridad"]