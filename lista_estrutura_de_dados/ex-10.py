documentos = {
'doc1': "o céu é azul",
'doc2': "o sol é amarelo e o céu é vasto",
'doc3': "a lua brilha no céu azul"
}

output = {}

for k, v in documentos.items():
    for palavra in v.split():
        if palavra not in output:
            output[palavra] = {k}
        else:
            output[palavra].add(k)

print(output)