personas = input()
lista_ordenada = list()
lista_personas = personas.split(";")

for persona in lista_personas:
    _persona = persona.split(",")
    lista_ordenada.append(_persona)

# Se ordenan normales/preferencial
preferencial = list()
normal = list()

for persona in lista_ordenada:
    if persona[1] != "None":
        preferencial.append(persona)
    else:
        normal.append(persona)

# Se ordenan preferenciales colados/no colados
preferencial_colado = list()
preferencial_no_colado = list()

for persona in preferencial:
    if persona[2] == "True":
        preferencial_colado.append(persona)
    else:
        preferencial_no_colado.append(persona)

# Se oredenan normales colados/no colados
normal_colado = list()
normal_no_colado = list()

for persona in normal:
    if persona[2] == "True":
        normal_colado.append(persona)
    else:
        normal_no_colado.append(persona)

# Se imprime
for persona in preferencial_no_colado:
    print(persona)

for persona in normal_no_colado:
    print(persona)

for persona in preferencial_colado:
    print(persona)

for persona in normal_colado:
    print(persona)