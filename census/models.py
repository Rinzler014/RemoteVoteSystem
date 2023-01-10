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
    mail = models.CharField(max_length=20)
    phoneNumber = models.CharField(max_length=20)
    postalCode = models.IntegerField()
    town = models.CharField(max_length=40)
    state = models.CharField(max_length=40)
    gender = models.CharField(max_length=2)
    secQuestion1 = models.CharField(max_length=80)
    secAns1 = models.CharField(max_length=20)
    secQuestion2 = models.CharField(max_length=80)
    secAns2 = models.CharField(max_length=20)
    secQuestion3 = models.CharField(max_length=80)
    secAns3 = models.CharField(max_length=20)
    faceImage1 = models.ImageField(upload_to='images/')
    faceImage2 = models.ImageField(upload_to='images/')
    faceImage3 = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.cic

class State(models.Model):
    state = models.CharField(max_length=50)
    code = models.IntegerField()
    def __str__(self):
        return self.state 

class Town(models.Model):
    town = models.CharField(max_length=50)
    code = models.CharField(max_length=4)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    def __str__(self):
        return self.town 

class SecurityQuestion(models.Model):
    question = models.CharField(max_length=200)
    def __str__(self):
        return self.question 

class PoliticalParty(models.Model):

    partyName = models.CharField(max_length=50)
    partyLogo = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.partyName
