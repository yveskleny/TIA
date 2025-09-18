class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

    def exibir_dados(self):
        print(f"Produto: {self.nome} | Preço: {self.valor}")

class Pedido:
    def __init__(self, data):
        self.data = data
        self.lista_produtos = []

    
    def adicionar_produto(self, produto):
        self.lista_produtos.append(produto)
        print("Produto Adicionado ao pedido!")
    
    def fechar_pedido(self):
        total = 0
        for produto in self.lista_produtos:
            total += produto.valor

        return total