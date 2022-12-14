from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.hashers import check_password
from .models import *


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget = forms.widgets.TextInput(attrs={
                'class': 'username-field form-control form-control-lg',
                "placeholder": "Usuario"
            })
        self.fields['password'].widget = forms.widgets.PasswordInput(attrs={
                'class': 'password-field form-control form-control-lg',
                "placeholder": "Contraseña"
            })

class Empadronamiento(forms.Form):
    
    cic = forms.CharField(  max_length = 9, 
                            required = True, 
                            label = "CIC", 
                            widget = forms.TextInput(attrs = {
                                "class": "form-text-field"
                                }
                            ))

    curp = forms.CharField( max_length = 18, 
                            required = True, 
                            label = "CURP",
                            widget = forms.TextInput(attrs = {
                                "class": "form-text-field"
                                }
                            ))

    name = forms.CharField( max_length = 40, 
                            required = True, 
                            label = "Nombre(s)",
                            widget = forms.TextInput(attrs = {
                                "class": "form-text-field"
                                }
                            ))

    lastName = forms.CharField( max_length = 40, 
                                required = True, 
                                label = "Apellido Paterno",
                                widget = forms.TextInput(attrs = {
                                    "class": "form-text-field"
                                    }
                                ))

    momLastName = forms.CharField(  max_length = 40, 
                                    required = True, 
                                    label = "Apellido Materno",
                                    widget = forms.TextInput(attrs = {
                                        "class": "form-text-field"
                                        }
                                    ))
                                    
    birthDate = forms.CharField(    max_length = 10, 
                                    required = True, 
                                    label = "Fecha de Nacimiento",
                                    widget = forms.TextInput(attrs = {
                                        "class": "form-date-field"
                                        }
                                    ))

    email = forms.EmailField(   required = True, 
                                label = "Correo Electronico",
                                widget = forms.TextInput(attrs = {
                                    "class": "form-email-field"
                                    }
                                ))

    phoneNumber = forms.CharField(  max_length = 10, 
                                    required = True, 
                                    label = "Numero Telefonico",
                                    widget = forms.TextInput(attrs = {
                                            "class": "form-text-field"
                                        }
                                    ))

    postalCode = forms.IntegerField(    max_value=99999,
                                        required = True, 
                                        label = "Codigo Postal",
                                        widget = forms.TextInput(attrs = {
                                            "class": "form-text-field"
                                            }
                                        ))

    town = forms.ChoiceField(   required = True, 
                                label = "Municipio",
                                choices=(("E", "E"),),
                                widget = forms.Select(attrs = {
                                    "class": "form-list-field"
                                    }
                                ))

    estate = forms.ModelChoiceField( required = True, 
                                label = "Estado",
                                queryset = Locations.objects.all(),
                                widget = forms.Select(attrs = {
                                    "class": "form-list-field"
                                    }
                                ))

    gender = forms.ChoiceField( required = True,
                                label = "Genero",
                                choices=(("MaleG", "M"), ("FemaleG", "F")),
                                widget = forms.Select(attrs = {
                                    "class": "form-list-field"
                                    }
                                ))

    secQuestion1 = forms.ChoiceField( required = True,
                                      label = "Pregunta de Seguridad 1",
                                      choices=(("E", "E"),),
                                      widget = forms.Select(attrs = {
                                          "class": "form-list-field"
                                          }
                                      ))

    secAns1 = forms.CharField(  max_length = 20, 
                                required = True, 
                                label = "Respuesta a Pregunta de Seguridad 1",
                                widget = forms.TextInput(attrs = {
                                    "class": "form-text-field"
                                    }
                                ))

    secQuestion2 = forms.ChoiceField(   required = True, 
                                        label = "Pregunta de Seguridad 2",
                                        choices=(("E", "E"),),
                                        widget = forms.Select(attrs = {
                                            "class": "form-list-field"
                                            }
                                        ))

    secAns2 = forms.CharField(  max_length = 20, 
                                required = True, 
                                label = "Respuesta a Pregunta de Seguridad 2",
                                widget = forms.TextInput(attrs = {
                                    "class": "form-text-field"
                                    }
                                ))

    secQuestion3 = forms.ChoiceField(   required = True, 
                                        label = "Pregunta de Seguridad 3",
                                        choices=(("E", "E"),),
                                        widget = forms.Select(attrs = {
                                            "class": "form-list-field"
                                            }
                                        ))

    secAns3 = forms.CharField(  max_length = 20, 
                                required = True, 
                                label = "Respuesta a Pregunta de Seguridad 3",
                                widget = forms.TextInput(attrs = {
                                    "class": "form-text-field"
                                    }
                                ))

    biometricalFace = forms.FileInput()

    def clean_phoneNumber(self):
        print(type(self.cleaned_data))
        phoneNumber = self.cleaned_data.get("phoneNumber")
        print(phoneNumber)

        if len(phoneNumber) != 10:
            raise forms.ValidationError("El numero telefonico debe ser de 10 caracteres...")
        
        return phoneNumber
    



