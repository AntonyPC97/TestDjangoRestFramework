from django.db import models

# Create your models here.

class Pais(models.Model):
    nombre = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre

class Facultad(models.Model):
    nombre= models.CharField(max_length=30)
    def __str__(self):
        return self.nombre

class Curso(models.Model):
    nombre = models.CharField(max_length=30)
    creditos = models.FloatField()
    facultad = models.ForeignKey(Facultad ,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.nombre

class Alumno(models.Model):
    nombre = models.CharField(max_length=50)
    codigo = models.CharField(max_length=8)
    cursos = models.ManyToManyField(Curso)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.nombre