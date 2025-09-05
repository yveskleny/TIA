dicionario_original = {'maçã': 'fruta', 'cenoura': 'legume',
'banana': 'fruta', 'brócolis': 'legume'}

dict_invertido = {}

for chave, valor in dicionario_original.items():
    if valor not in dict_invertido.keys():
        dict_invertido[valor] = [chave]
    else:
        dict_invertido[valor].append(chave)

print(dict_invertido)