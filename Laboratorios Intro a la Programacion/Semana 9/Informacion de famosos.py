class Famoso:
    def __init__(self, nombre, _id, altura, fecha):
        self.nombre = nombre
        self.id = _id
        self.altura = altura
        self.fecha = fecha


class PUCWood:
    def __init__(self):
        self.famosos = list()

    def agregar_famoso(self, famoso):
        self.famosos.append(famoso)

    def filtrar_por_altura(self, simbolo, altura):
        for famoso in self.famosos:
            if simbolo == "<=":
                if famoso.altura <= altura:
                    print(famoso.nombre)
            elif simbolo == ">=":
                if famoso.altura >= altura:
                    print(famoso.nombre)
            else:
                if famoso.altura == altura:
                    print(famoso.nombre)

    def filtrar_por_nombre(self, string):
        for famoso in self.famosos:
            if string in famoso.nombre:
                print(famoso.nombre)


######## PROGRAMA ########

# Se almacenan los famosos
puc = PUCWood()

M = int(input())
for i in range(M):
    nombre, _id, altura, fecha = input().split(",")
    puc.agregar_famoso(Famoso(nombre, _id, altura, fecha))

# Se realizan las consultas
N = int(input())
for i in range(N):

    consulta = input().split(" ")

    # Se filtran las consultas
    if consulta[0] == "altura":
        simbolo, altura = consulta[1:]
        puc.filtrar_por_altura(simbolo, altura)
    else:
        string = consulta[1]
        puc.filtrar_por_nombre(string)