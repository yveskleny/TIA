class Produto:
    def __init__(self, nome, preco, id_produto):
        self.nome = nome
        self.preco = preco
        self.id_produto = id_produto


class Carrinho:
    def __init__(self):
        self.produtos = {}

    
    def adicionar_produto(self, produto, quantidade):
        if produto not in self.produtos:
            self.produtos[produto] = quantidade
        else:
            self.produtos[produto] += quantidade
    

    def remover_produto(self, produto, quantidade):
        if quantidade >= self.produtos[produto]:
            self.produtos.pop(produto)
        else:
            self.produtos[produto] -= quantidade
    

    def calcula_total(self):
        total = 0
        for prod, qtd in self.produtos.items():
            total += (prod.preco * qtd)
        
        return total

    def exibir_carrinho(self):
        print("Nome | Quantidade | Preço Unitario | Preço agregado")
        for prod, qtd in self.produtos.items():
            print(f"{prod.nome} | {qtd} unidades | R$ {prod.preco:.2f} | R$ {(prod.preco*qtd):.2f}")
        print()
        print(f"Total Carrinho: {self.calcula_total()}")