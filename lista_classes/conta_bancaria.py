class ContaBancaria:
    def __init__(self, saldo, titular):
        self.__saldo = saldo
        self.__titular = titular

    
    def depositar(self, valor):
        if valor <= 0:
            print("O valor que deseja depositar é inválido")
        else:
            self.__saldo += valor
    
    def sacar(self, valor):
        if valor > self.__saldo:
            print("Saldo insuficiente.")
        elif valor < 0:
            print("O valor que deseja sacar é inválido.")
        else:
            self.__saldo -= valor
    
    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def titular(self):
        return self.__titular

    
    @saldo.setter
    def saldo(self, valor):
        raise Exception("Operação Invalida")

    
    @titular.setter
    def titular(self, nome_titular):
        if not nome_titular:
            raise Exception("O nome não pode estar vazio")


c1 = ContaBancaria(1000, "teste_user")

print(c1.saldo)
c1.depositar(500)
print(c1.saldo)
c1.sacar(750)
print(c1.saldo)
#c1.titular = ""
print(c1.titular)


    
