'''
Ejercicio 1
Escribir una función que calcule el máximo común divisor entre dos números.
'''
from math import gcd
def mcd(num1, num2):
    num1 = abs(int(num1))
    num2 = abs(int(num2))
    if num2 > num1:
        min = num1
    else:
        min = num2
    while min > 0:
        if num1 % min == 0 and num2 % min == 0:
            return min
        min -= 1

print("---------- Pruebas ----------")
''' Se comparan los resultados usando la función gcd de la librería math '''
print(f"mcd(7,9) = {mcd(7,9)} = {gcd(7,9)}")
print(f"mcd(14,19) = {mcd(14,19)} = {gcd(14,19)}")
print(f"mcd(28,36) = {mcd(28,36)} = {gcd(28,36)}")
print(f"mcd(18,24) = {mcd(18,24)} = {gcd(18,24)}")
print(f"mcd(320,150) = {mcd(320,150)} = {gcd(320,150)}")