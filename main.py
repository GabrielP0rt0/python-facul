"""
Gerador de senhas aleatórias com comprimento personalizado.
"""

import random
import string

def gerar_senha(comprimento=12):
    """Gera uma senha aleatória com o comprimento especificado."""
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(comprimento))

if __name__ == "__main__":
    try:
        comprimento_usuario = int(input("Digite o comprimento desejado para a senha: "))
        if comprimento_usuario <= 0:
            raise ValueError("O comprimento deve ser maior que zero.")
        senha_gerada = gerar_senha(comprimento_usuario)
        print(f"Sua senha gerada é: {senha_gerada}")
    except ValueError as erro:
        print(f"Entrada inválida: {erro}")