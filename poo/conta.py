class Conta:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def exibir_saldo(self):
        return f"Titular: {self.titular}, Saldo: R${self.saldo:.2f}"
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return f"Depósito de R${valor:.2f} realizado com sucesso."
        else:
            return "Valor de depósito inválido."
        
    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            return f"Saque de R${valor:.2f} realizado com sucesso."
        else:
            return "Saldo insuficiente ou valor inválido."

conta1 = Conta("Alice", 1000)
conta2 = Conta("Bob", 500)
print(conta1.exibir_saldo())
print(conta1.depositar(200))
print(conta1.sacar(150))
print(conta1.exibir_saldo())
print(conta2.exibir_saldo())