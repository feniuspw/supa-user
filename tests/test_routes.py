import types
from fastapi.testclient import TestClient
from src.main import app
import src.api.auth as auth_module

client = TestClient(app)


def test_healthcheck():
    response = client.get("/healthcheck")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_login_with_email_and_password_success(mocker):
    dummy = types.SimpleNamespace(
        user=types.SimpleNamespace(id="user123"),
        session=types.SimpleNamespace(
            access_token="access",
            refresh_token="refresh",
            expires_in=3600,
            expires_at=123456,
        ),
    )
    mocker.patch.object(auth_module.AuthService, "login_with_email_and_password", return_value=dummy)
    data = {"email": "test@example.com", "password": "secret"}
    response = client.post("/login-with-email-and-password", json=data)
    assert response.status_code == 200
    assert response.json() == {
        "user_id": "user123",
        "access_token": "access",
        "refresh_token": "refresh",
        "expires_in": 3600,
        "expires_at": 123456,
    }


def test_login_with_email_and_password_failure(mocker):
    mocker.patch.object(auth_module.AuthService, "login_with_email_and_password", side_effect=Exception("fail"))
    data = {"email": "test@example.com", "password": "secret"}
    response = client.post("/login-with-email-and-password", json=data)
    assert response.status_code == 500
    assert response.json() == {"detail": "Internal Server Error"}


def test_login_with_sso_success(mocker):
    mocker.patch.object(auth_module.AuthService, "login_with_sso", return_value={"url": "http://example.com"})
    data = {"provider": "google", "redirect_to": "http://localhost"}
    response = client.post("/login-with-sso", json=data)
    assert response.status_code == 200
    assert response.json() == {"redirect_url": "http://example.com"}


def test_login_with_sso_microsoft_success(mocker):
    mocker.patch.object(auth_module.AuthService, "login_with_sso", return_value={"url": "http://example.com"})
    data = {"provider": "azure", "redirect_to": "http://localhost"}
    response = client.post("/login-with-sso", json=data)
    assert response.status_code == 200
    assert response.json() == {"redirect_url": "http://example.com"}


def test_login_with_sso_failure(mocker):
    mocker.patch.object(auth_module.AuthService, "login_with_sso", side_effect=Exception("fail"))
    data = {"provider": "google", "redirect_to": "http://localhost"}
    response = client.post("/login-with-sso", json=data)
    assert response.status_code == 500
    assert response.json() == {"detail": "Internal Server Error"}
