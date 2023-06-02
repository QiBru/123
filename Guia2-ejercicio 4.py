#Guia2-ejercicio 4.py
#esteeee programa fue realizado por el chat gpt preguntar al profe
from os import system
print('cls')
#Desarrollar un algoritmo para determinar el mayor de tres números, puede haber iguales.
print()
print('-------------------------------------------------------------------------------------------------------------------------------------------')
print("algoritmo para determinar el mayor de tres números, puede haber iguales")
print('-------------------------------------------------------------------------------------------------------------------------------------------')
print()

a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
c = int(input("Ingrese el tercer número: "))

if a == b and b == c: # Si los tres números son iguales
    print("Los tres números son iguales.")
elif a == b or a == c or b == c: # Si hay dos números iguales
    if a == b:
        if a > c:
            print("El número mayor es:", a)
        else:
            print("El número mayor es:", c)
    elif a == c:
        if a > b:
            print("El número mayor es:", a)
        else:
            print("El número mayor es:", b)
    elif b == c:
        if b > a:
            print("El número mayor es:", b)
        else:
            print("El número mayor es:", a)
else: # Si los tres números son distintos
    if a > b and a > c:
        print("El número mayor es:", a)
    elif b > a and b > c:
        print("El número mayor es:", b)
    else:
        print("El número mayor es:", c)