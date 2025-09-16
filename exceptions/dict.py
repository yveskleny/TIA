def temp(dictionary, dict_key):
    try:
        print(dictionary[dict_key])
    except KeyError:
        return f'Erro: A chave "{dict_key}" não existe no dicionário.'


dict1 = {'nome': 'João', 'idade': 30, 'cidade': 'Brasilia'}

print(temp(dict1, 'teste'))