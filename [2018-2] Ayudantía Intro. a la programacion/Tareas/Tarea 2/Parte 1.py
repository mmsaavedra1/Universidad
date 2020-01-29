bateria = int(input())
n = int(input())

# Comienzan las iteraciones
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