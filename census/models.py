from django.db import models

# Create your models here.
class Padron(models.Model):
    CIC = models.CharField(max_length=9, primary_key=True, unique=True)
    CURP = models.CharField(max_length=18)
    Nombre = models.CharField(max_length=40)
    ApPaterno = models.CharField(max_length=40)
    ApMaterno = models.CharField(max_length=40)
    FechaNacimiento = models.CharField(max_length = 10)
    Correo = models.CharField(max_length=20)
    Telefono = models.CharField(max_length=20)
    CP = models.IntegerField()
    Municipio = models.CharField(max_length=40)
    Estado = models.CharField(max_length=40)
    Genero = models.CharField(max_length=2)
    Q1 = models.CharField(max_length=80)
    Ans1 = models.CharField(max_length=20)
    Q2 = models.CharField(max_length=80)
    Ans2 = models.CharField(max_length=20)
    Q3 = models.CharField(max_length=80)
    Ans3 = models.CharField(max_length=20)
    Rostro = models.CharField(max_length=256)