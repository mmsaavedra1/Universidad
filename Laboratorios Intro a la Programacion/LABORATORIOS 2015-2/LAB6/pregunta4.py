a = """Lorem ipsum ad his scripta blandit partiendo, eum fastidii
accumsan euripidis in, eum liber hendrerit an. Qui ut wisi vocibus
suscipiantur, quo dicit ridens inciderint id. Quo mundi lobortis refor
midans eu, legimus senserit definiebas an eos. Eu sit tincidunt incor
rupte definitionem, vis mutat affert percipit cu, eirmod consectetu
er signiferumque eu per. In usu latine equidem dolores. Quo no fall
i viris intellegam, ut fugit veritus placerat per."""

def strPropiedades(s):
    lista = s.split()
    carac = len(s)
    num = len(lista)
    promedio = sum([len(x) for x in lista]) / num
    espacios = num - 1
    punt = 0
    for i in s:
        if not i.isdigit() and not i.isalpha():
            punt += 1

    return num, carac, promedio, espacios, punt

print(strPropiedades(a))