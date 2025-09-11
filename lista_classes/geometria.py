class Vertice:
    def __init__(self, x: float = 0.0, y: float = 0.0):
        self.x = x
        self.y = y


class Retangulo:
    def __init__(self, vertice: Vertice, vertice_oposto: Vertice):
        self.vertice = vertice
        self.vertice_oposto = vertice_oposto
    
    def area(self):
        base = abs(self.vertice.x - self.vertice_oposto.x)
        altura = abs(self.vertice.y - self.vertice_oposto.y)
        return base * altura

    def perimetro(self):
        base = abs(self.vertice.x - self.vertice_oposto.x)
        altura = abs(self.vertice.y - self.vertice_oposto.y)

        return (2 * base) + (2 * altura)
    
v1 = Vertice(1,1)
v2 = Vertice(4,3)

r = Retangulo(v1, v2)

print("Area:", r.area())
print("Perimetro:", r.perimetro())