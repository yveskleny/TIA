class Vetor2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, outro_vetor):
        self.x += outro_vetor.x
        self.y += outro_vetor.y

    def __sub__(self, outro_vetor):
        self.x -= outro_vetor.x
        self.y -= outro_vetor.y

    def __mul__(self, escalar):
        self.x *= escalar
        self.y *= escalar

    def __str__(self):
        return f"Vetor({self.x},{self.y})"

    def __eq__(self, outro_vetor):
        if self.x == outro_vetor.x and self.y == outro_vetor.y:
            return True
        return False


v1 = Vetor2D(2, 3)
v2 = Vetor2D(2, 3)
print(v1 == v2)

v1 + v2
print(v1.__str__())
v2 + v1
print(v1.__str__())
v1 * 2
print(v1.__str__())
v2 * 3
print(v2.__str__())



