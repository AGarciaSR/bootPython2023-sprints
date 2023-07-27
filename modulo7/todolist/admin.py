from django.contrib import admin
from todolist.models import Tarea, Prioridad

# Register your models here.
admin.site.register(Tarea)
admin.site.register(Prioridad)