from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()
client = TestClient(app)

response_msg = {'status': 'successful!'}


@app.get('/')
async def get_response():
    return response_msg


def test_get_response():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == response_msg
