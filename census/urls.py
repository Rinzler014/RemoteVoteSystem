from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [   
    path("", views.log_in, name='login'),
    path("empadron", views.empadron, name = "empadron"),
    path("empadron/logout", views.log_out, name = "logout"),
]