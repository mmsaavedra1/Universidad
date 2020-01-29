# Recibimos el tablero
def definir_mapa(n):
    lista = list()
    for i in range(n):
        fila = input()
        fila = fila.lstrip("[")
        fila = fila.rstrip("]")
        lista.append(fila.split(","))

    return lista


# Imprimimos el tablero
def imprimir_tablero(mapa):
    print(" " + "___" * columnas + " ")
    for i in mapa:
        actual = "|"
        for j in i:
            actual += j
        print(actual + "|")
    print(" " + "---" * columnas + " ")


##### AQUI SE SETEAN CONDICIONES INICIALES #####

posicion = input().split(",")
direccion = input()
n = int(input())
mapa = definir_mapa(n)

x = int(posicion[0].lstrip("("))
y = int(posicion[1].rstrip(")"))
mapa[y][x] = " " + direccion + " "
filas = n
columnas = len(mapa[0])

bateria = int(input())
n = int(input())

##### AQUI COMIENZA A OPERAR #####
for i in range(n):
    opcion = input()

    # Se realiza lo que dicta cada opcion
    if "OP 1" in opcion:
        opcion = opcion.replace("OP 1", "")
        print("Bateria:", bateria)

    elif "OP 2" in opcion:
        opcion = opcion.replace("OP 2", "")
        carga_bateria = int(input())
        if bateria + carga_bateria > 100:
            bateria = 100
        else:
            bateria += carga_bateria
        print("Cargar Bateria")

    elif "OP 3" in opcion:
        opcion = opcion.replace("OP 3", "")
        direccion = opcion[-1]
        print("Robot Apunta a " + direccion)

    elif "OP 4" in opcion:
        opcion = opcion.replace("OP 4", "")
        x, y = opcion.split("(")[1].rstrip(")").split(",")
        print("X:" + x + "\n" + "Y:" + y)

    elif "OP 5" in opcion:
        opcion = opcion.replace("OP 5", "")
        print("Deshacer Movimiento")

    elif "OP 6" in opcion:
        opcion = opcion.replace("OP 6", "")
        print("Rehacer Movimiento")

    elif "OP 7" in opcion:
        opcion = opcion.replace("OP 7", "")
        print("Mostrar Mapa")

        # Se imprime el mapa en pantalla
        imprimir_tablero(mapa)