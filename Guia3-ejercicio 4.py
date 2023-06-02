# Realice un algoritmo que:

# Permitir el ingreso de 12 valores entre 1 y 100.
cont2 = cont3 = 0
acum2 = acum3 = 0
cont = 0
ingresados = 0
while True:
    numero = int(input('ingrese un numero entre 1 y 100: '))
# Salir con -1 en caso de no completar la lista de los 12 números.
    if numero == -1:
        break
# Validar que el valor ingresado esté entre 1 y 100 inclusivos.
    if numero  <1 or numero >100:
        print('valor fuera de rango ')
        continue
    ingresados += 1

# Contar y acumular los divisibles por 2. (número % 2)
    if numero % 2 == 0 :
        cont2 += 1
        acum2 += numero
# Contar y acumular los no divisibles por 2. (else)
    else:
        cont3 += 1
        acum3+= numero
# Mostrar los resultados en caso de completar la lista.
print('cantidad de valores ingresados', ingresados)
print('cantidad divisible por 2 :',cont2,'valor acumulado ',acum2 )
print('cantidad de no divisible por 2 :',cont3,'valor acumulado ',acum3 )
# En caso de no completar la lista mostrar el mensaje “No ha completado la lista de 12 números”.