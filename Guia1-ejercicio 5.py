#Guia1-ejercio 5.py
from os import system
system('cls')
#Desarrollar un algoritmo para calcular el promedio de 5 valores enteros:
print()
print('--------------------------------------------------')
print('calcular el promedio de 5 valores enteros')
print('--------------------------------------------------')
print()
#Mostrar mensaje de ingreso y guardar en uno.
Uno = int(input('ingresar un valor para uno '))
#Mostrar mensaje de ingreso y guardar en dos.
Dos = int(input('ingresar un valor para dos '))
#Mostrar mensaje de ingreso y guardar en tres.
Tres = int(input('ingresar un valor para tres '))
#Mostrar mensaje de ingreso y guardar en cuatro.
Cuatro = int(input('ingresar un valor para cuatro '))
#Mostrar mensaje de ingreso y guardar en cinco.
Cinco = int(input('ingresar un valor para cinco '))
#Calcular el promedio y guardar en promedio.
promedio = (Uno + Dos + Tres + Cuatro + Cinco) /5
#Mostrar mensaje y el valor de promedio.
print()
print('--------------')
print('valor promedio' ,promedio)
print('--------------')