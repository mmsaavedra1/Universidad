def movimiento_valido(i, j, n):
    """Funcion que define si un movimiento esta dentro del tablero"""

    # Verifica si el siguiente movimiento hacia la derecha se puede hacer.
    if i+1 <= n:
        return True

    # Verifica si el siguiente movimiento hacia abajo se puede hacer.
    elif j+1 <= n:
        return True

    # Opcion retornada cuando se puede mover para el lado deseado.a
    else:
        return False


def tablero(x, y, n):
    """Funcion recursiva que analiza cada movimiento
    y cuenta la cantidad de caminos realizados"""

    global caminos_posibles

    # Condicion de termino para un camino.
    if (x == n) and (y == n):
        caminos_posibles += 1
        return True


    # 1º Sumamos indefinidamente hacia la derecha.
    if (x != n) and movimiento_valido(x, y, n):
        tablero(x+1, y, n)

    # 2ª Sumamaos indefinidamente hacia abajo.
    if (y != n) and movimiento_valido(x, y, n):
        tablero(x, y + 1, n)

if __name__ == '__main__':

    # Se setean los caminos posibles.
    caminos_posibles = 0

    # Se genera un input con la cantidad deseada.
    numero_celdas = int(input("Ingresa el tamaño del tablero: \n"))

    # Se ejecuta la funcion recursiva.
    tablero(1, 1, numero_celdas)
    print(caminos_posibles)


