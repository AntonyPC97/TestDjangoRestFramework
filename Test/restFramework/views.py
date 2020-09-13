
from rest_framework import viewsets
from .models import Alumno,Curso,Pais,Facultad
from .serializers import AlumnoSerializer,CursoSerializer,PaisSerializer,FacultadSerializer

# Create your views here.

class PaisView(viewsets.ModelViewSet):
    queryset = Pais.objects.all()
    serializer_class = PaisSerializer

class CursoView(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class AlumnoView(viewsets.ModelViewSet):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer

class FacultadView(viewsets.ModelViewSet):
    queryset = Facultad.objects.all()
    serializer_class = FacultadSerializer