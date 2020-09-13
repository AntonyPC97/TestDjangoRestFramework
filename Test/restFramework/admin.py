from django.contrib import admin
from .models import Curso,Pais,Alumno,Facultad

# Register your models here.
admin.site.register(Curso)
admin.site.register(Alumno)
admin.site.register(Pais)
admin.site.register(Facultad)
