'''
Ejercicio 5:
Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una 
cadena de texto en su valor numérico, escriba una función get_int() que lea un valor 
entero del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente 
resolver el ejercicio tanto de manera iterativa como recursiva
'''
def get_int_iterativo():
    error = True
    while error:
        try:
            num = int(input("Ingrese un número: "))
            error = False
        except ValueError:
            print("Dato inválido. Vuelva a ingresarlo!")
    return num

def get_int_recursivo():
    try:
        num = int(input("Ingrese un número: "))
        return num
    except ValueError:
        print("Dato inválido. Vuelva a ingresarlo!")
        return get_int_recursivo()
    




print("---------- Prueba Iterativo ----------")
print(get_int_iterativo())
print("---------- Prueba Recursivo ----------")

print(get_int_recursivo())