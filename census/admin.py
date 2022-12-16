from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Padron)
class PadronAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Identificadores", {
            "fields": ("CIC", "CURP")
        }),
        ("Datos Personales", {
            "fields": ("Nombre", "ApPaterno", "ApMaterno", "FechaNacimiento", "Genero")
        }),
        ("Datos de Contacto", {
            "fields": ("Correo", "Telefono")
        }),
        ("Datos de Domicilio", {
            "fields": ("Municipio", "Estado", "CP")
        }),
        ("Informacion de Seguridad", {
            "fields": ("Q1", "Ans1", "Q2", "Ans2", "Q3", "Ans3")
        }),
        ("Informacion Biométrica", {
            "fields": ("Rostro1", "Rostro2", "Rostro3")
        }),
        )

admin.site.register(Locations)