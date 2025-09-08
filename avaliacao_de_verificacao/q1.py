numeros = []

for i in range(5):
    num = float(input(f"Digite a {i+1} nota: "))
    numeros.append(num)

media = sum(numeros)/len(numeros)

for i, nota in enumerate(numeros):
    print(f"Nota {i+1} é {nota:.2f}")

print(f"Média é: {media:.2f}")

