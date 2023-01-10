from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("", views.home, name = "home"), 
    path("login", views.log_in, name='login'),
    path("empadron/logout", views.log_out, name = "logout"),

    path("empadron", views.empadron, name = "empadron"),

    path("voting-sheet", views.votingSheet, name = "voting-sheet"),
    path("voting-sheet/history", views.votingSheet_history, name = "voting-sheet-history"),

    path("voting-sheet/generate", views.votingSheet_generate, name = "voting-sheet-generate"),
    path("voting-sheet/fill/<str:id_sheet>", views.votingSheet_fill, name = "voting-sheet-fill"),
    path("voting-sheet/candidates/<str:id_sheet>", views.votingSheet_candidates, name = "voting-sheet-candidates"),

    path("voting-sheet/validate", views.votingSheet_validate, name = "voting-sheet-validate"),
    

    path('ajax/load-towns/', views.load_towns, name='ajax_load_towns'), # AJAX

    
]