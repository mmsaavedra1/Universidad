numero1 = int(input())
suma = 0

# SE DICE QUE AL MENOS 3 DIGITOS
numero = numero1 % 1000

# Se obtienen las cifras del numero
centenas = numero // 100
decenas = (numero % 100) // 10
unidades = numero % 10

# Se controlan las sentencias de control de flujo
if 0 < centenas < 2:
    suma += 10
elif 2 <= centenas < 7:
    suma += 20
else:
    suma -= 1

if 0 < decenas < 7:
    suma += 20
else:
    suma += 4

if unidades < 4:
    suma -= 10
else:
    suma += 0  # no tienen sentido estas lineas

print("El valor obtenido es: " + str(suma))