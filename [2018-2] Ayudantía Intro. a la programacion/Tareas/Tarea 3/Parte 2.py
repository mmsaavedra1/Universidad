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


class Receta:
    def __init__(self):
        self.lista_ingredientes = list()

    def agregar_ingrediente(self, ingrediente):
        if ingrediente not in self.lista_ingredientes:
            self.lista_ingredientes.append(ingrediente)
            return 0
        else:
            return 1

    def quitar_ingredientes(self, ingrediente):
        if ingrediente in self.lista_ingredientes:
            indice = self.lista_ingredientes.index(ingrediente)
            eliminado = self.lista_ingredientes.pop(indice)
            return 0

        else:
            return 1


############## RUN ###############


if __name__ == '__main__':
    # Se guardan todos los ingredientes
    entrada = input()
    lista_ingredientes = filtrado(entrada)

    # Se genera la instancia de receta
    receta = Receta()

    # Recibe las intrucciones de esta parte
    n = int(input())

    for _ in range(n):
        instruccion = input()

        # Busca el ingrediente
        for ingrediente in lista_ingredientes:
            if ingrediente.nombre == instruccion[1:]:
                indice = lista_ingredientes.index(ingrediente)
                break

        # Se llevan a cabo las operaciones de agregar o quitar
        if instruccion[0] == "+":
            retorno = receta.agregar_ingrediente(lista_ingredientes[indice])
            # Se imprimen los mensajes en pantalla
            if retorno == 0:
                print("Agregado:", ingrediente.nombre)
            else:
                print("Error:", ingrediente.nombre, "ya esta en la receta")

        else:
            retorno = receta.quitar_ingredientes(lista_ingredientes[indice])
            # Se imprimen los mensajes en pantalla
            if retorno == 0:
                print("Quitado:", ingrediente.nombre)
            else:
                print("Error:", ingrediente.nombre, "no esta en la receta")

    # Se imprimen los ingredientes que quedaron en la receta en orden
    receta.lista_ingredientes.sort(key=lambda x: x.nombre)
    for ingrediente in receta.lista_ingredientes:
        print(ingrediente)


############## RUN ###############