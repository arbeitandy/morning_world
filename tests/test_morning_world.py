import os
import tempfile
import pytest

from morning_world import morning_world


@pytest.fixture
def client():
    morning_world.app.config['TESTING'] = True
    client = morning_world.app.test_client()

    yield client

    
