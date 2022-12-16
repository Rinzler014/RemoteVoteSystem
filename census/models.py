from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.contrib.auth.forms import AuthenticationForm

# Create your models here.

class Padron(models.Model):
    cic = models.CharField(max_length=9, primary_key=True, unique=True)
    curp = models.CharField(max_length=18)
    name = models.CharField(max_length=40)
    lastName = models.CharField(max_length=40)
    momLastName = models.CharField(max_length=40)
    birthDate = models.CharField(max_length = 10)
    email = models.CharField(max_length=20)
    phoneNumber = models.CharField(max_length=20)
    postalCode = models.IntegerField()
    town = models.CharField(max_length=40)
    estate = models.CharField(max_length=40)
    gender = models.CharField(max_length=2)
    secQuest1 = models.CharField(max_length=80)
    secAns1 = models.CharField(max_length=20)
    secQuest2 = models.CharField(max_length=80)
    secAns2 = models.CharField(max_length=20)
    secQuest3 = models.CharField(max_length=80)
    secAns3 = models.CharField(max_length=20)
    faceImage1 = models.ImageField(upload_to='images/')
    faceImage2 = models.ImageField(upload_to='images/')
    faceImage3 = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.cic

class Locations(models.Model):
    state = models.CharField(max_length=50)
    code = models.CharField(max_length=3)
    def __str__(self):
        return self.state

class SecurityQuestions(models.Model):
    question = models.CharField(max_length=200)
