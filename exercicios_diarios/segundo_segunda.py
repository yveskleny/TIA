precos_frutas = { 'maçã': 2.50, 'banana': 1.75, 'laranja': 3.00, 'uva': 4.50 }

nome_fruta = input("Digite o nome da fruta que deseja consultar: ").lower()

try:
    print(f"O preço da {nome_fruta} é R$ {precos_frutas[nome_fruta]:.2f}")
except KeyError:
    print(f"Desculpe, a fruta {nome_fruta} não foi encontrada em nosso catálogo.")