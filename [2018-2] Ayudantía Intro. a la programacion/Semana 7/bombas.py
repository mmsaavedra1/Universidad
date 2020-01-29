numeros = input().split(" ")
# Se definen variables
n = int(numeros[0])
rango = int(numeros[1])

# Se crea y almacena el tablero
tablero_final = list()
for i in range(n):
    tablero = input()

    lista = list()
    for i in tablero:
        lista.append(i)

    tablero_final.append(lista)

# Se analiza que tipo de letra es
letra = ""
termina = False
x = -1

for fila in tablero_final:
    x += 1
    y = -1
    for columna in fila:
        y += 1
        if columna != "-":
            letra = columna
            termina = True
            break
    if termina:
        break

if letra == "X" or (letra == "Z" and rango == 2):
    # Hacia arriba
    for i in range(rango):
        if x - i >= 0:
            tablero_final[x - i][y] = letra
    # Hacia abajo
    for i in range(rango):
        if x + i < n:
            tablero_final[x + i][y] = letra

    # Hacia la izquierda
    for j in range(rango):
        if y - j >= 0:
            tablero_final[x][y - j] = letra

    # Hacia la derecha
    for j in range(rango):
        if y + j < n:
            tablero_final[x][y + j] = letra


elif letra == "Y":
    # Hacia diagonal superior izquierda
    for j in range(rango):
        if x - j >= 0 and y - j >= 0:
            tablero_final[x - j][y - j] = letra

    # Hacia diagonal inferior izquierda
    for j in range(rango):
        if x + j < n and y - j >= 0:
            tablero_final[x + j][y - j] = letra

    # Hacia diagonal superior derecha
    for j in range(rango):
        if x - j >= 0 and y + j < n:
            tablero_final[x - j][y + j] = letra

    # Hacia diagonal superior derecha
    for j in range(rango):
        if x + j < n and y + j < n:
            tablero_final[x + j][y + j] = letra

elif letra == "Z":
    # Hacia arriba
    for i in range(rango):
        if x - i >= 0:
            tablero_final[x - i][y] = letra
    # Hacia abajo
    for i in range(rango):
        if x + i < n:
            tablero_final[x + i][y] = letra

    # Hacia la izquierda
    for j in range(rango):
        if y - j >= 0:
            tablero_final[x][y - j] = letra

    # Hacia la derecha
    for j in range(rango):
        if y + j < n:
            tablero_final[x][y + j] = letra

    # Hacia diagonal superior izquierda
    for j in range(rango):
        if x - j >= 1 and y - j >= 1:
            tablero_final[x - j][y - j] = letra

    # Hacia diagonal inferior izquierda
    for j in range(rango):
        if x + j < n - 1 and y - j >= 1:
            tablero_final[x + j][y - j] = letra

    # Hacia diagonal superior derecha
    for j in range(rango):
        if x - j >= 1 and y + j < n - 1:
            tablero_final[x - j][y + j] = letra

    # Hacia diagonal superior derecha
    for j in range(rango):
        if x + j < n - 1 and y + j < n - 1:
            tablero_final[x + j][y + j] = letra

# Formar tablero para imprimir
tablero_nuevo = ""
for fila in tablero_final:
    for columna in fila:
        tablero_nuevo += columna + " "
    tablero_nuevo.rstrip()
    tablero_nuevo += "\n"

print(tablero_nuevo.rstrip())