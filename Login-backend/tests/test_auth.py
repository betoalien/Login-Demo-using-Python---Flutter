from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

# No es necesario importar los fixtures (client, db_session), pytest los inyecta mágicamente.

def test_create_user_success(client: TestClient):
    """
    Prueba el registro exitoso de un nuevo usuario.
    """
    response = client.post(
        "/api/users/",
        json={"email": "testuser@example.com", "password": "testpassword123"},
    )
    assert response.status_code == 201, response.text
    data = response.json()
    assert data["email"] == "testuser@example.com"
    assert "id" in data
    # Asegurarnos de que la contraseña no se devuelve
    assert "hashed_password" not in data

def test_create_user_duplicate_email(client: TestClient):
    """
    Prueba que no se puede registrar un usuario con un email que ya existe.
    """
    # Primero, creamos un usuario
    client.post(
        "/api/users/",
        json={"email": "duplicate@example.com", "password": "testpassword123"},
    )
    # Luego, intentamos crearlo de nuevo
    response = client.post(
        "/api/users/",
        json={"email": "duplicate@example.com", "password": "anotherpassword"},
    )
    assert response.status_code == 400, response.text
    assert "Email already registered" in response.json()["detail"]

def test_login_for_access_token_success(client: TestClient):
    """
    Prueba el inicio de sesión exitoso y la obtención de un token.
    """
    # Primero, creamos el usuario con el que vamos a iniciar sesión
    client.post(
        "/api/users/",
        json={"email": "loginuser@example.com", "password": "correctpassword"},
    )
    # Ahora, intentamos iniciar sesión
    login_response = client.post(
        "/api/token",
        data={"username": "loginuser@example.com", "password": "correctpassword"},
    )
    assert login_response.status_code == 200, login_response.text
    data = login_response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

def test_login_wrong_password(client: TestClient):
    """
    Prueba el fallo de inicio de sesión con una contraseña incorrecta.
    """
    client.post(
        "/api/users/",
        json={"email": "wrongpass@example.com", "password": "correctpassword"},
    )
    login_response = client.post(
        "/api/token",
        data={"username": "wrongpass@example.com", "password": "wrongpassword"},
    )
    assert login_response.status_code == 401, login_response.text
    assert "Incorrect email or password" in login_response.json()["detail"]

def test_read_current_user_success(client: TestClient):
    """
    Prueba el acceso a una ruta protegida con un token válido.
    """
    # 1. Registrar usuario
    client.post(
        "/api/users/",
        json={"email": "protected@example.com", "password": "password123"},
    )
    # 2. Iniciar sesión para obtener el token
    login_response = client.post(
        "/api/token",
        data={"username": "protected@example.com", "password": "password123"},
    )
    token = login_response.json()["access_token"]
    
    # 3. Acceder a la ruta protegida con el token
    headers = {"Authorization": f"Bearer {token}"}
    profile_response = client.get("/api/users/me", headers=headers)
    
    assert profile_response.status_code == 200, profile_response.text
    data = profile_response.json()
    assert data["email"] == "protected@example.com"

def test_read_current_user_no_token(client: TestClient):
    """
    Prueba que no se puede acceder a una ruta protegida sin un token.
    """
    response = client.get("/api/users/me")
    assert response.status_code == 401, response.text
    assert response.json()["detail"] == "Not authenticated"
