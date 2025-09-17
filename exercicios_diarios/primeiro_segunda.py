
try:
    ano_nascimento = int(input("Em que ano você nasceu? "))
except ValueError:
    print("Erro: Você não digitou um número válido.")
else:
    print(f"Você tem ou fará aproximadamente {2025 - ano_nascimento} anos em 2025.")
