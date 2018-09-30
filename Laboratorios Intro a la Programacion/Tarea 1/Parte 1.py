n = int(input())

for i in range(0, n):

    # Se definen las variables
    opcion = input()
    accion = ""

    if opcion == "Op 1":
        accion = "Mostrar Reserva"

    elif opcion == "Op 2":
        accion = "Cargar Bateria"

    elif opcion == "Op 3":
        accion = "Mostrar Velocidad"

    elif opcion == "Op 4":
        accion = "Cambiar Velocidad"

    elif opcion == "Op 5":
        accion = "Apuntar Abajo"

    elif opcion == "Op 6":
        accion = "Apuntar Arriba"

    elif opcion == "Op 7":
        accion = "Apuntar Derecha"

    elif opcion == "Op 8":
        accion = "Apuntar Izquierda"

    elif opcion == "Op 9":
        accion = "Avanzar Abajo"

    elif opcion == "Op 10":
        accion = "Avanzar Arriba"

    elif opcion == "Op 11":
        accion = "Avanzar Derecha"

    elif opcion == "Op 12":
        accion = "Avanzar Izquierda"

    print(accion)


