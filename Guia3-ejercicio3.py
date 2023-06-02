# Realice un algoritmo que:
cont1=cont2 = 0
acum1=acum2 = 0
# Permite ingresar una serie de números enteros entre 1 y 999.

while True:
        numero = int(input('ingrese un valor entre 1 y 999: '))
    # Salir con cero (0).
        if numero  == 0:
            break
    # Validar que no se ingresen valores fuera del rango y mostrar un mensaje “Valor fuera de rango”.
        if numero <1 or numero >999:
            print('Valor fuera de rango')
            continue
    # Contar y acumular los menores o igual a 500.
        if numero <= 500:
            cont1 += 1
            acum1 += numero
    # Contar y acumular los valores mayores a 500.
        if numero > 500:
            cont2 += 1
            acum2 += numero
# Mostrar los resultados
print('cantidad de valores menores  o iguales a 500 ', cont1,'valor acumulados  ', acum1)
print('cantidad de valores mayores a 500 ', cont2,'valor acumulados  ', acum2)
