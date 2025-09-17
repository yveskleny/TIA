class Retangulo:
    def __init__(self, base = 0, altura = 0):
        self.base = base
        self.altura = altura

    
    def calcular_area(self):
        return self.base * self.altura

    
r1 = Retangulo(10, 5)

area_retangulo = r1.calcular_area()

print(f"A área do retângulo é {area_retangulo}")