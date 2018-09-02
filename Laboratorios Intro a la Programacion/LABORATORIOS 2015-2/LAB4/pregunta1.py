from random import randint as r

print("*** Arbol de Navidad ***")

def arbol(ancho=9):
    esp = altura - ancho - 1
    hojas = 2*ancho + 1
    print((' ' * esp), end='')
    for i in range(hojas):
        valor = r(1, 10)
        cosa = adorno(valor)
        print(cosa, end='')
    print()

def adorno(n):
    cosa = None
    if n > 4:
        cosa = "*"
    elif n == 4:
        cosa = "0"
    elif n == 3:
        cosa = "@"
    elif n == 2:
        cosa = "#"
    elif n == 1:
        cosa = "$"
    return cosa

ancho  = int(input("Dame un ancho: "))
altura = int((ancho + 1) / 2)

for i in range(altura):
    arbol(i)

esp_tallo = int((ancho - 3) / 2)
print((' ' * esp_tallo + 'I' * 3 + '\n' ) * 2)