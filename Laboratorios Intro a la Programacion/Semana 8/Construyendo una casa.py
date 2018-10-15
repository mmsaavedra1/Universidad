class Casa:
    def __init__(self, propietario, pisos, habitantes):
        self.propietario = propietario
        self.pisos = pisos
        self.habitantes = habitantes

if __name__ == '__main__':
  propietario, pisos, habitantes = input().split()

  c = Casa(propietario, pisos, habitantes)

  print(c.propietario)
  print(c.pisos)
  print(c.habitantes)