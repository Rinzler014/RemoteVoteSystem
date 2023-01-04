from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("", views.home, name = "home"), 
    path("login", views.log_in, name='login'),
    path("empadron", views.empadron, name = "empadron"),

    path('ajax/load-towns/', views.load_towns, name='ajax_load_towns'), # AJAX

    path("empadron/logout", views.log_out, name = "logout"),
]