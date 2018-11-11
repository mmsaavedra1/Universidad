####### ESCRIBE TU CODIGO AQUI #######
def filtrado(mensaje):
    # Se deja todo igual para filtrar por lista
    mensaje = mensaje.replace("|", "&")
    mensaje = mensaje.replace("/", "&")
    mensaje = mensaje.replace(".", "&")
    mensaje = mensaje.replace("_", "&")
    mensaje = mensaje.replace("-", "&")
    mensaje = mensaje.replace(",", "&")
    mensaje = mensaje.replace(";", "&")
    mensaje = mensaje.replace("*", "&")

    lista = mensaje.split("&")
    lista_ingredientes = list()

    for i in range(0, len(lista), 3):
        lista_ingredientes.append(
            Ingrediente(lista[i], lista[i + 1], int(lista[i + 2])))

    return sorted(lista_ingredientes, key=lambda x: x.nombre)


class Ingrediente:
    def __init__(self, nombre, tipo, puntaje):
        self.nombre = nombre
        self.tipo = tipo
        self.puntaje = puntaje

    def __str__(self):
        return self.nombre


######################################

entrada = input()
lista_ingredientes = filtrado(entrada)

for i in lista_ingredientes:
    print(i)