from django.shortcuts import render, redirect
from administracion.models import Categoria
from administracion.forms import CategoriaForm
from django.views.generic import ListView


# Create your views here.
def index_administracion(request):
    variable = 'No inspirarse en este proyecto ;)'
    return render(request, 'administracion/index.html', {'variable': variable})



class CategoriaListView(ListView):
    # template_name = "administracion/categorias/index.html"
    model = Categoria



# # Create your views here.
# def categorias_index(request):
#     # queryset
#     categorias = Categoria.objects.filter(baja=False)

#     if 'nombre' in request.GET:
#         categorias = categorias.filter(nombre__contains=request.GET['nombre'])
#     return render(request, 'administracion/categorias/index.html', {'categorias': categorias})





def categorias_nuevo(request):
    if request.method == "POST":
        formulario = CategoriaForm(request.POST)
        if formulario.is_valid():
            nombre_cleaned = formulario.cleaned_data['nombre']
            nueva_categoria = Categoria(nombre=nombre_cleaned)
            try:
                que_retorna = nueva_categoria.save()
            except ValueError as ve:
                formulario.add_error('nombre', str(ve))
            else:
                return redirect('categorias_index')
    else:
        formulario = CategoriaForm()
    return render(request, 'administracion/categorias/nuevo.html', {'form': formulario})
   

def categorias_editar(request, id_categoria):
    try:
        categoria = Categoria.objects.get(pk=id_categoria)
    except Categoria.DoesNotExist:
        return render(request, 'administracion/404_admin.html')

    if (request.method == 'POST'):
        formulario = CategoriaForm(request.POST)
        if formulario.is_valid():
            categoria.nombre = formulario.cleaned_data['nombre']
            categoria.save()
            return redirect('categorias_index')
    else:
        formulario = CategoriaForm(initial={'nombre': categoria.nombre})
    return render(request, 'administracion/categorias/editar.html', {'form': formulario})


def categorias_eliminar(request, id_categoria):
    try:
        categoria = Categoria.objects.get(pk=id_categoria)
        categoria.soft_delete()
    except Categoria.DoesNotExist:
        return render(request, 'administracion/404_admin.html')
    
    return redirect('categorias_index')

