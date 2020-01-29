posicion = input()
bateria = int(input())
velocidad = int(input())
n = int(input())

# Configurar posicion del robot
configurar_robot(posicion)

for i in range(0, n):

    # Se definen las variables
    giro = False
    avanza = False
    accion = input()

    if accion == "Op 1":
        print("Bateria:", bateria)

    elif accion == "Op 2":

        carga = int(input())
        print("Cuanto desea cargar?")

        # Se dejan fijas las condicones
        if bateria + carga > 100:
            bateria = 100
        else:
            bateria += carga

    elif accion == "Op 3":
        print("Velocidad:", velocidad)

    elif accion == "Op 4":

        nueva_velocidad = int(input())
        print("Cuanto desea cambiar?")

        # Se dejan fijas las condiciones
        if 1 <= nueva_velocidad + velocidad <= 4:
            velocidad += nueva_velocidad
        else:
            print("Velocidad fuera de rango")

    if accion == "Op 5":
        nueva_direccion = "D"
        giro = True

    elif accion == "Op 6":
        nueva_direccion = "U"
        giro = True

    elif accion == "Op 7":
        nueva_direccion = "R"
        giro = True

    elif accion == "Op 8":
        nueva_direccion = "L"
        giro = True

    if accion == "Op 9":
        direccion = "D"
        avanza = True

    elif accion == "Op 10":
        direccion = "U"
        avanza = True

    elif accion == "Op 11":
        direccion = "R"
        avanza = True

    elif accion == "Op 12":
        direccion = "L"
        avanza = True

    if avanza:
        # Analisis de movimiento
        while direccion != obtener_direccion():
            girar_derecha()

        if bateria < 5:
            print("Sin bateria")

        else:

            # Se devuleve si hay choque
            hay_choque = False
            veces_avanzadas = 0

            for j in range(0, velocidad):
                # Para cada iteracion se analiza si puede avanzar y se resta  bateria
                if bateria < 5:
                    print("Sin bateria")
                    break

                else:
                    # Analiza si existe tope y se avanza
                    if avanzar():
                        bateria -= 5
                        veces_avanzadas += 1

                    else:
                        print("Alerta de Choque")
                        hay_choque = True
                        break

            if hay_choque:
                # Se devuelve
                girar_derecha()
                girar_derecha()

                for i in range(0, veces_avanzadas):
                    avanzar()
                    bateria += 5

                # Se vuelve al giro original
                girar_derecha()
                girar_derecha()

    if giro:
        while obtener_direccion() != nueva_direccion:
            girar_derecha()

print(dibujar_mapa())
print("Bateria:", bateria)
print("Velocidad:", velocidad)