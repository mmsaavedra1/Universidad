class IronMan:
    def __init__(self, nombre, vida, fuerza, defensa):
        self.nombre = nombre
        self.vida = vida
        self.fuerza = fuerza
        self.defensa = defensa

    def golpear(self, superheroe):
        self.vida -= superheroe.fuerza - self.defensa
        if self.vida <= 0:
            self.vida = 0


class CapitanAmerica:
    def __init__(self, nombre, vida, fuerza, defensa):
        self.nombre = nombre
        self.vida = vida
        self.fuerza = fuerza
        self.defensa = defensa

    def golpear(self, superheroe):
        self.vida -= superheroe.fuerza - self.defensa
        if self.vida <= 0:
            self.vida = 0


###### PROGRAMA #####
n = int(input())
i = 0
iron = input().split(" ")
cap = input().split(" ")

iron_man = IronMan(iron[0], int(iron[1]), int(iron[2]), int(iron[3]))
capitan = CapitanAmerica(cap[0], int(cap[1]), int(cap[2]), int(cap[3]))

while i != n:
    # Se verifica la vida
    i += 1
    if iron_man.vida != 0 and capitan.vida != 0:
        # Golpea IronMan
        capitan.golpear(iron_man)
    else:
        break

    if i != n:
        i += 1
        # Se verifica la vida
        if iron_man.vida != 0 and capitan.vida != 0:
            # Golpea CapitanAmerica
            iron_man.golpear(capitan)
        else:
            break
    else:
        break

if iron_man.vida > capitan.vida:
    print("Ganador:", iron_man.nombre, str(iron_man.vida) + ",",
          capitan.nombre, capitan.vida)
else:
    print("Ganador:", capitan.nombre, str(capitan.vida) + ",", iron_man.nombre,
          iron_man.vida)