jogadores = [
    {'nome': 'Carla', 'pontuacao': 85},
    {'nome': 'Davi', 'pontuacao': 90},
    {'nome': 'Ana', 'pontuacao': 90},
    {'nome': 'Beto', 'pontuacao': 80}
]



print(sorted(jogadores, key=lambda item: (-item['pontuacao'], item['nome'])))
    
