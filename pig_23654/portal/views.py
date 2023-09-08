from django.http import HttpResponse
from django.template import loader
from datetime import datetime
from django.shortcuts import render

# Create your views here.
def indice(request):
    # mi_template = loader.get_template("index.html")
    # contexto = {"ahora" : datetime.now() }
    # template_renderizado = mi_template.render(contexto, request)
    # respuesta = HttpResponse(template_renderizado)
    # return respuesta
    return render(request, "portal\index.html", {"ahora": datetime.now})


def cursos(request, inicio):

    prueba = request
    return HttpResponse(f"<b>TODOS LOS CURSOS desde el </b> {inicio}", status=500)

