class Estudiante:
    def __init__(self, nombre, apellido, edad, carrera):
        self.nombre = nombre + " " + apellido
        self.edad = edad
        self.carrera = carrera


nombre, apellido, edad, carrera = input().split(" ")

estudiante = Estudiante(nombre, apellido, edad, carrera)
print(estudiante.nombre)
print(estudiante.edad)
print(estudiante.carrera)