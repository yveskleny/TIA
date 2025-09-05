prerequisitos = {
'Cálculo II': {'Cálculo I'},
'Física II': {'Física I', 'Cálculo I'},
'Algoritmos Avançados': {'Estrutura de Dados'},
'Estrutura de Dados': {'Algoritmos Básicos'}
}

caminho_proposto = ['Cálculo I', 'Física I', 'Cálculo II', 'Física II']

caminho_invalido = ['Física II', 'Física I', 'Cálculo I']

def validador_de_caminho_de_cursos(prerequisitos, caminho_proposto):
    cursadas = []

    for curso in caminho_proposto:
        if curso not in prerequisitos:
            cursadas.append(curso)
        else:
            for requisito in prerequisitos[curso]:
                if requisito not in cursadas:
                    return False
            cursadas.append(curso)

    return True


print(validador_de_caminho_de_cursos(prerequisitos, caminho_invalido))