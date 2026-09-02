import pytest

from app import create_app


@pytest.fixture
def client():
    application = create_app()
    application.config["TESTING"] = True

    with application.test_client() as test_client:
        yield test_client


def test_index_returns_project_information(client):
    response = client.get("/")

    assert response.status_code == 200
    assert response.get_json() == {
        "name": "Automated DevSecOps Security Pipeline",
        "status": "running",
    }


def test_health_endpoint(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json() == {"status": "healthy"}


def test_security_headers(client):
    response = client.get("/")

    assert response.headers["Content-Security-Policy"] == (
        "default-src 'none'; frame-ancestors 'none'"
    )
    assert response.headers["X-Content-Type-Options"] == "nosniff"
    assert response.headers["X-Frame-Options"] == "DENY"
    assert response.headers["Referrer-Policy"] == "no-referrer"
    assert response.headers["Cache-Control"] == "no-store"


def test_unknown_route_returns_404(client):
    response = client.get("/does-not-exist")

    assert response.status_code == 404