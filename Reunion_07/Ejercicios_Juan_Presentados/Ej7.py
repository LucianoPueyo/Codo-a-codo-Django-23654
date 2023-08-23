'''
#### Ejercicio 7
Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una 
persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es 
opcional. Crear los siguientes métodos para la clase:
* Un constructor, donde los datos puden estar vacios
* Los setters y getters para cada uno de los atributos. El atributo cantidad no se puede 
  modificar directamente, solo ingresando o retirando dinero.
* mostrar(): Muestra los datos de la cuenta
* ingresar(cantidad): se ingresa una cantidad a la cuenta, si la misma es negativa 
  no se hará nada.
* retirar(cantidad): se retira una cantidad de la cuenta. La misma puede tener 
  saldo negativo.
'''
from Ej6 import Persona, ExcepcionPersona

class ExcepcionCuenta(BaseException):
    pass

class Cuenta:
    def __init__(self, titular, cantidad = 0.0):
            self.titular = titular
            self.__cantidad = cantidad

    @property
    def titular(self):
        return self.__titular
    
    @property
    def cantidad(self):
        return self.__cantidad
    
    @titular.setter
    def titular(self, titular):
        if isinstance(titular, Persona):
            self.__titular = titular
        else:
            raise ExcepcionCuenta("Datos inválidos")

    def mostrar(self):
        print(f"""Cuenta perteneciente a 
            Nombre: {self.__titular.nombre}, 
            DNI N° {self.__titular.dni}
            Edad: {self.__titular.edad}. 
            Saldo: ${self.__cantidad}""")
        
    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad
            print(f"Se ingresaron ${cantidad}")

    def retirar(self,cantidad):
        if cantidad > 0:
            self.__cantidad -= cantidad
            print(f"Se extrayeron ${cantidad}")
        else:
            print("Debe ingresar una cantidad válida")
            
            
print("---------- Pruebas ----------")
print("---------- 1 ----------")
try:
    cuenta = Cuenta(Persona(), 5_000)
except (ExcepcionPersona, ExcepcionCuenta) as e:
    print(e)
print("---------- 2 ----------")
try:
    cuenta = Cuenta(Persona("Juan", 25, 24154), 5_000)
except (ExcepcionPersona, ExcepcionCuenta) as e:
    print(e)
print("---------- 3 ----------")
try:
    cuenta = Cuenta(("Juan", 25, 12123456))
except (ExcepcionPersona, ExcepcionCuenta) as e:
    print(e)
print("---------- 4 ----------")
try:
    cuenta = Cuenta(("Juan", 25, 12123456))
except (ExcepcionPersona, ExcepcionCuenta) as e:
    print(e)
print("---------- 5 ----------")
try:
    cuenta = Cuenta(Persona("Juan", 25, 12123456))
    cuenta.mostrar()
    cuenta.ingresar(5_000)
    cuenta.mostrar()
    cuenta.retirar(2_000)
    cuenta.mostrar()
    cuenta.titular = Persona("Fulano", 30, 12123456)
    cuenta.mostrar()
    cuenta.retirar(5_000)
    cuenta.mostrar()
except (ExcepcionPersona, ExcepcionCuenta) as e:
    print(e)

print("---------- 6 ----------")

try:
    cuenta = Cuenta(Persona("Juan", 25, 12123456), 10_000)
    cuenta.mostrar()
    cuenta.retirar(-5)

except (ExcepcionPersona, ExcepcionCuenta) as e:
    print(e)
