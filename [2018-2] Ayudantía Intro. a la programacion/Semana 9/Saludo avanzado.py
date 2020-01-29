class Perrito:
    def __init__(self, nombre):
        self.nombre = nombre
        self.conocidos = list()

    def conocer(self, humano):
        self.conocidos.append(humano)
        print(
            "Mi nombre es " + self.nombre + ", un gusto conocerte " + humano.apodo)

    def saludar(self, humano):
        no_lo_conoce = True
        for _humano in self.conocidos:
            if _humano.nombre == humano:
                no_lo_conoce = False
                print("Hola " + _humano.apodo + ", juguemos!")
                break

        if no_lo_conoce:
            print("Grr, " + humano + " fuera de aqui")


class Humano:
    def __init__(self, nombre, apodo):
        self.nombre = nombre
        self.apodo = apodo

    def __repr__(self):
        return self.nombre + " " + self.apodo


entrada = input()
perrito = Perrito(entrada.split(" ")[1])
entrada = input()
while not entrada == 'perritos':
    entrada = entrada.split(" ")
    if entrada[0] == "Humano":
        humano = Humano(entrada[1], entrada[2])
    else:
        if entrada[0] == "Saluda":
            perrito.saludar(entrada[1])
        else:
            perrito.conocer(humano)
    entrada = input()

