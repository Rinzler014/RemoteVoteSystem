from django.shortcuts import render
from django.contrib.auth import logout, login
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import *
from .models import *


# Create your views here.

@login_required(login_url="/")
def empadron(request):

    if request.user.is_authenticated:

        empadron_form = Empadronamiento(request.POST, request.FILES or None)
        context = {
            "title": "Empadronamiento de Usuarios",
            "form": empadron_form
        }
        

        if empadron_form.is_valid():
            print("FORM VALID!")

            data = empadron_form.cleaned_data

            Padron.objects.create(
                cic = data["cic"],
                curp = data["curp"],
                name = data["name"],
                lastName = data["lastName"],
                momLastName = data["momLastName"],
                birthDate = data["birthDate"],
                email = data["email"],
                phoneNumber = data["phoneNumber"],
                postalCode = data["postalCode"],
                town = data["town"],
                estate = data["state"],
                gender = data["gender"],
                secQuest1 = data["secQuestion1"],
                secAns1 = data["secAns1"],
                secQuest2 = data["secQuestion2"],
                secAns2 = data["secAns2"],
                secQuest3 = data["secQuestion3"],
                secAns3 = data["secAns3"],
                faceImage1 = data["faceImage1"],
                faceImage2 = data["faceImage2"],
                faceImage3 = data["faceImage3"],
            )

            return redirect("empadron")
        
    
        return render(request, "empadron/form.html", context)
    
    else:
        messages.error(request, "Usuario no Autenticado")
        return redirect("login")


def log_in(request):

    if request.user.is_authenticated:
        return redirect("empadron")

    if request.method == 'POST':
        form = AuthenticationForm(request = request, data = request.POST)

        if form.is_valid():
            user = authenticate(
                username = form.cleaned_data["username"],
                password = form.cleaned_data["password"]
            )

            if user is not None:
                login(request, user)
                messages.success(request, f"Inicio de Sesion Correcto!")
                return redirect("empadron")
        
        else:
            messages.error(request, "Usuario o Contraseña Incorrectos. Los campos son sensibles a mayusculas o minusculas")
    
    form = LoginForm()

    return render(
        request,
        template_name="empadron/login.html",
        context={
            "form" : form
        }
    )


@login_required(login_url="/")
def log_out(request):
    
    logout(request)
    messages.info(request, "Cierre de Sesion Exitoso")
    return render(request, "empadron/logout.html")
            