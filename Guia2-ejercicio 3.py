#Guia2-ejercicio 3.py
from os import system
print('çls')
#Desarrollar un algoritmo para determinar el mayor de tres números distintos.
print()
print('------------------------------------------------------------')
print('algoritmo para determinar el mayor de tres números distintos')
print('------------------------------------------------------------')
print()
#Muestra un mensaje de presentación.
print('mayor a 3 numeros distintos ')
#Mostrar mensaje de ingreso de un valor y guardarlo en la variable a.
a = int(input('ingreso de un valor para a '))
#Mostrar mensaje de ingreso de un valor y guardarlo en la variable b.
b = int(input('ingreso de un valor para b '))
#Mostrar mensaje de ingreso de un valor y guardarlo en la variable c.
c= int(input('ingreso de un valor para c '))
#Implementar tres comparaciones para determinar cuál es el mayor.
if a > b:
    if a > c:
        print('el mayor es a ',a)
    else:
        print('el mayor es ',c)
else:
    if b > c:
        print('el mayor es ',b)
    else:
        print('es mayor ',c)
#Mostrar el mensaje correspondiente para cada resultado de la comparación.

#Mostrar Fin del programa.
print()
print('---------------------------------------------------------------')
print('Fin del programa')
print('---------------------------------------------------------------')
print()
