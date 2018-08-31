from pprint import pprint

# Diccionario que almacena una pareja de grupos por
parejas_por_tema = {
    "AFP": list(),
    "Politicas de drogas": list(),
    "Soluciones privadas": list(),
    "Ingreso basico": list(),
    "Regulacion de monopolios": list(),
    "Mercado de organos": list(),
    "Keynes vs Hayek": list(),
    "Inmigracion": list(),
    "Bajar o subir impuestos": list(),
    "Politicas de cluster": list(),
    "Moneda unica para Latinoamerica": list(),
    "Criptomonedas": list()
}

# Lista de grupos con preferencias por orden de respuesta
# Esta la modificare cuando reciba las prioridades
grupo_1 = {"1": ["AFP", "Soluciones privadas", "Ingreso basico"]}
grupo_2 = {"2": ["Criptomonedas", "Regulacion de monopolios"]}
grupo_3 = {"3": ["Inmigracion", "AFP"]}
grupo_4 = {"4": ["Bajar o subir impuestos"]}
grupo_5 = {"5": ["Politicas de cluster"]}
grupo_6 = {"6": ["Criptomonedas"]}
grupo_7 = {"7": ["Criptomonedas", "AFP", "Mercado de organos"]}
grupo_8 = {"8": ["Keynes vs Hayek"]}
grupo_9 = {"9": ["Moneda unica para Latinoamerica"]}
grupo_10 = {"10": []}
grupo_11 = {"11": []}
grupo_12 = {"12": []}
grupo_13 = {"13": []}
grupo_14 = {"14": []}
grupo_15 = {"15": []}
grupo_16 = {"16": []}

# Grupos almacenados
grupos = [grupo_1, grupo_2, grupo_3, grupo_4, grupo_5, grupo_6, grupo_7,
          grupo_8, grupo_9, grupo_10, grupo_11, grupo_12, grupo_13,
          grupo_14, grupo_15, grupo_16]

# Clave de activacion de que ya hay 6 temas definidos
# Temas definidos almacenados en una lista
# Se crea una copia de la original que va mutando
contador = 0
temas_definidos = list()
_grupos = grupos.copy()


# Analisis y algoritmo de grupos

# PARTE 1º

# Se da la posibilidad de que los primeros grupos que fijen 8 temas distintos
# una vez conseguido esto, se corta esta parte y se distribuyen las parejas
# faltantes para que no quede disparejo.

for grupo in grupos:
    # Si ya se definieron 8 temas distintos se corta el ciclo
    # y se analiza de nuevo
    if contador == 8:
        break

    # Si no, se agrega la primera opcion a estas
    else:
        # Se obtienen los temas elegidos por grupo
        temas = list(grupo.values())[0]

        for tema in temas:

            if len(parejas_por_tema[tema]) < 2:

                # Se asignan los grupos a los temas
                parejas_por_tema[tema].append(list(grupo.keys())[0])

                # Se remueve el grupo que ya tiene tema
                _grupos.remove(grupo)

                # Si el tema es nuevo se agrega a la lista de temas elegidos
                if tema not in temas_definidos:
                    contador += 1
                    temas_definidos.append(tema)
                break

# PARTE 2º

# Definidos los temas ya elegidos se hace un filtro de los temas que
# aun faltan por definir

temas_restantes = list()
for tema in parejas_por_tema.keys():
    if tema not in temas_definidos:
        temas_restantes.append(tema)

# Se genera una copia que muta
_temas_restantes = temas_restantes.copy()

# Ahora se realiza el mismo algoritmo de asignacion eliminando las opciones
# recorriendo solo los grupos que aun no estan asignados

for grupo in _grupos:
    # Se obtienen los temas elegidos por grupo
    temas = list(grupo.values())[0]
    for tema in temas:
        if tema in _temas_restantes:

            # Se asignan los grupos a los temas
            parejas_por_tema[tema].append(list(grupo.keys())[0])

            # Se remueve de los temas que faltan
            _temas_restantes.remove(tema)

            # Se mata el grupo y se continua analizando
            break

pprint(parejas_por_tema)