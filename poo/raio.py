from math import pi

class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return f"Area: {round(self.raio**2 * pi, 2)}"

    def calcular_perimetro(self):
        return f"Perimentro: {round(2*pi*self.raio, 2)}"

    

c1 = Circulo(5)
c2 = Circulo(2)

print(c1.calcular_area())
print(c1.calcular_perimetro())

print(c2.calcular_area())
print(c2.calcular_perimetro())
