"""
URL configuration for pig_23654 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name="indice"),
    path('cursos/<int:inicio>', views.cursos, name="cursos"),
    path('proyectos/', views.proyectos, name="proyectos"),
    path('json_proyectos/', views.json_proyectos, name="json_proyectos"),
    path('quienes_somos/', views.quienes_somos, name="quienes_somos"),
	#autenticacion
    path('cuentas/registrarse', views.pig_registrarse, name='registrarse'),
    # path('cuentas/login', views.pig_login, name='login'),
    # path('cuentas/logout/',
    #      auth_views.LogoutView.as_view(template_name='portal/index.html'), name='logout'),
    #por defecto de django    
    # path('accounts/login/', auth_views.LoginView.as_view(
    #         template_name='portal/login.html',
    #         extra_context={'variable':'EXTRA CONTENT'},
    #     )),
    # path('accounts/logout/',
    #      views.PigLogoutView.as_view(), name='logout'),
    # path('accounts/password_change/', auth_views.PasswordChangeView.as_view(success_url="/"), name='password_change'), 
    path('accounts/', include('django.contrib.auth.urls')),
]
