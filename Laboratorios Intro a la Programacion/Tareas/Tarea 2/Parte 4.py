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
    print("Mostrar Mapa")
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

        # Actualizar en mapa
        mapa[int(y)][int(x)] = " " + direccion + " "
        print("Robot Apunta a " + direccion)

    elif "OP 4" in opcion:
        opcion = opcion.replace("OP 4", "")

        # Posiciones a las que quiero ir
        _x, _y = opcion.split("(")[1].rstrip(")").split(",")
        _x = int(_x)
        _y = int(_y)

        # Se actualiza y traslada en el mapa en cada iteracion
        mapa[int(y)][int(x)] = "   "

        # Primero en el eje de las x

        analiza_y = True
        for _ in range(columnas):
            if _x == x:
                break

            if bateria - 5 < 0:
                print("Sin Bateria")
                analiza_y = False
                break

            else:
                if bateria - 5 >= 0:
                    bateria -= 5
                    if _x > x:
                        x += 1
                    elif _x < x:
                        x -= 1
                else:
                    analiza_y = False
                    print("Sin Bateria")
                    break

        # Segundo en el eje de las y
        if analiza_y:
            for _ in range(filas):
                if _y == y:
                    break

                if bateria - 5 < 0:
                    print("Sin Bateria")
                    break

                else:
                    if bateria - 5 >= 0:
                        bateria -= 5
                        if _y > y:
                            y += 1
                        elif _y < y:
                            y -= 1
                    else:
                        print("Sin Bateria")
                        break

        # Se actualiza en el mapa
        mapa[int(y)][int(x)] = " " + direccion + " "
        print("X:" + str(x) + "\n" + "Y:" + str(y))

    elif "OP 5" in opcion:
        opcion = opcion.replace("OP 5", "")
        print("Deshacer Movimiento")

    elif "OP 6" in opcion:
        opcion = opcion.replace("OP 6", "")
        print("Rehacer Movimiento")

    elif "OP 7" in opcion:
        opcion = opcion.replace("OP 7", "")

        # Se imprime el mapa en pantalla
        imprimir_tablero(mapa)