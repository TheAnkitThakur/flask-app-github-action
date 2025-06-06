from app import create_app

def test_home_route():
    app = create_app()
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello from Flask CI/CD App!" in response.data
