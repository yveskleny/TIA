estoque = {'maçã': 10, 'banana': 5, 'laranja': 0}
precos = {'maçã': 2.50, 'banana': 3.00, 'laranja': 2.75}
carrinho = {'maçã': 4, 'banana': 6}

def calcula_total(estoque, precos, carrinho):
    
    produtos_indisponiveis = []
    total = 0
    for item, qtd in carrinho.items():
        if estoque[item] <= qtd:
            produtos_indisponiveis.append(item)
        else:
            total += precos[item]*carrinho[item]

    return total, produtos_indisponiveis


total_carrinho, produtos_faltantes = calcula_total(estoque, precos, carrinho)

print(f"Valor total do carrinho: R$ {total_carrinho:.2f}")
print(f"Itens indisponíveis: {produtos_faltantes}")