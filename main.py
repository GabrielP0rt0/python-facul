from fastapi import FastAPI
import random
import string

app = FastAPI()

def gerar_senha(comprimento=16):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(comprimento))

@app.get("/senha")
def obter_senha():
    senha = gerar_senha()
    return {"senha": senha}
