from django.db import models


class Persona(models.Model):
    nombre = models.CharField(verbose_name="Nombre", max_length=250)
    apellido = models.TextField(verbose_name="Apellido")
    dni = models.CharField(verbose_name="DNI", max_length=250, primary_key=True)
    email = models.EmailField(verbose_name="Email", max_length=250)
    apodo = models.CharField(verbose_name="Apodo", max_length=250)

    def __str__(self) -> str:
        return f"{self.dni} - {self.apellido}"