import pytest
from app import app

# add a fixture to the test file
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

