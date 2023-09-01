from django.http import HttpResponse


# Create your views here.
def indice(request):
    respuesta = HttpResponse("Estoy re aprendiendo Django")
    return respuesta


def cursos(request, inicio):

    prueba = request

    return HttpResponse(f"<b>TODOS LOS CURSOS desde el </b> {inicio}", status=500)
