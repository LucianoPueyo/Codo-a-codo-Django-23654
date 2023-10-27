from django.contrib import admin
from administracion.models import Estudiante, Docente, Curso, Categoria, Proyecto, Comision, Inscripcion

# Register your models here.
admin.site.register(Estudiante)
admin.site.register(Docente)
admin.site.register(Curso)
admin.site.register(Categoria)
admin.site.register(Proyecto)
admin.site.register(Comision)
admin.site.register(Inscripcion)