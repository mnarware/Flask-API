import pytest
from hello import app

@pytest.fixture
def client():
    return app.test_client()

def test_hello(client):
    res=client.get('/')
    res.status_code== 200
    res.text =="Hey Congrats!"

def test_ping(client):
    res=client.get('/ping')
    res.status_code== 200
    res.text =="Why are you pinging me."
