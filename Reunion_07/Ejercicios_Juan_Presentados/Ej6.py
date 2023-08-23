'''
 Ejercicio 6
Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los 
siguientes métodos para la clase:
* Un constructor, donde los datos pueden estar vacíos
* Los setters y getters para cada uno de los atributos. Se deben validar las 
  entradas de datos
* Un método *mostrar()* que muestre los datos de la persona
* Un método *es_mayor_de_edad()* que devuelva un valor lógico indicando 
  si es mayor de edad.
'''
class ExcepcionPersona(BaseException):
    pass

class Persona:
    def __init__(self, nombre = "", edad = 0, dni = ""):
        #Uso los setters para darle valores
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
        
    @property
    def nombre(self):
        return self.__nombre
        
    @nombre.setter
    def nombre(self, nombre):
        if(nombre != "" and nombre.replace(" ", "").isalpha()):
            self.__nombre = nombre
        else:
            raise ExcepcionPersona("Nombre inválido")
        
    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self, edad):
        if isinstance(edad,int) and edad > 0 and edad < 110:
            self.__edad = edad
        else:
            raise ExcepcionPersona("Edad Inválida")
        
    @property
    def dni(self):
        return self.__dni
    
    @dni.setter
    def dni(self, dni):
        dni = str(dni)
        if dni.isdigit() and len(dni) > 6 and len(dni) < 9:
            self.__dni = dni
        else:
            raise ExcepcionPersona("DNI Inválido ")
        
    def mostrar(self):
        print(f"{self.__nombre} cuyo DNI es {self.__dni} tiene {self.__edad} años")
        
    def es_mayor_de_edad(self):
        return self.__edad >= 18

print("---------- Pruebas ----------")
print("---------- 1 ----------")

try:
    p1 = Persona()
except ExcepcionPersona as e:
    print(e)

print("---------- 2 ----------")

try:
    p1 = Persona("Juan123")
except ExcepcionPersona as e:
    print(e)
    
print("---------- 3 ----------")

try:
    p1 = Persona("Juan")
except ExcepcionPersona as e:
    print(e)

print("---------- 4 ----------")

try:
    p1 = Persona("Juan", 250)
except ExcepcionPersona as e:
    print(e)

print("---------- 5 ----------")

try:
    p1 = Persona("Juan", 25)
except ExcepcionPersona as e:
    print(e)

print("---------- 6 ----------")

try:
    p1 = Persona("Juan", 25, 123456789)
    
except ExcepcionPersona as e:
    print(e)

print("---------- 7 ----------")

try:
    p1 = Persona("Juan", 25, 123456)
    
except ExcepcionPersona as e:
    print(e)

print("---------- 8 ----------")

try:
    p1 = Persona("Juan", 25, 12123456)
    p1.mostrar()
    print("Es mayor de edad") if p1.es_mayor_de_edad() else print("Es menor de edad")
except ExcepcionPersona as e:
    print(e)

print("---------- 9 ----------")

try:
    p1 = Persona("Pedro", 16, 12123456)
    p1.mostrar()
    print("Es mayor de edad") if p1.es_mayor_de_edad() else print("Es menor de edad")
    print("---------- Prueba getters ----------")
    print(f"Nombre {p1.nombre}\nEdad: {p1.edad}\nDNI: {p1.dni}")
    print("---------- Prueba setters ----------")
    p1.nombre = "Javier"
    p1.edad = 15
    p1.dni = 12678654
    p1.mostrar()
except ExcepcionPersona as e:
    print(e)

