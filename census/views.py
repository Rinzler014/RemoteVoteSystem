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

        empadron_form = Empadronamiento(request.POST or None)
        context = {
            "title": "Empadronamiento de Usuarios",
            "form": empadron_form
        }

        if empadron_form.is_valid():
            print("FORM VALID!")
            print(empadron_form.cleaned_data)
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



    '''

    login_form = LoginEmpadronamiento(request.POST or None)
    context = {
        "title": "Acceso a Colaboradores",
        "form": login_form
    }

    if login_form.is_valid():
        print("LOGIN CORRECT!")
        request.session['forward'] = True
        return redirect("empadron", login_form.cleaned_data.get("username"))
    
    return render(request, "empadron/login.html", context)

    '''


@login_required(login_url="/")
def log_out(request):
    
    logout(request)
    messages.info(request, "Cierre de Sesion Exitoso")
    return render(request, "empadron/logout.html")
            