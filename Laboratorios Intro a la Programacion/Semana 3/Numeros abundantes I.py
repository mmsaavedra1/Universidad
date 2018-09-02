numero = int(input())

# Se setean los numeros importantes
divisor = 1
suma = 0

while divisor != numero:
    if numero % divisor == 0:
        suma += divisor
        print(divisor)

    divisor += 1

# Se imprime si o si la suma
print(suma)

if suma > numero:
    print("Abundante")
else:
    print("No abundante")