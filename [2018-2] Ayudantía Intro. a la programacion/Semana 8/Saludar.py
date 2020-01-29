class Perrito:
    def __init__(self, nombre, humano):
        self.nombre = nombre
        self.humano = humano

    def saludar(self):
        print(
            "Mi nombre es " + self.nombre + " y amo jugar con " + self.humano)


perrito, companero = input().split()
# Completar
perro = Perrito(perrito, companero)
perro.saludar()