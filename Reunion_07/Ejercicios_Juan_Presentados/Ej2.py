'''
Ejercicio 2
Escribir una función que calcule el mínimo común múltiplo entre dos números.
'''
from math import gcd
def mcm(num1, num2):
    num1 = abs(int(num1))
    num2 = abs(int(num2))
    if num2 > num1:
        mcm = num2
    else:
        mcm = num1
    while True:
        if mcm % num1 == 0 and mcm % num2 == 0:
            return mcm
        mcm += 1
print("---------- Pruebas ----------")
print(f"mcm(18,24) = {mcm(18,24)} = {18*24 // gcd(18,24)}")
print(f"mcm(10,8) = {mcm(10,8)} = {10*8 // gcd(10,8)}")
print(f"mcm(250,20) = {mcm(250,20)} = {250*20 // gcd(250,20)}")
print(f"mcm(36,50) = {mcm(36,50)} = {36*50 // gcd(36,50)}")