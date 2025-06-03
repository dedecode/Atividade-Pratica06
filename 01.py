import random
import string

def gerar_senha_aleatoria():
    print("Gerador de Senha Aleatória")
    while True:
        try:
            quantidade_caracteres = int(input("Quantos caracteres a senha deve ter? "))
            if quantidade_caracteres <= 0:
                print("Por favor, digite um número positivo.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for i in range(quantidade_caracteres))
    print(f"Sua senha gerada é: {senha}")

gerar_senha_aleatoria()
