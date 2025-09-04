from random import randint

def transpor_matriz(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])

    matriz_transposta = [[0] * linhas for _ in range(colunas)]

    for i in range(linhas):
        for j in range(colunas):
            matriz_transposta[j][i] = matriz[i][j]
    
    return matriz_transposta


def print_matriz(matriz):
    
    for linha in matriz:
        print(linha)
    print()

matriz = [[randint(1,10)] * 5 for _ in range(randint(3,10))]

print_matriz(matriz)

print_matriz(transpor_matriz(matriz))




