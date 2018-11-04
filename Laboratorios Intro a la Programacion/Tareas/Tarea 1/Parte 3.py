## Escribe tu código debajo de toda la parte que está indicada como NO MODIFICAR ##
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
    MOVIMIENTOS = {"U": Posicion(0, -1), "D": Posicion(0, 1),
                   "L": Posicion(-1, 0), "R": Posicion(1, 0)}
    pos = Posicion(5, 5)
    direccion = random.choice(["U", "D", "L", "R"])


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


def obtener_direccion():
    return Wrapper.direccion


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

n = int(input())

# Se fija la direccion actual del Robot
direcion_actual = obtener_direccion()
nueva_direccion = ""

for i in range(0, n):
    accion = input()

    if accion == "Op 5":
        nueva_direccion = "D"

    elif accion == "Op 6":
        nueva_direccion = "U"

    elif accion == "Op 7":
        nueva_direccion = "R"

    elif accion == "Op 8":
        nueva_direccion = "L"

    while obtener_direccion() != nueva_direccion:
        girar_derecha()

print(dibujar_mapa())