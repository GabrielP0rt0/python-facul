"""
API FastAPI para gerar senhas aleatórias de 16 caracteres.
"""

import random
import string
from fastapi import FastAPI

app = FastAPI()

def gerar_senha(comprimento=16):
    """Gera uma senha aleatória com o comprimento fixo de 16 caracteres."""
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(comprimento))

@app.get("/senha")
def obter_senha():
    """Endpoint GET que retorna uma senha gerada."""
    senha = gerar_senha()
    return {"senha": senha}
