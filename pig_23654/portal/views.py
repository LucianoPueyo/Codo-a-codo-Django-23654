from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.template import loader
from datetime import datetime
from django.shortcuts import render, redirect
from portal.forms import ContactoForm, RegistrarUsuarioForm
from administracion.models import Lenguaje
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView

# Create your views here.

    
def index(request):
    # mi_template = loader.get_template("index.html")
    # contexto = {"ahora" : datetime.now() }
    # template_renderizado = mi_template.render(contexto, request)
    # respuesta = HttpResponse(template_renderizado)
    # return respuesta

    formulario_contacto = None
    if request.method == 'GET':
        formulario_contacto = ContactoForm()
    elif request.method == 'POST':
        formulario_contacto = ContactoForm(request.POST)
        # # Acá hago todo lo que impacta en el sistema (envio de email, grabar datos, etc)
        if formulario_contacto.is_valid():
            messages.success(request, 'Hemos recibido tus datos')
            mensaje = f"De : {formulario_contacto.cleaned_data['nombre']} <{formulario_contacto.cleaned_data['email']}>\n Asunto: {formulario_contacto.cleaned_data['asunto']}\n Mensaje: {formulario_contacto.cleaned_data['mensaje']}"
            mensaje_html = f"""
                <p>De: {formulario_contacto.cleaned_data['nombre']} <a href="mailto:{formulario_contacto.cleaned_data['email']}">{formulario_contacto.cleaned_data['email']}</a></p>
                <p>Asunto:  {formulario_contacto.cleaned_data['asunto']}</p>
                <p>Mensaje: {formulario_contacto.cleaned_data['mensaje']}</p>
            """
            asunto = "CONSULTA DESDE LA PAGINA - " + \
                formulario_contacto.cleaned_data['asunto']
            send_mail(asunto, mensaje, settings.EMAIL_HOST_USER, [
                      settings.RECIPIENT_ADDRESS], fail_silently=False, html_message=mensaje_html)
        # else:
        #     messages.error(
        #         request, 'Por favor revisa los errores en el formulario')
    else:
        return HttpResponseBadRequest("Mandaste cualquiera")

    
    contexto = {
        'ahora':  datetime.now,
        'mi_formulario':  formulario_contacto,
        'lenguajes': Lenguaje.objects.all()
    }

    return render(request, "portal\index.html", contexto)


def cursos(request, inicio):

    listado_cursos = [
        {
            'nombre': 'Fullstack Java',
            'descripcion': 'Curso de Fullstack',
            'categoria': 'Programación',
            'portada': {
                'imagen': "https://vilmanunez.com/wp-content/uploads/2016/03/herramientas-y-recursos-para-crear-curso-online.png"
            }
        },
        {
            'nombre': 'Diseño UX/UI',
            'descripcion': 'Curso de Diseño',
            'categoria': 'Diseño',
            'portada': {
                'imagen': "https://vilmanunez.com/wp-content/uploads/2016/03/herramientas-y-recursos-para-crear-curso-online.png"
            }
        },
        {
            'nombre': 'Big Data',
            'descripcion': 'test',
            'categoria': 'Análisis de Datos',
            'portada': {
                'imagen': "https://vilmanunez.com/wp-content/uploads/2016/03/herramientas-y-recursos-para-crear-curso-online.png"
            }
        },
        {
            'nombre': 'Big Data Avanzado',
            'descripcion': 'test',
            'categoria': 'Análisis de Datos',
            'portada': {
                'imagen': "https://vilmanunez.com/wp-content/uploads/2016/03/herramientas-y-recursos-para-crear-curso-online.png"
            }
        },
    ]

    return render(request, "portal/cursos.html", {'cursos': listado_cursos})


def proyectos(request):
    return render(request, "portal/proyectos.html")


def json_proyectos(request,):
    proyectos = [{
        'autor': 'Gustavo Villegas',
        'portada': 'https://agenciadeaprendizaje.bue.edu.ar/wp-content/uploads/2021/12/Gustavo-Martin-Villegas-300x170.png',
        'url': 'https://marvi-artarg.web.app/'
    }, {
        'autor': 'Enzo Martín Zotti',
        'portada': 'https://agenciadeaprendizaje.bue.edu.ar/wp-content/uploads/2022/01/Enzo-Martin-Zotti-300x170.jpg',
        'url': 'https://hablaconmigo.com.ar/'
    }, {
        'autor': 'María Echevarría',
        'portada': 'https://agenciadeaprendizaje.bue.edu.ar/wp-content/uploads/2022/01/Maria-Echevarria-300x170.jpg',
        'url': 'https://compassionate-colden-089e8a.netlify.app/'
    },]
    response = {'status': 'Ok', 'code': 200,
                'message': 'Listado de proyectos', 'data': proyectos}
    return JsonResponse(response, safe=False)


def quienes_somos(request):
    return render(request, "portal/quienes_somos.html")


def pig_login(request):
    if request.method == 'POST':
        # AuthenticationForm_can_also_be_used__
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' Bienvenido/a {username} !!')
            return redirect('indice')
        else:
            messages.error(request, f'Cuenta o password incorrecto, realice el login correctamente')
    form = AuthenticationForm()
    return render(request, 'portal/login.html', {'form': form, 'title': 'Log in'})

def pig_registrarse(request):
    if request.method == 'POST':
        form = RegistrarUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            # email = form.cleaned_data.get('email')
            messages.success(
                request, f'Tu cuenta fue creada con éxito! Ya te podes loguear en el sistema.')
            return redirect('login')
    else:
        form = RegistrarUsuarioForm()
    return render(request, 'portal/registrarse.html', {'form': form, 'title': 'registrese aquí'})


class PigLogoutView(LogoutView):
    # next_page = 'inicio'

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.add_message(request, messages.INFO, 'Se ha cerrado la session correctamente.')
        return response