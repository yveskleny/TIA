
letras = [letter for letter in "abcdefghijklmnopqrstuvwxyz"]

frase = input("Digite a frase que deseja encriptar: ").lower()
qtd_saltos = int(input("Digite quantidade de saltos que deseja realizar: "))

frase_encriptada = ""

for letra in frase:
    if letra not in letras:
        frase_encriptada += letra
        continue
    index = letras.index(letra)
    frase_encriptada += letras[(index + qtd_saltos) % 26]

print(frase_encriptada)



