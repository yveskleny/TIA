senhas_validas = ["1234", "A4B3", "C9D8"]

while True:
    senha_usuario = input("Digite sua senha: ")
    if senha_usuario in senhas_validas:
        print("Acesso permitido!")
        break
    print("Acesso negado. Tente Novamente.")