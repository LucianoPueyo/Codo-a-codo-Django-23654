# from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseServerError
from django.urls import reverse
from django.shortcuts import render


def index(request):
    # Faltaba agregar articles a INSTALLED_APPS en settings
    return render(request, "index.html")
    # return HttpResponse("Pagina de bienvenida")


# Create your views here.
def special_case_2003(request):
    return HttpResponse("Caso especial del 2003")


def year_archive(request, year):
    response = HttpResponse(f"Archivos el año {year}")
    if year == 2028:
        url = reverse("index")
        response = HttpResponseRedirect(url)
    elif year == 2029:
        response = HttpResponseServerError("CUalquier cosa")

    return response


def month_archive(request, year, month):

    return HttpResponse(f"Archivos del mes {month} del año {year}")


def article_detail(request, year, month, slug):
    return HttpResponse(f"Detalle del archivo con slug '{slug}' del mes {month} del año {year}")