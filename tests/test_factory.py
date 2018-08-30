from morning_world import create_app


def test_config():
    """test: create_app with default test config"""
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing

def test_root_path(client):
    response = client.get('/')
    assert response.data == b'<p>Morning World!</p>'
