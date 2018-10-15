# Se almacenan los datos
m = int(input())
base_de_datos = list()

for i in range(m):
    datos = input().split(",")
    base_de_datos.append(datos)

# Se realizan las consultas
n = int(input())

for i in range(n):
    _consulta = input()
    consulta = _consulta.upper()

    # Se filtra la consulta
    datos_consulta = consulta.split(" ")
    consulta = consulta.replace(datos_consulta[0] + " ", "")

    # Se analiza si esta en la BD
    es_falso = True

    if datos_consulta[0] == "SUPERMERCADO":
        for dato in base_de_datos:
            if consulta in dato[0]:
                print(_consulta + ": True")
                es_falso = False
                break

    elif datos_consulta[0] == "CALLE":
        for dato in base_de_datos:
            if consulta in dato[1]:
                print(_consulta + ": True")
                es_falso = False
                break

    else:
        for dato in base_de_datos:
            if consulta in dato[2]:
                print(_consulta + ": True")
                es_falso = False
                break

    if es_falso:
        print(_consulta + ": False")