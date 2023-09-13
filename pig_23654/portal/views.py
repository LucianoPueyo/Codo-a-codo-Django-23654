from django.http import HttpResponse, JsonResponse
from django.template import loader
from datetime import datetime
from django.shortcuts import render

# Create your views here.


def index(request):
    # mi_template = loader.get_template("index.html")
    # contexto = {"ahora" : datetime.now() }
    # template_renderizado = mi_template.render(contexto, request)
    # respuesta = HttpResponse(template_renderizado)
    # return respuesta

    respuesta = None
    if request.method == 'POST':
        nombre = request.POST["nombre"]
        consulta = request.POST["consulta"]
        respuesta = f"Gracias <b> {nombre} </b> por tu consulta"

    return render(request, "portal\index.html", {"ahora": datetime.now, "respuesta": respuesta})


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
