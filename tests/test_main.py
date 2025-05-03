import string
from fastapi.testclient import TestClient
from main import app, gerar_senha

client = TestClient(app)

# --- Testes da função gerar_senha() ---

def test_senha_tem_16_caracteres():
    senha = gerar_senha()
    assert len(senha) == 16

def test_senha_contem_caracteres_validos():
    senha = gerar_senha()
    caracteres_validos = string.ascii_letters + string.digits + string.punctuation
    for c in senha:
        assert c in caracteres_validos

def test_senhas_sao_diferentes():
    senha1 = gerar_senha()
    senha2 = gerar_senha()
    assert senha1 != senha2 


# --- Testes do endpoint /senha ---

def test_endpoint_status_code_200():
    response = client.get("/senha")
    assert response.status_code == 200

def test_resposta_contem_chave_senha():
    response = client.get("/senha")
    data = response.json()
    assert "senha" in data

def test_senha_do_endpoint_tem_16_caracteres():
    response = client.get("/senha")
    senha = response.json()["senha"]
    assert len(senha) == 16

def test_senha_do_endpoint_tem_caracteres_validos():
    response = client.get("/senha")
    senha = response.json()["senha"]
    caracteres_validos = string.ascii_letters + string.digits + string.punctuation
    for c in senha:
        assert c in caracteres_validos
