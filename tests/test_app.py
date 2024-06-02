import sys
import os
import pytest

# Dodaj katalog nadrzędny do sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import app  # Importuj aplikację z main.py

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello_world(client):
    rv = client.get('/')
    assert rv.data == b'Hello, World!'
    assert rv.status_code == 200
