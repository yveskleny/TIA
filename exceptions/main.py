
def divisao(a, b):
    return a / b


try:
    a = int(input("Numero 1: "))
    b = int(input("Numero 2: "))
    resultado = divisao(a, b)
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero.")
except ValueError:
       print("Erro: O valor informado deve ser um número.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
else:
    print(f"O resultado da divisão é: {resultado}")
finally:
    print("Operação finalizada.") 


