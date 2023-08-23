'''
Ejercicio 3:
Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con 
cada palabra que contiene y la cantidad de veces que aparece (frecuencia).
'''
def frec_palabras(cadena: str):
    if not isinstance(cadena, str):
        #Si el dato no es de tipo str invoco a una excepción
        raise ValueError("Dato no válido")
    
    #Paso la cadena a minusculas y la separo por espacios
    lista_palabras = cadena.lower().split()
    dict_palabras = dict()

    for palabra in lista_palabras:
        if palabra in dict_palabras.keys():
            #Si la palabra está en el diccionario le sumo 1 a su valor
            dict_palabras[palabra] += 1
        else:
            #Si no está la agrego con el valor 1
            dict_palabras[palabra] = 1
    return dict_palabras

print("---------- Pruebas ----------")

try:
    print(frec_palabras(2))
except ValueError as error:
    print(error)
    
print(frec_palabras("Mensaje de prueba Prueba MENSAJE menSaje de prueba Mensaje DE PRUEBA"))