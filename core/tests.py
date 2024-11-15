import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Colecao
from django.contrib.auth.models import User

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def user(db):
    return User.objects.create_user(username="testuser", password="testpass")

@pytest.fixture
def colecao(user):
    return Colecao.objects.create(nome="Minha Coleção", colecionador=user)

def test_criacao_colecao(api_client, user):
    api_client.force_authenticate(user=user)
    url = reverse("colecao-list-create")
    data = {"nome": "Nova Coleção", "descricao": "Descrição da coleção"}
    response = api_client.post(url, data)
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data["nome"] == "Nova Coleção"
    assert response.data["colecionador"] == user.id

def test_permissao_edicao_colecao(api_client, user, colecao):
    api_client.force_authenticate(user=user)
    url = reverse("colecao-detail", args=[colecao.id])
    data = {"nome": "Coleção Atualizada", "descricao": "Descrição atualizada"}
    response = api_client.put(url, data)
    assert response.status_code == status.HTTP_200_OK
    assert response.data["nome"] == "Coleção Atualizada"

def test_permissao_usuario_nao_autenticado(api_client, colecao):
    url = reverse("colecao-detail", args=[colecao.id])
    response = api_client.delete(url)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

def test_listagem_colecoes(api_client, user, colecao):
    api_client.force_authenticate(user=user)
    url = reverse("colecao-list-create")
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) > 0