'''
Ejercicio 4
Escribir otra función que reciba el diccionario generado con la función anterior y 
devuelva una tupla con la palabra más repetida y su frecuencia.
'''
from Ej3 import frec_palabras

def mas_repetida(palabras: dict):
    if not isinstance(palabras, dict):
        raise ValueError("Dato no válido")  
    max = ("", 0)
    for palabra, frecuencia in palabras.items():
        if frecuencia > max[1]:
            max = (palabra,frecuencia)
        elif frecuencia == max[1]:
            max += (palabra, frecuencia)
    return max

print("---------- Pruebas ----------")

print(mas_repetida(frec_palabras("Mensaje de prueba Prueba MENSAJE menSaje de prueba Mensaje DE PRUEBA")))

try:
    print(mas_repetida(["Hola", "esto", "es", "una", "prueba"]))
except ValueError:
    print("Tipo de dato no válido!")

print(mas_repetida({"hola": 5, "esto": 2, "es": 5, "una": 2, "prueba": 1}))
print(mas_repetida({"hola": 2, "esto": 2, "es": 2, "una": 3, "prueba": 3}))
print(mas_repetida({"hola": 1, "esto": 8, "es": 3, "una": 1, "prueba": 1}))