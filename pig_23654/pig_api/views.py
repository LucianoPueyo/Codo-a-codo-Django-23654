from django.shortcuts import render
from rest_framework import viewsets, permissions
from pig_api import serializers
from administracion.models import Categoria


# Create your views here.
class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = serializers.CategoriaSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]