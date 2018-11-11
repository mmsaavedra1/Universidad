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


def filtrado_complemento(mensaje):
    # Se deja todo igual para filtrar por lista
    mensaje = mensaje.replace("|", "&")
    mensaje = mensaje.replace("/", "&")
    mensaje = mensaje.replace("_", "&")
    mensaje = mensaje.replace("-", "&")
    mensaje = mensaje.replace(",", "&")
    mensaje = mensaje.replace(";", "&")
    mensaje = mensaje.replace("*", "&")

    lista = mensaje.split("&")
    lista_ingredientes = list()

    for i in range(0, len(lista), 3):
        lista_ingredientes.append(
            [lista[i], lista[i + 1], float(lista[i + 2])])
        lista_ingredientes.append(
            [lista[i + 1], lista[i], float(lista[i + 2])])

    return lista_ingredientes


class Ingrediente:
    def __init__(self, nombre, tipo, puntaje):
        self.nombre = nombre
        self.tipo = tipo
        self.puntaje = puntaje

    def __str__(self):
        return self.nombre


class Receta:
    def __init__(self, restricciones):
        self.lista_ingredientes = list()
        self.puntaje_total = 0
        self.restricciones = restricciones

    def agregar_ingrediente(self, ingrediente):
        aux = list()
        for datos in self.restricciones:
            aux.append(datos[0])

        if ingrediente.tipo in aux:
            for restriccion in self.restricciones:
                if (restriccion[0] == ingrediente.tipo):
                    if (restriccion[1] > 0):
                        if ingrediente not in self.lista_ingredientes:
                            self.lista_ingredientes.append(ingrediente)
                            restriccion[1] -= 1
                            return 0
                        else:
                            return 1
                    else:
                        return 2

        else:
            if ingrediente not in self.lista_ingredientes:
                self.lista_ingredientes.append(ingrediente)
                return 0
            else:
                return 1

    def quitar_ingredientes(self, ingrediente):
        aux = list()
        for datos in self.restricciones:
            aux.append(datos[0])

        if ingrediente.tipo in aux:
            for restriccion in self.restricciones:
                if (restriccion[0] == ingrediente.tipo):
                    if ingrediente in self.lista_ingredientes:
                        indice = self.lista_ingredientes.index(ingrediente)
                        eliminado = self.lista_ingredientes.pop(indice)
                        restriccion[1] += 1
                        return 0
                    else:
                        return 1

        else:
            if ingrediente in self.lista_ingredientes:
                indice = self.lista_ingredientes.index(ingrediente)
                eliminado = self.lista_ingredientes.pop(indice)
                return 0

            else:
                return 1

    def calcular_puntaje(self, lista_complementos):
        ingredientes_ya_analizados = list()

        # Itera en la lista de ingredientes
        for ingrediente in self.lista_ingredientes:
            esta_solo = True
            # Itera en la lista de complementos
            for complemento in lista_complementos:
                # 1º Filtro para analisis
                if ingrediente.nombre == complemento[0]:
                    # Itera en la lista de ingredientes
                    for ingrediente_complemento in self.lista_ingredientes:
                        # 2º Filtro para analisis
                        if ingrediente_complemento.nombre == complemento[1]:
                            lista_analisis = sorted(
                                [complemento[0], complemento[1]])
                            # 3º Filtro
                            if lista_analisis not in ingredientes_ya_analizados:
                                self.puntaje_total += (
                                                      ingrediente.puntaje + ingrediente_complemento.puntaje) * \
                                                      complemento[2]
                                ingredientes_ya_analizados.append(
                                    lista_analisis)
                                esta_solo = False
                                break

            # 4º Filtro para analisis
            for par in ingredientes_ya_analizados:
                if (ingrediente.nombre == par[0]) or (
                    ingrediente.nombre == par[1]):
                    esta_solo = False
                    break

            # Si pasa todos los filtros y efectivamente esta solo
            if esta_solo:
                self.puntaje_total += ingrediente.puntaje

        return round(self.puntaje_total, 1)


        ############## RUN ###############


# Se guardan todos los ingredientes y los complementos
entrada = input()
lista_ingredientes = filtrado(entrada)

entrada = input()
lista_complementos = filtrado_complemento(entrada)

# Cantida de restricciones
restricciones = int(input())
tipo_de_alimento = list()

for _ in range(restricciones):
    instruccion = input().split(" ")
    tipo_de_alimento.append([instruccion[0][:-1], int(instruccion[1])])

# Se genera la instancia de receta
receta = Receta(tipo_de_alimento)

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
        elif retorno == 1:
            print("Error:", ingrediente.nombre, "ya esta en la receta")
        else:
            print("Error: no puedes agregar mas ingredientes del tipo",
                  ingrediente.tipo)

    else:
        retorno = receta.quitar_ingredientes(lista_ingredientes[indice])
        # Se imprimen los mensajes en pantalla
        if retorno == 0:
            print("Quitado:", ingrediente.nombre)
        else:
            print("Error:", ingrediente.nombre, "no esta en la receta")

# Se imprimen los ingredientes que quedaron en la receta en orden
receta.lista_ingredientes.sort(key=lambda x: x.nombre)

############## RUN ###############


########## NO PUEDES MODIFICAR ESTE CÓDIGO ############
for ingrediente in receta.lista_ingredientes:
    print(ingrediente)
print(receta.calcular_puntaje(lista_complementos))