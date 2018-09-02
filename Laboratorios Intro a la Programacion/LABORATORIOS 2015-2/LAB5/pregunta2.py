class Fraccion:

    num = den = 0

    def __init__(self, n, d):
        self.num = n
        self.den = d

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    @staticmethod
    def __gcd(a, b):
        while b: a, b = b, a%b
        return a

    @staticmethod
    def __lcm(a, b):
        return abs(a*b)/Fraccion.__gcd(a, b)

    @staticmethod
    def __prep(a, b):
        lcm = Fraccion.__lcm(a.den, b.den)
        return lcm, int((lcm/a.den) * a.num), int((lcm/b.den) * b.num)

    @staticmethod
    def suma(a, b):
        _lcm, left, right = Fraccion.__prep(a, b)
        return Fraccion(left+right, _lcm)

    def suma(self, b):
        _lcm, left, right = Fraccion.__prep(self, b)
        return Fraccion(left, right, _lcm)

    @staticmethod
    def resta(a, b):
        _lcm, left , right = Fraccion.__prep(a, b)
        return Fraccion(left - right, _lcm)

    def resta(self, b):
        _lcm, left , right = Fraccion.__prep(self, b)
        return Fraccion(left - right, _lcm)

    @staticmethod
    def producto(a, b):
        return Fraccion(a.num*b.num, a.den*b.den)

    def producto(self, b):
        return Fraccion(self.num*b.num, self.den*b.den)

    @staticmethod
    def division(a, b):
        return Fraccion(a.num*b.dem, a.den*b.num)

    def division(self, b):
        return Fraccion(self.num*b.dem, self.den*b.num)

    def tofloat(self):
        return float(self.num/self.den)

    def simplificar(self):
        # k = max(self.num, self.den) / min(self.num, self.den)
        mini = min(self.num, self.den)
        for i in reversed(range(1, mini)):
            if self.num % i == 0 and self.den % i == 0:
                self.num /= i
                self.den /= i
        self.num = int(self.num)
        self.den = int(self.den)

