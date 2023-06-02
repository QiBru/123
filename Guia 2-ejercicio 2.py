#desarrollar un algoritmo para determinar el mayo de dos numeros
from os import system
print('cls')
#1 mostrar un mensaje de presentacion explicando que hace el programa
print ('este programa determinar el mayor de dos numeros enteros distintos.')
#2 mostrar mensaje de ingreso de un valor y guardarl9o en varia
a =int(input('ingrese un numero entero distinto para a: '))
#3
b = int(input('ingrese un numero entero distinto para b: '))
#4 comparar si a==b
if a == b:
#por la salida del Si indicar que a y b son iguales, terminar el progama.
    print('el numeros ingresados son iguales.')
else:
#6 por la salida del no comprobar SI a > b.
    if a > b:
#7 por la salida del SI indicar que a es mayor que b, terminar el programa
        print('El numero mayo es a =', a)

    else:
#8 por la salida del no indicar que b es mayor que a.
        print('El numero mayor es b =',b)
#9 mostrar fin del programa
print('Fin del programa')
