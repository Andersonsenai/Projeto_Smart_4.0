import requests
from auth_mock import gerar_token

BASE_URL = "http://localhost:8000"

def test_acesso_sem_token():
    response = requests.get(f"{BASE_URL}/admin-data")
    assert response.status_code == 401 # Valida HTTP 401

def test_acesso_com_token_sem_permissao():
    token_operator = gerar_token("OPERATOR")
    headers = {"Authorization": f"Bearer {token_operator}"}
    
    response = requests.get(f"{BASE_URL}/admin-data", headers=headers)
    assert response.status_code == 403 # Valida HTTP 403

def test_acesso_com_token_correto():
    token_admin = gerar_token("ADMIN")
    headers = {"Authorization": f"Bearer {token_admin}"}
    
    response = requests.get(f"{BASE_URL}/admin-data", headers=headers)
    assert response.status_code == 200 # Valida HTTP 200 (Happy Path)