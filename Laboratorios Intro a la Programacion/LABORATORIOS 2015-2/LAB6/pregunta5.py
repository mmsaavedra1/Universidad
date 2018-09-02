class Codificador:

    clave = mensaje = codificado = None

    def __init__(self, clave):
        self.clave = clave

    def codificador(self, mensaje):
        self.mensaje = mensaje
        self.codificado = ''
        for i in mensaje:
            if i.islower():
                char = chr(ord('z') - ord(i) + ord('a'))
            elif i.isupper():
                char = chr(ord('Z') - ord(i) + ord('A'))
            else:
                char = ' '
            self.codificado += char

    def imprimir(self, intento):
        if intento == self.clave:
            print(self.mensaje)
        else:
            print(self.codificado)