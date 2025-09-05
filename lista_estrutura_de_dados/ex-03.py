from collections import defaultdict
palavras = ["amor", "roma", "mora", "ramo", "omar", "ator", "rato", "tora", "rota", "taro", "casa", "saça", "acas", "asac", "mar", "ram"]

anagramas = dict()

for palavra in palavras:
    key = ''.join(sorted(palavra))
    if key not in anagramas:
        anagramas[key] = [palavra]
    else:
        anagramas[key].append(palavra)
        
print(list(anagramas.values()))