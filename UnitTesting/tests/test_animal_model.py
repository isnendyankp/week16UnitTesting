import pytest
from app import app

# add a fixture to the test file
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# Test for Animal Model

# This Animal Model test for response status code 200 means that the request was successful
def test_get_animals(client):
    with app.app_context():
        response = client.get('/animal/')
        assert response.status_code == 200