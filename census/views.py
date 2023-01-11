from django.shortcuts import render
from django.contrib.auth import logout, login
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse
from django.forms import formset_factory
from bson import ObjectId
import utils
from .forms import *
from .models import *

# Create your views here.

db = utils.get_db_handle("mongodb://localhost:27017", "election")


# Home
def home(request):

    '''
    db = utils.get_db_handle("mongodb://localhost:27017", "election")
    electionDB = db["vote_sheets"]

    electionDB.insert_one({
        "startDate": "2023/06/06",
        "endDate": "2023/06/08",
        "electionName": "Eleccion de Presidente",
        "electionType": "Presidencial",
        "electionStatus": "Activa",
        "electionDescription": "Eleccion de Presidente de la Republica Mexicana",
        "electionCandidates": [{

                "candidateName": "Andres Manuel Lopez Obrador",
                "candidateParty": "Morena",
                "candidateDescription": "Candidato a la Presidencia de la Republica Mexicana", 
                
                }],
    })
    '''
    
    return render(request, "empadron/home.html")

# /////////// Core Views ///////////

@login_required(login_url="/")
def empadron(request):

    if request.method == "POST":

        if request.user.is_authenticated:

            empadron_form = Empadronamiento(request.POST, request.FILES)
            context = {
                "title": "Empadronamiento de Usuarios",
                "form": empadron_form
            }

            if empadron_form.is_valid():
                print("FORM VALID!")

                data = empadron_form.cleaned_data

                print(data)

                Padron.objects.create(
                    cic = data["cic"],
                    curp = data["curp"],
                    name = data["name"],
                    lastName = data["lastName"],
                    momLastName = data["momLastName"],
                    birthDate = data["birthDate"],
                    mail = data["mail"],
                    phoneNumber = data["phoneNumber"],
                    postalCode = data["postalCode"],
                    town = data["town"],
                    state = data["state"],
                    gender = data["gender"],
                    secQuestion1 = data["secQuestion1"],
                    secAns1 = data["secAns1"],
                    secQuestion2 = data["secQuestion2"],
                    secAns2 = data["secAns2"],
                    secQuestion3 = data["secQuestion3"],
                    secAns3 = data["secAns3"],
                    faceImage1 = request.FILES["faceImage1"],
                    faceImage2 = request.FILES["faceImage2"],
                    faceImage3 = request.FILES["faceImage3"],
                )

                return redirect("empadron")
            
        
            return render(request, "empadron/form.html", context)
    
    else:
        empadron_form = Empadronamiento()
        context = {
            "title": "Empadronamiento de Usuarios",
            "form": empadron_form
        }

        return render(request, "empadron/form.html", context)

@login_required(login_url="/")
def votingSheet(request):
    return render(request, "votingSheet/menu.html")


@login_required(login_url="/")
def votingSheet_generate(request):

    if request.method == "POST":
    
            votingSheet_form = VoteSheetsCreate(request.POST)
            context = {
                "form": votingSheet_form
            }

            # print(votingSheet_form.is_valid())

            # print(votingSheet_form.cleaned_data)

            if votingSheet_form.is_valid():
                print("FORM VALID!")

                electionDB = db["vote_sheets"]

                data = votingSheet_form.cleaned_data

                votingSheet_form.cleaned_data["electionDateStart"] = votingSheet_form.cleaned_data["electionDateStart"].strftime("%Y/%m/%d")
                votingSheet_form.cleaned_data["electionDateEnd"] = votingSheet_form.cleaned_data["electionDateEnd"].strftime("%Y/%m/%d")

                votingSheet_form.cleaned_data["electionTimeStart"] = votingSheet_form.cleaned_data["electionTimeStart"].strftime("%H:%M")
                votingSheet_form.cleaned_data["electionTimeEnd"] = votingSheet_form.cleaned_data["electionTimeEnd"].strftime("%H:%M")

                sheet = electionDB.insert_one(data)

                return redirect('voting-sheet-fill', id_sheet = str(sheet.inserted_id))

            return render(request, "votingSheet/voting_sheets_generate.html", context)
                                   
    else:
        votingSheet_form = VoteSheetsCreate()
        context = {
            "form": votingSheet_form
        }

        return render(request, "votingSheet/voting_sheets_generate.html", context)

@login_required(login_url="/")
def votingSheet_fill(request, id_sheet):

    electionDB = db["vote_sheets"]
    sheet = electionDB.find_one({"_id": ObjectId(id_sheet) })
    candidates = sheet["electionCandidatesNumber"]

    fillFormSet = formset_factory(VoteSheetsFill, extra=candidates)
    formSet = fillFormSet()

    context = {
        "formSet": formSet,
        "sheet_id": id_sheet,
        "candidates": candidates,
    }

    if request.method == "POST":

        formSet = fillFormSet(request.POST)

        context = {
            "formSet": formSet,
            "sheet_id": id_sheet,
            "candidates": candidates,
        }

        if formSet.is_valid():
            print("FORM VALID!")
            for form in formSet:
                print(form.cleaned_data)

    return render(request, "votingSheet/voting_sheets_fill.html", context)
    


@login_required(login_url="/")
def votingSheet_candidates(request):
    pass

@login_required(login_url="/")
def votingSheet_validate(request):
    pass

@login_required(login_url="/")
def votingSheet_history(request):
    
    if request.method == "POST":
    
            if request.user.is_authenticated:
    
                votingSheet_form = VoteSheetsChecker(request.POST)
                context = {
                    "form": votingSheet_form
                }
    
                if votingSheet_form.is_valid():
                    print("FORM VALID!")
                    data = votingSheet_form.cleaned_data  

                    context = {
                        # vote sheet id and other fields to pass to other page
                    }
                
                return render(request, "votingSheet/history_sheets.html", context)
        
    else:
        votingSheet_form = VoteSheetsChecker()
        context = {
            "form": votingSheet_form
        }

        return render(request, "votingSheet/history_sheets.html", context)


# /////////// Login Views ///////////

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

# /////////// AJAX Views ///////////            

def load_towns(request):
    state_id = request.GET.get('state')
    towns = Town.objects.filter(state_id = state_id).order_by('town')
    return render(request, "empadron/towns_dropdown.html", {'towns': towns})