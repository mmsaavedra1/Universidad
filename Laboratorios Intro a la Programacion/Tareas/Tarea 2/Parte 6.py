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


# Comprueba choque
def no_choque(x, y, n, sentido):
    # Se analiza segun el sentido de movimiento de "X"
    if sentido == "X":
        # Se analiza si se sale del margen
        if (x + n) in range(0, columnas):
            # Se analiza si el siguiente elemento es una "X"
            if mapa[y][x + n] != " X ":
                return True
            else:
                print("Alerta de choque")
                return False
        else:
            print("Alerta de choque")


    # Se analiza segun el sentido de movimiento de "Y"
    else:
        # Se analiza si se sale del margen
        if (y + n) in range(0, filas):
            # Se analiza si el siguiente elemento es una "X"
            if mapa[y + n][x] != " X ":
                return True
            else:
                print("Alerta de choque")
                return False
        else:
            print("Alerta de choque")


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

historial = list()
deshacer = list()
desecho = False

##### AQUI COMIENZA A OPERAR #####
for i in range(n):
    opcion = input()
    print(opcion, historial, deshacer)

    # Se realiza lo que dicta cada opcion
    if "OP 1" in opcion:
        opcion = opcion.replace("OP 1", "")
        print("Bateria:", bateria)

    elif "OP 2" in opcion:
        # Ya no se puede rehacer
        historial = list()
        deshacer = list()
        desecho = False

        # Se almacena en historial
        historial.append([x, y, direccion, bateria, "CARGAR"])

        opcion = opcion.replace("OP 2", "")
        carga_bateria = int(input())
        if bateria + carga_bateria > 100:
            bateria = 100
        else:
            bateria += carga_bateria
        print("Cargar Bateria")


    elif "OP 3" in opcion:
        # Ya no se puede rehacer
        historial = list()
        deshacer = list()
        desecho = False

        # Se almacena en historial
        historial.append([x, y, direccion, bateria, "DIRECCION"])

        opcion = opcion.replace("OP 3", "")
        direccion = opcion[-1]

        # Actualizar en mapa
        mapa[int(y)][int(x)] = " " + direccion + " "
        print("Robot Apunta a " + direccion)

    elif "OP 4" in opcion:
        # Ya no se puede rehacer
        historial = list()
        deshacer = list()
        desecho = False

        # Se almacena en historial
        historial.append([x, y, direccion, bateria, "MOVER"])

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
                    if _x > x:
                        if no_choque(x, y, 1, "X"):
                            bateria -= 5
                            x += 1
                        else:
                            analiza_y = False
                            break

                    elif _x < x:
                        if no_choque(x, y, -1, "X"):
                            bateria -= 5
                            x -= 1
                        else:
                            analiza_y = False
                            break

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
                        if _y > y:
                            if no_choque(x, y, 1, "Y"):
                                bateria -= 5
                                y += 1
                            else:
                                break

                        elif _y < y:
                            if no_choque(x, y, -1, "Y"):
                                bateria -= 5
                                y -= 1
                            else:
                                break

                    else:
                        print("Sin Bateria")
                        break

        # Se actualiza en el mapa
        mapa[int(y)][int(x)] = " " + direccion + " "
        print("X:" + str(x) + "\n" + "Y:" + str(y))

    elif "OP 5" in opcion:
        opcion = opcion.replace("OP 5", "")

        # Se deshacen los movimientos
        if len(historial) != 0:
            movimientos = historial.pop()
            deshacer.append(movimientos)
            mapa[y][x] = "   "
            x, y, direccion, bateria, tipo = movimientos
            mapa[y][x] = direccion

            ##### AQUI VA EL TIPO
            if tipo == "CARGAR":
                print("Bateria:", bateria)
            elif tipo == "DIRECCION":
                print("Robot Apunta a", direccion)
            else:
                print("X:" + str(x) + "\n" + "Y:" + str(y))

            desecho = True

        else:
            print("Operacion Invalida")

    elif "OP 6" in opcion:
        opcion = opcion.replace("OP 6", "")

        # Se rehacen los movimientos
        if desecho:
            movimientos = deshacer.pop(0)
            historial.append(movimientos)
            mapa[y][x] = "   "
            x, y, direccion, bateria, tipo = movimientos
            mapa[y][x] = direccion

            ##### AQUI VA EL TIPO
            if tipo == "CARGAR":
                print("Bateria:", bateria)
            elif tipo == "DIRECCION":
                print("Robot Apunta a", direccion)
            else:
                print("X:" + str(x) + "\n" + "Y:" + str(y))

        else:
            print("Operacion Invalida")

    elif "OP 7" in opcion:
        opcion = opcion.replace("OP 7", "")

        # Se imprime el mapa en pantalla
        imprimir_tablero(mapa)