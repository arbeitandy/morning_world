import pytest
import json
from morning_world import create_app

def test_config():
    """test: create_app with default test config"""
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing

def test_root_path_get_200(client):
    r = client.get('/', headers={'Accept':''})
    assert r.status_code == 200
    assert r.data == b'<p>Morning World!</p>'


def test_root_path_json_200(client):
    r = client.get('/', headers={'Accept':'application/json'})
    assert r.status_code == 200
    assert r.headers['Content-Type'] == 'application/json'
    assert json.loads(r.data) == {"message": "Good morning"}
"""
def test_root_path_get_404(client):
    r = client.get('/failcase', headers={'Accept':''})
    assert r.status_code == 404

def test_root_path_json_404(client):
    r = client.get('/failcase', headers={'Accept':'application/json'})
    assert r.status_code == 404
"""

""" testing additional methods """
def test_root_path_json_name(client):
    r = client.get('john?lang=en', headers={'Accept':'application/json'})
    assert json.loads(r.data) == { "msgs": ["Hello john!"] }

def test_root_path_json_name_es(client):
    r = client.get('john?lang=es', headers={'Accept':'application/json'})
    assert json.loads(r.data) == { "msgs": ["Hola john!"] }

@pytest.fixture
def app():
    app = create_app({'TESTING': True,})
    yield app

@pytest.fixture
def client(app):
    return app.test_client()
