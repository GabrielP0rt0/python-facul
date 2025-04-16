import random
import string


def gerar_senha(comprimento=12):
    return "".join(
        random.choice(string.ascii_letters + string.digits + string.punctuation)
        for _ in range(comprimento)
    )


if __name__ == "__main__":
    try:
        comprimento = int(input("Digite o comprimento desejado para a senha: "))
        if comprimento <= 0:
            raise ValueError("O comprimento deve ser maior que zero.")
        senha = gerar_senha(comprimento)
        print(f"Sua senha gerada é: {senha}")
    except ValueError as e:
        print(f"Entrada inválida: {e}")
