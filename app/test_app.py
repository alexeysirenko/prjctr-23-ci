from app import app

def test_hello():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hello, World!' in response.data

def test_test():
    client = app.test_client()
    response = client.get('/test')
    assert response.status_code == 200
    assert b'test!' in response.data