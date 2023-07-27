from django.shortcuts import redirect, render
from django.utils.timezone import localtime
from django.contrib.auth.models import User
from todolist.models import Tarea, Prioridad
from .forms import TareaFilter, TareaForm, TareaObservacion

# Create your views here.
def welcome(request):
    if request.method == "POST":
        form = TareaFilter(request.POST)
        if form.is_valid():
            tareas = Tarea.objects.only('id','nombre','descripcion','etiqueta').filter(user_id=request.user, nombre__icontains=form.cleaned_data["filtro"]).order_by('fecha_limite')
    else:
        tareas = Tarea.objects.only('id','nombre','descripcion','etiqueta').filter(user_id=request.user).order_by('fecha_limite')
        form = TareaFilter()
    context = {
        'tareas' : tareas,
        'form_filtro' : form
    }
    return render(request, "welcome.html", context)

def nueva_tarea(request):
    if request.method == "POST":
        form = TareaForm(request.POST)
        if form.is_valid():
            new_tarea = Tarea()
            new_tarea.user_id = User.objects.get(username=form.cleaned_data["user_designated"])
            new_tarea.nombre = form.cleaned_data["nombre"]
            new_tarea.descripcion = form.cleaned_data["descripcion"]
            new_tarea.etiqueta = form.cleaned_data["etiqueta"]
            new_tarea.prioridad = Prioridad.objects.get(name=form.cleaned_data["prioridad"])
            new_tarea.fecha_limite = form.cleaned_data["fecha_limite"]
            new_tarea.completada = False
            new_tarea.save()
            return redirect(welcome)
    else:
        form = TareaForm()
        context = {
            'form': form,
            'title': 'Añadiendo una nueva tarea',
            'cotitle': 'Añadir tarea'
        }
        return render(request, "nueva_tarea.html", context)

def editar_tarea(request, id):
    if request.method != "POST":
        tarea_detail = Tarea.objects.only('id','user_id','nombre','descripcion','etiqueta','prioridad', 'fecha_limite').get(id=id)
        form = TareaForm(initial={
            'nombre': tarea_detail.nombre,
            'descripcion': tarea_detail.descripcion,
            'etiqueta': tarea_detail.etiqueta,
            'prioridad': tarea_detail.prioridad,
            'fecha_limite': tarea_detail.fecha_limite,
            'user_designated': tarea_detail.user_id})
        context = {
            'form': form,
            'title': 'Editando tarea',
            'cotitle': 'Editar tarea'
        }
        return render(request, "nueva_tarea.html", context)
    else:
        form = TareaForm(request.POST)
        if form.is_valid():
            updated_tarea = Tarea.objects.all().get(id=id)
            updated_tarea.nombre = form.cleaned_data['nombre']
            updated_tarea.descripcion = form.cleaned_data['descripcion']
            updated_tarea.etiqueta = form.cleaned_data['etiqueta']
            updated_tarea.prioridad = form.cleaned_data['prioridad']
            updated_tarea.fecha_limite = form.cleaned_data['fecha_limite']
            updated_tarea.save()
        context = {
            'operacion' : "actualizado"
        }
        return redirect(welcome)

def elimina_tarea(request, id):
    Tarea.objects.filter(id=id).delete()
    return redirect(welcome)

def tarea_detail(request, id):
    if request.method == "POST":
        form = TareaObservacion(request.POST)
        if form.is_valid():
            tarea = Tarea.objects.get(id=id)
            tarea.observacion = form.cleaned_data["observacion"]
            tarea.save()
    else:
        tarea = Tarea.objects.get(id=id)
        form = TareaObservacion(initial={'observacion': tarea.observacion})
    context = {
        'tarea' : tarea,
        'form' : form
    }
    return render(request, "tarea_detail.html", context)

def completa_tarea(request, id):
    tarea = Tarea.objects.get(id=id)
    tarea.completada = True
    tarea.fecha_completada = localtime().date()
    tarea.save()
    context = {
        'tarea' : tarea
    }
    return render(request, "tarea_detail.html", context)