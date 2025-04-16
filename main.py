"""
Gerador de senhas aleatórias com comprimento personalizado.
"""

import random
import string

def gerar_senha(tamanho=12):
    """Gera uma senha aleatória com o comprimento especificado."""
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(tamanho))

if __name__ == "__main__":
    try:
        tamanho = int(input("Digite o comprimento desejado para a senha: "))
        if tamanho <= 0:
            raise ValueError("O comprimento deve ser maior que zero.")
        senha_gerada = gerar_senha(tamanho)
        print(f"Sua senha gerada é: {senha_gerada}")
    except ValueError as erro:
        print(f"Entrada inválida: {erro}")
