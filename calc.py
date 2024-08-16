class Calculator:
    def __init__(self, fff, ddd):
        self.ddd = ddd
        self.fff = fff
    def __add__(self):
        self.fff = int(input('Первое значение:'))
        self.ddd = int(input('Второе значение:'))
        f = self.ddd + self.fff
        return print(f)
    def __sub__(self):
        f = self.fff - self.ddd
        return print(f)
    def __mul__(self):
        f = self.ddd * self.fff
        return print(f)
    def __truediv__(self):
        f = self.fff / self.ddd
        return print(f)

gfhhg = Calculator(None, None)
gfhhg.__add__()
gfhhg.__sub__()
gfhhg.__mul__()
gfhhg.__truediv__()