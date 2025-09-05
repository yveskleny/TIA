dados_brutos = [
{'id': 1, 'nome': 'Ana', 'contato': {'email': 'ana@email.com', 'telefone': '111-111'}},
{'id': 2, 'nome': 'Beto', 'contato': {'email': 'beto@email.com', 'telefone': '222-222'}}
]


for dado in dados_brutos:
    dado.update(dado.pop("contato"))

print(dados_brutos)