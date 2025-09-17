class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    
    def mostrar_informacoes(self):
        print(f"Este é um {self.marca} {self.modelo} do ano {self.ano}.")

# Criando os objetos
carro1 = Carro("Toyota", "Corolla", 2022)
carro2 = Carro("Honda", "Civic", 2023)

carro1.mostrar_informacoes()
carro2.mostrar_informacoes()