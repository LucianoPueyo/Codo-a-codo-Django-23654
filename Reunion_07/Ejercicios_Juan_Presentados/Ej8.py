'''
Ejercicio 8:
Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase 
CuentaJoven que deriva de la clase creada en el punto 7. Cuando se crea esta nueva clase, 
además del titular y la cantidad se debe guardar una bonificación que estará expresada en 
tanto por ciento. Crear los siguientes métodos para la clase:
* Un constructor
* Los setters y getters para el nuevo atributo
* En esta ocasión los titulares tienen que ser mayores de edad, por lo tanto hay que crear 
  un método es_titular_valido() que devuelve verdadero si el titular es mayor de edad pero 
  menor de 25 años y falso en caso contrario
* La retirada de dinero solo se podrá hacer si es titular es válido
* El método mostrar() debe devolver el mensaje de "CuentaJoven" y la bonificación de la 
  cuenta.
'''
from Ej6 import Persona, ExcepcionPersona
from Ej7 import Cuenta, ExcepcionCuenta

class CuentaJoven(Cuenta):
    
    def __init__(self, titular, cantidad = 0.0, bonificacion = 0):
        super().__init__(titular, cantidad)
        self.__bonificacion = bonificacion

    @property
    def bonificacion(self):
        return self.__bonificacion
        
    @bonificacion.setter
    def bonificacion(self, bonificacion):
        self.__bonificacion = bonificacion

    def es_titular_valido(self):
        return self.titular.edad > 18 and self.titular.edad < 25
        
    def retirar(self, cantidad):
        if self.es_titular_valido() and cantidad > 0:
            super().retirar(cantidad)
        elif not self.es_titular_valido():
            print("Un titular inválido no puede extraer dinero")
        else:
            print("Debe ingresar una cantidad válida")
            
    def mostrar(self):
        print(f"""Cuenta perteneciente a 
            Nombre: {self.titular.nombre}, 
            DNI N° {self.titular.dni}
            Edad: {self.titular.edad}. 
            Saldo: ${self.cantidad}
            Bonificacion: {self.bonificacion}""")

print("---------- Pruebas ----------")
print("---------- 1 ----------")
try:
    cuenta = CuentaJoven(Persona(), 5_000)
except (ExcepcionPersona, ExcepcionCuenta) as e:
    print(e)
print("---------- 2 ----------")
try:
    cuenta = CuentaJoven(Persona("Juan", 25, 24154), 5_000)
except (ExcepcionPersona, ExcepcionCuenta) as e:
    print(e)
print("---------- 3 ----------")
try:
    cuenta = CuentaJoven(("Juan", 25, 12123456))
except (ExcepcionPersona, ExcepcionCuenta) as e:
    print(e)
print("---------- 4 ----------")
try:
    cuenta = CuentaJoven(("Juan", 25, 12123456))
except (ExcepcionPersona, ExcepcionCuenta) as e:
    print(e)
print("---------- 5 ----------")
try:
    cuenta = CuentaJoven(Persona("Juan", 25, 12123456), 0,10)
    cuenta.mostrar()
    cuenta.ingresar(5_000)
    cuenta.mostrar()
    cuenta.retirar(2_000)
    cuenta.mostrar()
    cuenta.titular = Persona("Fulano", 19, 12123457)
    cuenta.mostrar()
    cuenta.retirar(5_000)
    cuenta.mostrar()
    cuenta.retirar(2_500)
    cuenta.mostrar()

except (ExcepcionPersona, ExcepcionCuenta) as e:
    print(e)

print("---------- 6 ----------")

try:
    cuenta = CuentaJoven(Persona("Juan", 20, 12123456), 10_000, 10)
    cuenta.mostrar()
    cuenta.retirar(-5)

except (ExcepcionPersona, ExcepcionCuenta) as e:
    print(e)