numero = int(input())

billetes_20 = 0
billetes_50 = 0
billetes_100 = 0

# Primero se analiza la descomposicion en multiplos de 20
while numero - 20 > 0:
    if numero % 50 == 0:
        break

    # Se actualiza el mundo de cada iteracion
    numero -= 20
    billetes_20 += 1

# Luego se analiza la descomposicion en multiplos de 50
while numero - 50 > 0:
    if numero % 100 == 0:
        break

    # Se actualiza el mundo de cada iteracion
    numero -= 50
    billetes_50 += 1

# Luego se analiza la descomposicion en multiplos de 100
if numero - 100 > 0:
    billetes_100 = numero // 100
    numero -= 100 * billetes_100

if numero != 0:
    print("No se puede descomponer")
else:
    print(billetes_20, "billete(s) de 20")
    print(billetes_50, "billete(s) de 50")
    print(billetes_100, "billete(s) de 100")