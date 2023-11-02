from django.contrib import admin
from administracion.models import Estudiante, Docente, Curso, Categoria, Proyecto, Comision, Inscripcion, Lenguaje

#permite mostrar y editar modelos relacionados en línea dentro de la interfaz de administración de otro modelo     
class InscripcionInline(admin.TabularInline):
    model = Inscripcion

#agregar la funcionalidad de creación de instancias de Inscripcion
class ComisionAdmin(admin.ModelAdmin):
    inlines = [
        InscripcionInline,
    ]

@admin.action(description="Método para recuperar a los alumnos seleccionados")
def recuperar(self, request, queryset):
    for alumno in queryset:
        alumno.restore()

class JuanCarlos(admin.ModelAdmin):
    list_display = ('dni', 'nombre', 'apellido')
    search_fields = ('apellido',)
    actions =  [recuperar,]
    inlines = [
        InscripcionInline,
    ]


# Registro por defecto en el admin de Django 
admin.site.register(Estudiante, JuanCarlos)
admin.site.register(Docente)
admin.site.register(Curso)
admin.site.register(Categoria)
admin.site.register(Proyecto)
admin.site.register(Comision, ComisionAdmin)
admin.site.register(Inscripcion)
admin.site.register(Lenguaje)




class CacAdminSite(admin.AdminSite):
    site_header = 'Administracion Codo a Codo'
    site_title = 'Administracion superuser'
    index_title= 'Administracion del sitio'
    empty_value_display = 'No hay datos para visualizar'

#registros de modelos en Admin personalizado
sitio_admin = CacAdminSite(name='cacadmin')
sitio_admin.register(Estudiante, JuanCarlos)
sitio_admin.register(Comision, ComisionAdmin)
sitio_admin.register(Inscripcion)