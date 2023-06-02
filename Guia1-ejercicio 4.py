#Guia1-ejercio 4.py
from os import system
system('cls')
#Desarrollar un algoritmo para calcular la superficie de un triángulo rectángulo (base por altura dividido dos):
print()
print('--------------------------------------------------')
print('calcular la superficie de un triángulo rectángulo ')
print('--------------------------------------------------')
print()
#Mostrar el mensaje de ingreso y guardar en base.
base = int(input('ingresar la base '))
#Mostrar el mensaje de ingreso y guardar en altura.
Altura= int(input('ingresar la altura '))
#Calcular y guardar en superficie.
Resultado = (base * Altura/2)
#Mostrar mensaje y el valor de superficie.
print()
print('--------------------------------------------------')
print('resultado ', Resultado)
print('--------------------------------------------------')
