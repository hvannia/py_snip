# Path: testing_falcon/test_falcon_app.py
# test case for the falcon application in testing_falcon/falcon_app.py
# uses pytest with pytest-falcon plugin
#

import pytest
import falcon
import json
from falcon import testing
from falcon_app import app

@pytest.fixture
def client():
    return testing.TestClient(app)

def test_post_empty_body(client):
    response = client.simulate_post('/', body='')
    assert response.status == falcon.HTTP_400
    assert response.json['title'] == 'Empty request body'
    assert response.json['description'] == 'A valid JSON document is required.'

def test_post_valid_json(client):
    response = client.simulate_post('/', body='{"name": "John"}')
    assert response.status == falcon.HTTP_200
    assert response.json['success'] == True


# test with pytest.raises
def test_post_empty_body_with_pytest_raises(client):
    with pytest.raises(falcon.HTTPBadRequest) as e:
        client.simulate_post('/', body='')
    assert e.value.title == 'Empty request body'
    assert e.value.description == 'A valid JSON document is required.'

    