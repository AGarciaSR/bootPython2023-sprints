from django import forms
from django.contrib.auth.models import User
from .models import Tarea, Prioridad

class TareaForm(forms.ModelForm):
    user_designated = forms.ModelChoiceField(label="Usuario designado", queryset=User.objects.all(), blank=True, required=True)
    nombre = forms.CharField(max_length=400)
    descripcion = forms.CharField(widget=forms.Textarea(attrs={"rows":"5"}))
    etiqueta = forms.ChoiceField
    prioridad = forms.ModelChoiceField(label="Prioridad", queryset=Prioridad.objects.all(), blank=True, required=True)
    fecha_limite = forms.DateField()
    
    class Meta:
        model = Tarea
        exclude = ['user_id', 'completada', 'fecha_completada', 'observacion']
        
class TareaFilter(forms.Form):
    filtro = forms.CharField(max_length=400)
    
class TareaObservacion(forms.Form):
    observacion = forms.CharField(widget=forms.Textarea(attrs={"rows":"5"}))