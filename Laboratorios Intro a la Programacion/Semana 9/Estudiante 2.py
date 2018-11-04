class Estudiante:
    def __init__(self, nombre, apellido, edad, carrera):
        self.nombre = nombre + " " + apellido
        self.edad = edad
        self.carrera = carrera
        self.notas = list()

    def agregar_nota(self, nota):
        self.notas.append(nota)

    def calcular_promedio(self):
        promedio = 0
        for i in notas:
            promedio += float(i)
        return promedio / len(notas)


lista = input().split(" ")
nombre, apellido, edad, carrera = lista[:4]
notas = lista[4:]

# Codigo
estudiante = Estudiante(nombre, apellido, edad, carrera)
for nota in notas:
    estudiante.agregar_nota(nota)

print(estudiante.nombre)
print(estudiante.edad)
print(estudiante.carrera)
print(estudiante.calcular_promedio())