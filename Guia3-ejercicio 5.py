# Realice un algoritmo que:
import ramdom
# Genere una lista de 30 números al azar de hasta 2 dígitos.
cont2 = cont3 = acum2 = acum3 =  0
for x in range (0,30):
    numero = ramdom.randint(10,99)
# Mostrar los pares con un “*” asterisco delante. (nro % 2 = 0)
    if numero % 2 == 0:
        print('*', numero)
# Mostrar los impares con un “#” numeral delante. (else)
    if numero % 3==0:
        print('#', numero)
# Contar y acumular los pares.
cont2 += 1
acum2 += numero
# Contar y acumular los impares.
cont3 += 1
acum3 += numero
# Mostrar el resultado de la cuenta y el acumulado de cada grupo.
print('cantidad de pares ' ,cont2, 'valores acumulado', acum2)
print('cantidad de inpares ' ,cont3, 'valores acumulado', acum3)
