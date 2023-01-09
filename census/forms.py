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
                                "class": "form-control"
                                }
                            ))

    curp = forms.CharField( max_length = 18, 
                            required = True, 
                            label = "CURP",
                            widget = forms.TextInput(attrs = {
                                "class": "form-control"
                                }
                            ))

    name = forms.CharField( max_length = 40, 
                            required = True, 
                            label = "Nombre(s)",
                            widget = forms.TextInput(attrs = {
                                "class": "form-control"
                                }
                            ))

    lastName = forms.CharField( max_length = 40, 
                                required = True, 
                                label = "Apellido Paterno",
                                widget = forms.TextInput(attrs = {
                                    "class": "form-control"
                                    }
                                ))

    momLastName = forms.CharField(  max_length = 40, 
                                    required = True, 
                                    label = "Apellido Materno",
                                    widget = forms.TextInput(attrs = {
                                        "class": "form-control"
                                        }
                                    ))
                                    
    birthDate = forms.DateField(   
                                    required = True,
                                    label = "Fecha de Nacimiento",
                                    widget=forms.DateInput(attrs={
                                        "class" : "form-control",
                                        "type": "date"
                                    })
                                    )
                                    

    mail = forms.EmailField(   required = True, 
                                label = "Correo Electronico",
                                widget = forms.TextInput(attrs = {
                                    "class": "form-control",
                                    "type": "email"
                                    }
                                ))

    phoneNumber = forms.CharField(  max_length = 10, 
                                    required = True, 
                                    label = "Numero Telefonico",
                                    widget = forms.TextInput(attrs = {
                                            "class": "form-control"
                                        }
                                    ))

    postalCode = forms.IntegerField(    max_value=99999,
                                        required = True, 
                                        label = "Codigo Postal",
                                        widget = forms.TextInput(attrs = {
                                            "class": "form-control"
                                            }
                                        ))

    state = forms.ModelChoiceField( required = True, 
                                    label = "Estado",
                                    queryset = State.objects.all(),
                                    widget = forms.Select(attrs = {
                                        "class": "form-control"
                                        }
                                    ))

    town = forms.ModelChoiceField(   required = True, 
                                label = "Municipio",
                                queryset = Town.objects.filter().order_by('town'),
                                widget = forms.Select(attrs = {
                                    "class": "form-control",
                                    }
                                ))

    gender = forms.ChoiceField( required = True,
                                label = "Genero",
                                choices=(("MaleG", "M"), ("FemaleG", "F")),
                                widget = forms.Select(attrs = {
                                    "class": "form-control"
                                    }
                                ))

    secQuestion1 = forms.ModelChoiceField( required = True,
                                      label = "Pregunta de Seguridad 1",
                                      queryset = SecurityQuestion.objects.all(),
                                      widget = forms.Select(attrs = {
                                          "class": "form-control"
                                          }
                                      ))

    secAns1 = forms.CharField(  max_length = 20, 
                                required = True, 
                                label = "Respuesta a Pregunta de Seguridad 1",
                                widget = forms.TextInput(attrs = {
                                    "class": "form-control"
                                    }
                                ))

    secQuestion2 = forms.ModelChoiceField(   required = True, 
                                        label = "Pregunta de Seguridad 2",
                                        queryset = SecurityQuestion.objects.all(),
                                        widget = forms.Select(attrs = {
                                            "class": "form-control"
                                            }
                                        ))

    secAns2 = forms.CharField(  max_length = 20, 
                                required = True, 
                                label = "Respuesta a Pregunta de Seguridad 2",
                                widget = forms.TextInput(attrs = {
                                    "class": "form-control"
                                    }
                                ))

    secQuestion3 = forms.ModelChoiceField(   required = True, 
                                        label = "Pregunta de Seguridad 3",
                                        queryset = SecurityQuestion.objects.all(),
                                        widget = forms.Select(attrs = {
                                            "class": "form-control"
                                            }
                                        ))

    secAns3 = forms.CharField(  max_length = 20, 
                                required = True, 
                                label = "Respuesta a Pregunta de Seguridad 3",
                                widget = forms.TextInput(attrs = {
                                    "class": "form-control"
                                    }
                                ))

    faceImage1 = forms.ImageField(label = "Imagen Rostro Numero 1", widget=forms.FileInput(attrs={
                                        "class" : "form-control",
                                        "type": "file"
                                    }))

    faceImage2 = forms.ImageField(label = "Imagen Rostro Numero 2", widget=forms.FileInput(attrs={
                                        "class" : "form-control",
                                        "type": "file"
                                    }))

    faceImage3 = forms.ImageField(label = "Imagen Rostro Numero 3", widget=forms.FileInput(attrs={
                                        "class" : "form-control",
                                        "type": "file"
                                    }))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["town"].queryset = Town.objects.none()

    # VALIDATIONS

    def clean_cic(self):
        cic = self.cleaned_data.get("cic")

        if len(cic) != 9:
            raise forms.ValidationError("El CIC debe ser de 9 caracteres...")

        return cic


    def clean_curp(self):
        curp = self.cleaned_data.get("curp")

        if len(curp) != 18:
            raise forms.ValidationError("La CURP debe ser de 18 caracteres...")

        return curp

    
    def clean_phoneNumber(self):
        print(type(self.cleaned_data))
        phoneNumber = self.cleaned_data.get("phoneNumber")

        if len(phoneNumber) != 10:
            raise forms.ValidationError("El numero telefonico debe ser de 10 caracteres...")
        
        return phoneNumber
    
    
    def clean_postalCode(self):
        postalCode = self.cleaned_data.get("postalCode")

        if len(str(postalCode)) != 5:
            raise forms.ValidationError("El codigo postal debe ser de 5 caracteres...")
        
        return postalCode
    
class VoteSheetsChecker(forms.Form):

    voteSheetID = forms.CharField(max_length = 10,
                                    widget=forms.TextInput(attrs={
                                        "class" : "form-control",
                                    }))

    def clean_voteSheetID(self):
        voteSheetID = self.cleaned_data.get("voteSheetID")

        if len(voteSheetID) != 10:
            raise forms.ValidationError("El ID de la hoja de votacion debe ser de 10 caracteres...")

class VoteSheetsCreate(forms.Form):

    electionName = forms.CharField(max_length = 50,
                                    label="Nombre de la Eleccion",
                                    widget=forms.TextInput(attrs={
                                        "class" : "form-control",
                                        }
                                    ))

    govermentPeriodStart = forms.IntegerField( required = True,
                                    label = "Periodo de Gobierno",
                                    widget = forms.NumberInput(attrs = {
                                        "class": "form-control"
                                        }
                                    ))

    govermentPeriodEnd = forms.IntegerField( required = True,
                                    label = "Periodo de Gobierno",
                                    widget = forms.NumberInput(attrs = {
                                        "class": "form-control"
                                        }
                                    ))

    electionState = forms.ModelChoiceField( required = True,
                                            label = "Estado",
                                            queryset = State.objects.all(),
                                            widget = forms.Select(attrs = {
                                                "class": "form-control"
                                                }
                                            ))

    electionTown = forms.ModelChoiceField(   required = True,
                                            label = "Municipio",
                                            queryset = Town.objects.all(),
                                            widget = forms.Select(attrs = {
                                                "class": "form-control"

                                                }
                                            ))

    electionDateStart = forms.DateField( required = True,
                                    label = "Fecha de inicio la Eleccion",
                                    widget = forms.DateInput(attrs = {
                                        "class": "form-control",
                                        "type": "date"

                                        }
                                    ))

    electionDateEnd = forms.DateField(   required = True,
                                    label = "Fecha de fin de la Eleccion",
                                    widget = forms.DateInput(attrs = {
                                        "class": "form-control",
                                        "type": "date"

                                        }
                                    ))

    electionTimeStart = forms.TimeField( required = True,
                                    label = "Hora de inicio de la Eleccion",
                                    widget = forms.TimeInput(attrs = {
                                        "class": "form-control",
                                        "type": "time"

                                        }
                                    ))
                    
    electionTimeStart = forms.TimeField( required = True,
                                label = "Hora de finalizacion de la Eleccion",
                                widget = forms.TimeInput(attrs = {
                                    "class": "form-control",
                                    "type": "time"

                                    }
                                ))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["electionTown"].queryset = Town.objects.none()
    



