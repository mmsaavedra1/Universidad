bateria = int(input())
velocidad = int(input())
n = int(input())

for i in range(0, n):
    comando = input()

    if comando == "Op 1":
        print("Bateria:", bateria)

    elif comando == "Op 2":

        carga = int(input())
        print("Cuanto desea cargar?")

        # Se dejan fijas las condicones
        if bateria + carga > 100:
            bateria = 100
        else:
            bateria += carga

    elif comando == "Op 3":
        print("Velocidad:", velocidad)

    elif comando == "Op 4":

        nueva_velocidad = int(input())
        print("Cuanto desea cambiar?")

        # Se dejan fijas las condiciones
        if 1 <= nueva_velocidad + velocidad <= 4:
            velocidad += nueva_velocidad
        else:
            print("Velocidad fuera de rango")