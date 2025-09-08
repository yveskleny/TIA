numeros = [5, 12, 17, 8, 21, 3, 11, 40]
resultado_final = []

for num in numeros:
    if num % 2 == 1 and num > 10:
        resultado_final.append(num)

print(f"Os números ímpares e maiores que 10 são: {resultado_final}")