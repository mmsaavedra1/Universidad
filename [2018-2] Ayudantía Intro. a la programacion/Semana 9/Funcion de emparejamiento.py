class Par:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def f(self, x, y):
        # en este método se puede implementar la función dada para determinar el orden
        return ( 1 /2 ) *(x + y ) *(x + y + 1) + y

    def menor_que(self, other):
        if self.f(self.a, self.b) < self.f(other.a, other.b):
            return True
        else:
            return False

    def mayor_que(self, other):
        if self.f(self.a, self.b) > self.f(other.a, other.b):
            return True
        else:
            return False

    def igual_que(self, other):
        if self.f(self.a, self.b) == self.f(other.a, other.b):
            return True
        else:
            return False

# Este código es para facilitar el desarrollo del ejemplo. Te sugerimos no modificarlo.
ab = Par(*map(int, input().strip(')').strip('(').split(',')))
cd = Par(*map(int, input().strip(')').strip('(').split(',')))


if ab.menor_que(cd):
    print("<")
elif ab.mayor_que(cd):
    print(">")
elif ab.igual_que(cd):
    print("==")