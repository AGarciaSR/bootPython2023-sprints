from django.urls import path
from . import views

urlpatterns = [
    path('welcome', views.welcome, name='welcome'),
    path('nueva_tarea', views.nueva_tarea, name='nueva_tarea'),
    path('tarea_detail/<int:id>', views.tarea_detail, name='tarea_detail'),
    path('completa_tarea/<int:id>', views.completa_tarea, name='completa_tarea'),
    path('edita_tarea/<int:id>', views.editar_tarea, name='edita_tarea'),
    path('elimina_tarea/<int:id>', views.elimina_tarea, name='elimina_tarea')
]