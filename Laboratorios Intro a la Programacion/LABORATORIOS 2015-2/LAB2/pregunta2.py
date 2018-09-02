print("A continuacion, se le solicitaran algunos datos. Por favor entregar valores numericos para (x),")
print("valores numericos de 4 digitos para (xxxx) y 's' o 'c' para (s/c) o 'ci' o 'ca' para (ci/ca)")

ingreso = int(input("Ingrese ingreso (x): "))
edad = 2015 - int(input("Ingrese año de nacimiento (xxxx): "))
hijos = int(input("Ingrese numero de hijos (x): "))
pertenencia = int(input("Ingrese años de pertenencia al banco (x): "))
estado = input("Se encuentra soltero o casado? (s/c): ")
ubicacion = input("Vive en la ciudad o el campo? (ci/ca): ")

aprobado = False

if pertenencia > 10 and hijos >= 2:
    aprobado = True
elif estado is 'c'and hijos > 3 and edad > 45 and edad < 55:
    aprobado = True
elif ingreso > 2500000 and estado == 's' and ubicacion == "ci":
    aprobado = True
elif ingreso > 3500000 and pertenencia > 5:
    aprobado = True
elif ubicacion == "ca" and estado == 'c' and hijos < 2:
    aprobado = True

print("ACEPTADO" if aprobado else "RECHAZADO")
