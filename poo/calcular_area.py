from math import pi

class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return f"Area: {round(self.raio**2 * pi, 2)}"

    def calcular_perimetro(self):
        return f"Perimentro: {round(2*pi*self.raio, 2)}"

    
class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return f"Area: {self.base * self.altura}"

    def calcular_perimetro(self):
        return f"Perimetro: {2*(self.base + self.altura)}"


