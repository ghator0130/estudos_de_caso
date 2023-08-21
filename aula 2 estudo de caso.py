class Fracao:
  def __init__(self, numerador, denominador):
    self.numerador = numerador
    self.denominador = denominador

  def __add__(self, other):
    num = self.numerador * other.denominador + other.numerador * self.denominador
    den = self.denominador * other.denominador
    return Fracao(num, den)

  def __sub__(self, other):
    num = self.numerador * other.denominador - other.numerador * self.denominador
    den = self.denominador * other.denominador
    return Fracao(num, den)

  def __mul__(self, other):
    num = self.numerador * other.numerador
    den = self.denominador * other.denominador
    return Fracao(num, den)

  def __truediv__(self, other):
    num = self.denominador * other.denominador
    den = self.numerador * other.numerador
    return Fracao(num, den)

  def __str__(self):
    return f"{self.numerador}/{self.denominador}"

  def __repr__(self):
    return f"Fracao({self.numerador}, {self.denominador})"

a = Fracao(1, 2)
b = Fracao(3, 4)

print(str(a + b))
print(str(a - b))
print(str(a * b))
print(str(a / b))

class Fracao:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def soma(self, other):
        num = self.numerador * other.denominador + other.numerador * self.denominador
        den = self.denominador * other.denominador
        return Fracao(num, den)

    def subtracao(self, other):
        num = self.numerador * other.denominador - other.numerador * self.denominador
        den = self.denominador * other.denominador
        return Fracao(num, den)

    def multiplicacao(self, other):
        num = self.numerador * other.numerador
        den = self.denominador * other.denominador
        return Fracao(num, den)

    def divisao(self, other):
        num = self.denominador * other.denominador
        den = self.numerador * other.numerador
        return Fracao(num, den)

    def __str__(self):
        return f"{self.numerador}/{self.denominador}"

a = Fracao(1, 2)
b = Fracao(3, 4)

# Soma
resultado_soma = a.soma(b)
print(f"Soma: {resultado_soma}")

# Subtração
resultado_subtracao = a.subtracao(b)
print(f"Subtração: {resultado_subtracao}")

# Multiplicação
resultado_multiplicacao = a.multiplicacao(b)
print(f"Multiplicação: {resultado_multiplicacao}")

# Divisão
resultado_divisao = a.divisao(b)
print(f"Divisão: {resultado_divisao}")