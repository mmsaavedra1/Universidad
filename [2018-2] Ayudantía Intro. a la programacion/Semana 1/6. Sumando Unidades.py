numero_1 = int(input())
numero_2 = int(input())

# Descomponer numero 1
centenas_1 = numero_1 // 100 #a1
resto_centenas_numero_1 = numero_1 % 100 #a2

decenas_1 = resto_centenas_numero_1 // 10 #a3
resto_decenas_numero_1 = resto_centenas_numero_1 % 10

unidades_1 = resto_decenas_numero_1

# Descomponer numero 2
centenas_2 = numero_2 // 100
resto_centenas_numero_2 = numero_2 % 100

decenas_2 = resto_centenas_numero_2 // 10
resto_decenas_numero_2 = resto_centenas_numero_2 % 10

unidades_2 = resto_decenas_numero_2

# Descomponer suma
numero_3 = numero_1 + numero_2

centenas_3 = numero_3 // 100
resto_centenas_numero_3 = numero_3 % 100

decenas_3 = resto_centenas_numero_3 // 10
resto_decenas_numero_3 = resto_centenas_numero_3 % 10

unidades_3 = resto_decenas_numero_3

# Resultados en pantalla
print(str(centenas_1) + "00 + " + str(decenas_1) + "0 + " + str(unidades_1))
print(str(centenas_2) + "00 + " + str(decenas_2) + "0 + " + str(unidades_2))
print(str(centenas_3) + "00 + " + str(decenas_3) + "0 + " + str(unidades_3))