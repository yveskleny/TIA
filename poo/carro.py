class Carro:
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

    def exibir_informacoes(self):
        return f"{self.marca} {self.modelo}, Ano: {self.ano}"
    
    def acelerar(self):
        return f"O {self.marca} {self.modelo} está acelerando."

    def frear(self):
        return f"O {self.marca} {self.modelo} está freando."      
    
    def reproduzir_musica(self, musica):
        return f"Tocando a música: {musica}"

    def buzinar(self):
        return "Buzinando: Beep Beep!"  


carro1 = Carro("Fiat", "Uno", "2025", "Vermelho")
print(carro1.acelerar())