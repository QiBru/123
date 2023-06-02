#Guia1-ejercicio 2.py
from os import system
system('cls')
# 1) Desarrollar un algoritmo para el cálculo de la hipotenusa:
print('calculo de la hipotenusa')
print()
# 2) Importar la librería math para obtener la raíz cuadrada (import math).
import math
# 3) Mostrar mensaje de ingreso y guardar cateto A en A.
A = int(input('ingrese el cateto de A: '))
# 4) Mostrar mensaje de ingreso y guardar cateto B en B.
B = int(input('ingrese el cateto de B: '))
# 5) Calcular y guardar hipotenusa en C “C = math.sqrt( pow(A,2) + pow(B,2) )” o “C = math.sqrt(A ** 2 + B ** 2)”
C = math.sqrt( pow(A,2) + pow(B,2) )
# 6) Mostrar mensaje con el resultado de C.
print('la hipotenusa es:', C)
