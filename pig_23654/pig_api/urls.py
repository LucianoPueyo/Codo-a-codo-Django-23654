from django.urls import path, include
from rest_framework.routers import DefaultRouter
from pig_api import views

mi_router = DefaultRouter()
mi_router.register('categorias', views.CategoriaViewSet, basename='categoria')


urlpatterns = [
    path('', include(mi_router.urls)),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework'))    
]
