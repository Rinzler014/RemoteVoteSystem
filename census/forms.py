from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.hashers import check_password
import datetime
from django.contrib import messages
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

        if "state" in self.data:
            try:
                state = int(self.data.get("state"))
                self.fields["town"].queryset =  Town.objects.filter(state_id = state)
            
            except (ValueError, TypeError):
                pass

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

    electionName = forms.ChoiceField( required = True,
                                    label="Nombre de la Eleccion",
                                    choices = (("E03", "Municipal"), ("E02", "Guvernamental"), ("E01", "Presidencial")),
                                    widget=forms.Select(attrs={
                                        "class" : "form-control",
                                        "onchange" : "disableFields()"
                                        }
                                    ))

    govermentPeriodStart = forms.IntegerField( required = True,
                                    label = "Periodo de Gobierno",
                                    widget = forms.NumberInput(attrs = {
                                        "class": "form-control",
                                        "type": "number",
                                        "min": "2023",
                                        "max": "2099",
                                        "step": "1",
                                        "value": "2023"
                                        }
                                    ))

    govermentPeriodEnd = forms.IntegerField( required = True,
                                    label = "Periodo de Gobierno",
                                    widget = forms.NumberInput(attrs = {
                                        "class": "form-control",
                                        "type": "number",
                                        "min": "2023",
                                        "max": "2099",
                                        "step": "1",
                                        "value": "2023"
                                        }
                                    ))

    electionState = forms.ModelChoiceField( required = False,
                                            label = "Estado",
                                            queryset = State.objects.all(),
                                            widget = forms.Select(attrs = {
                                                "class": "form-control"
                                                }
                                            ))

    electionTown = forms.ModelChoiceField(   required = False,
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
                    
    electionTimeEnd = forms.TimeField( required = True,
                                label = "Hora de finalizacion de la Eleccion",
                                widget = forms.TimeInput(attrs = {
                                    "class": "form-control",
                                    "type": "time"

                                    }
                                ))

    electionCandidatesNumber = forms.IntegerField( required = True,
                                                    label= "Numero de Candidatos",
                                                    widget= forms.NumberInput(attrs = {
                                                        "class" : "form-control",
                                                        "type" : "number"
                                                    }
                                                ))
    
    def clean(self):

        cleaned_data = super().clean()

        electionDateStart = cleaned_data.get("electionDateStart")
        electionDateEnd = cleaned_data.get("electionDateEnd")
        govermentPeriodStart = cleaned_data.get("govermentPeriodStart")
        govermentPeriodEnd = cleaned_data.get("govermentPeriodEnd")
        electionTimeStart = cleaned_data.get("electionTimeStart")
        electionTimeEnd = cleaned_data.get("electionTimeEnd")
        
        errors = []

        if electionDateStart > electionDateEnd:
            errors.append("La fecha de inicio de la eleccion debe ser menor a la fecha de fin de la eleccion")

        if govermentPeriodStart > govermentPeriodEnd or govermentPeriodStart == govermentPeriodEnd:
            errors.append("El inicio del periodo de gobierno debe ser mayor al fin del periodo de gobierno ")

        if electionTimeStart > electionTimeEnd:
            errors.append("La hora de inicio de la eleccion debe ser menor a la hora de fin de la eleccion")
        
        if errors:
            raise forms.ValidationError(errors)
                    
        return cleaned_data

    def clean_electionState(self):

        if self.cleaned_data.get("electionState") == None:
            return "N/A"
        else:
            return self.cleaned_data.get("electionState").state

    def clean_electionTown(self):

        if self.cleaned_data.get("electionTown") == None:
            return "N/A"
        else:
            return self.cleaned_data.get("electionTown").town

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["electionTown"].queryset = Town.objects.none() 


        if "electionState" in self.data:
            try:
                state = int(self.data.get("electionState"))
                self.fields["electionTown"].queryset =  Town.objects.filter(state_id = state)
            
            except (ValueError, TypeError):
                pass


class VoteSheetsFill(forms.Form):

   candidateName = forms.CharField( required = True,
                                    label = "Nombre del Candidato",
                                    widget = forms.TextInput(attrs = {
                                        "class": "form-control",
                                        "type": "text"
                                        }
                                    ))
    
   substituteCandidateName = forms.CharField( required = True,
                                    label = "Nombre del Candidato Suplente",
                                    widget = forms.TextInput(attrs = {
                                        "class": "form-control",
                                        "type": "text"
                                        }
                                    ))

   candidateParty = forms.ModelMultipleChoiceField( required = True,
                                    label = "Partido Politico o Alianza",
                                    queryset= PoliticalParty.objects.all(),
                                    widget = forms.Select(attrs = {
                                        "class": "form-control"
                                        }
                                    ))


    

