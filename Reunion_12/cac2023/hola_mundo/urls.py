from django.urls import path
from . import views

urlpatterns = [
    path('saludo', views.saludo, name="saludo"),
]
