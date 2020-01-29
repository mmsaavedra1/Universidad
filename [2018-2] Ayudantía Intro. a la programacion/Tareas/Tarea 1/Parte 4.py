################ NO MODIFICAR ###############
import random


class Posicion:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, int):
            return Posicion(self.x + other, self.y + other)
        return Posicion(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        # if isinstance(other, int):
        return Posicion(self.x * other, self.y * other)

    def __lt__(self, other):
        if isinstance(other, int):
            return self.x < other or self.y < other
        return self.x < other.x or self.y < other.y

    def __gt__(self, other):
        if isinstance(other, int):
            return self.x > other or self.y > other
        return self.x > other.x or self.y > other.y

    def __eq__(self, other):
        if isinstance(other, int):
            return self.x == other and self.y == other
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return "Posicion({}, {})".format(self.x, self.y)


class Wrapper:
    murallas = [[2, 3, 5, 6, 7, 8, 9], [5, 6, 7, 8, 9], [5, 6], [0, 1, 2, 3],
                [7, 8, 9],
                [1, 2, 3, 4, 7, 8, 9], [1, 2, 3, 4], [1, 7, 8, 9], [1], [0, 1]]

    FLECHAS = {"U": "\u2191", "D": "\u2193", "L": "\u2190", "R": "\u2192"}
    MOVIMIENTOS = {"U": Posicion(0, -1), "D": Posicion(0, 1),
                   "L": Posicion(-1, 0), "R": Posicion(1, 0)}
    pos = Posicion(9, 9)
    direccion = random.choice(["U", "D", "L", "R"])


def obtener_direccion():
    return Wrapper.direccion


def configurar_robot(pos):
    Wrapper.pos = Posicion(*[int(e) for e in pos[1:-1].split(",")])


def dibujar_mapa():
    mapa = " " + "_" * 39 + "\n"
    for i in range(len(Wrapper.murallas)):
        linea = "|"
        for j in range(len(Wrapper.murallas)):
            if Posicion(j, i) == Wrapper.pos:
                linea += " {} ".format(Wrapper.direccion)
            elif j in Wrapper.murallas[i]:
                linea += " X "
            else:
                linea += "   "
            linea += "|"
        mapa += linea + "\n"
    return mapa + " " + "-" * 39


def avanzar():
    nueva_pos = Wrapper.pos + Wrapper.MOVIMIENTOS[Wrapper.direccion]
    if nueva_pos < 0 or nueva_pos > len(Wrapper.murallas) - 1:
        return False
    elif nueva_pos.x in Wrapper.murallas[nueva_pos.y]:
        return False
    Wrapper.pos = nueva_pos
    return True


def girar_derecha():
    if Wrapper.direccion == "U":
        Wrapper.direccion = "R"
    elif Wrapper.direccion == "R":
        Wrapper.direccion = "D"
    elif Wrapper.direccion == "D":
        Wrapper.direccion = "L"
    elif Wrapper.direccion == "L":
        Wrapper.direccion = "U"


def girar_izquierda():
    if Wrapper.direccion == "U":
        Wrapper.direccion = "L"
    elif Wrapper.direccion == "L":
        Wrapper.direccion = "D"
    elif Wrapper.direccion == "D":
        Wrapper.direccion = "R"
    elif Wrapper.direccion == "R":
        Wrapper.direccion = "U"


################ NO MODIFICAR ###############
posicion = input()
bateria = int(input())
velocidad = int(input())
n = int(input())

# Configurar posicion del robot
configurar_robot(posicion)

for i in range(0, n):

    opcion = input()
    if opcion == "Op 9":
        direccion = "D"

    elif opcion == "Op 10":
        direccion = "U"

    elif opcion == "Op 11":
        direccion = "R"

    elif opcion == "Op 12":
        direccion = "L"

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

print(dibujar_mapa())
print("Bateria:", bateria)
print("Velocidad:", velocidad)