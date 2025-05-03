"""Testes unitários para a API FastAPI de geração de senhas."""

import string
from fastapi.testclient import TestClient
from main import app, gerar_senha

client = TestClient(app)

# --- Testes da função gerar_senha() ---


def test_senha_tem_16_caracteres():
    """Verifica se a senha gerada tem exatamente 16 caracteres."""
    senha = gerar_senha()
    assert len(senha) == 16


def test_senha_contem_caracteres_validos():
    """Verifica se a senha contém apenas caracteres válidos."""
    senha = gerar_senha()
    caracteres_validos = string.ascii_letters + string.digits + string.punctuation
    for c in senha:
        assert c in caracteres_validos


def test_senhas_sao_diferentes():
    """Verifica se a função gera senhas diferentes entre execuções."""
    senha1 = gerar_senha()
    senha2 = gerar_senha()
    assert senha1 != senha2


# --- Testes do endpoint /senha ---


def test_endpoint_status_code_200():
    """Verifica se o endpoint /senha responde com status HTTP 200."""
    response = client.get("/senha")
    assert response.status_code == 200


def test_resposta_contem_chave_senha():
    """Verifica se a resposta JSON contém a chave 'senha'."""
    response = client.get("/senha")
    data = response.json()
    assert "senha" in data


def test_senha_do_endpoint_tem_16_caracteres():
    """Verifica se a senha retornada pelo endpoint tem 16 caracteres."""
    response = client.get("/senha")
    senha = response.json()["senha"]
    assert len(senha) == 16


def test_senha_do_endpoint_tem_caracteres_validos():
    """Verifica se a senha da resposta contém apenas caracteres válidos."""
    response = client.get("/senha")
    senha = response.json()["senha"]
    caracteres_validos = string.ascii_letters + string.digits + string.punctuation
    for c in senha:
        assert c in caracteres_validos
