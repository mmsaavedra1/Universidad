class FechaHora:

    dd = mm = aaaa = 0
    HH = MM = SS = 0

    def __init__(self):
        pass

    def __str__(self):
        return str(self.aaaa)+"/"+str(self.mm)+"/"+str(self.dd)+" "+str(self.HH)+":"+str(self.MM)+":"+(str(self.SS) if self.SS != 0 else "00")

    def fijarFechaHora(self, a):

        sep = a.split()

        fecha = sep[0].replace("/", "-").split("-")
        hora = sep[1].split(":")

        self.dd = int(fecha[0])
        self.mm = int(fecha[1])
        self.aaaa = int(fecha[2])

        self.HH = int(hora[0])
        self.MM = int(hora[1])
        self.SS = int(hora[2])

    def fijarHora(self, a):

        hora = a.split(":")

        self.HH = int(hora[0])
        self.MM = int(hora[1])
        self.SS = int(hora[2])

    def fijarFecha(self, a):

        fecha = a.split("/").split("-")

        self.dd = int(fecha[0])
        self.mm = int(fecha[1])
        self.aaaa = int(fecha[2])

    def cambiar(self, a):
        num = int(a.split("=")[1])
        if a[0] == 'd' and num > 0 and num <= 31:
            self.dd = num
        elif a[0] == 'm' and num > 0 and num <= 12:
            self.mm = num
        elif a[0] == 'a':
            self.aaaa = num
        elif a[0] == "H" and num > 0 and num <= 24:
            self.HH = num
        elif a[0] == "M" and num > 0 and num <= 60:
            self.MM = num
        elif a[0] == "S" and num > 0 and num <= 60:
            self.SS = num
        else:
            print("Error")
