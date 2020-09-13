from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('paises',views.PaisView)
router.register('cursos',views.CursoView)
router.register('alumnos',views.AlumnoView)
router.register('facultades',views.FacultadView)

urlpatterns = [
    path('',include(router.urls))
]
