from math import pow, sin, radians
from random import randint, choice
import os

def calculo_seno(angulo):
    return sin(radians(angulo))

for ang in range(0, 361, 30):
    print(ang, calculo_seno(ang))

print(pow(2, 3))

print(randint(0, 100))

lista = []

for i in range(10):
    lista.append(randint(0, 100))
print(lista)
print("Numero sorteado: ", choice(lista))
    

os.mkdir('./teste_folder')