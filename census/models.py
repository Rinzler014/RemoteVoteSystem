from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.contrib.auth.forms import AuthenticationForm

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

    def __str__(self):
        return self.CIC

class Locations(models.Model):
    state = models.CharField(max_length=50)
    code = models.CharField(max_length=3)
    def __str__(self):
        return self.state

class SecurityQuestions(models.Model):
    question = models.CharField(max_length=200)
