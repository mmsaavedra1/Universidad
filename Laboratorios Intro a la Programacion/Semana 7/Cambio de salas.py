lista_madre = list()

while True:
    datos = input()

    if datos == "end":
        break

    # Filtrado de informacion
    lista_datos = datos.split(":")
    lista_datos_2 = [lista_datos[0], lista_datos[1].split(";")]
    lista_datos_final = [lista_datos[0], []]

    for datos in lista_datos_2[1]:
        _datos = datos.split(",")
        lista_datos_final[1].append(_datos)

    lista_madre.append(lista_datos_final)

# Aqui comienza el programa como tal

# Filtrado de salas
salas = list()
for dato in lista_madre:
    if dato[0] not in salas:
        salas.append(dato[0])

# Filtrado de alumnos por sala
for sala in salas:
    lista = list()

    for dato in lista_madre:
        for alumno in dato[1]:
            if alumno[1] == sala:
                lista.append(alumno)

    # Se ordenan los alumnos en la sala
    alumnos = list()
    for dato in lista:
        alumnos.append(int(dato[0]))
    alumnos.sort()

    # Se imprime cada lista
    lista = list()
    for _alumno in alumnos:
        lista.append([str(_alumno), sala])

    print(sala + ":", lista)