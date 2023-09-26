from fastapi.testclient import TestClient
from backend.main import app 

client = TestClient(app)

def test_homepage():
    response = client.get("/")
    assert response.status_code == 200

# async def test_get_blog_posts():
#     response = await client.get("/blogs")
#     assert response.status_code == 200
#     assert response.json() == {"item_id": 1, "name": "Example Item"}
