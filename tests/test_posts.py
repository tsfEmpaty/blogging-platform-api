import pytest
from fastapi.testclient import TestClient


@pytest.fixture
def sample_post():
    return {
        "title": "My First Blog Post",
        "content": "This is the content of my first blog post.",
        "category": "Technology",
        "tags": ["Tech", "Programming"],
    }


class TestCreatePost:
    def test_create_post_returns_201(self, client: TestClient, sample_post):
        response = client.post("/posts", json=sample_post)
        assert response.status_code == 201
        data = response.json()
        assert data["title"] == sample_post["title"]
        assert data["content"] == sample_post["content"]
        assert data["category"] == sample_post["category"]
        assert data["tags"] == sample_post["tags"]
        assert "id" in data
        assert "createdAt" in data
        assert "updatedAt" in data

    def test_create_post_with_invalid_body_returns_400(self, client: TestClient):
        response = client.post("/posts", json={"title": ""})
        assert response.status_code == 400


class TestGetPosts:
    def test_get_all_posts_returns_200(self, client: TestClient, sample_post):
        client.post("/posts", json=sample_post)
        response = client.get("/posts")
        assert response.status_code == 200
        assert isinstance(response.json(), list)
        assert len(response.json()) == 1

    def test_search_posts_by_term_returns_matching_posts(
        self, client: TestClient, sample_post
    ):
        client.post("/posts", json=sample_post)
        response = client.get("/posts?term=tech")
        assert response.status_code == 200
        data = response.json()
        assert len(data) == 1
        assert "tech" in data[0]["title"].lower()

    def test_search_posts_by_term_returns_empty_list_when_no_match(
        self, client: TestClient, sample_post
    ):
        client.post("/posts", json=sample_post)
        response = client.get("/posts?term=nonexistent")
        assert response.status_code == 200
        assert response.json() == []


class TestGetPost:
    def test_get_post_by_id_returns_200(self, client: TestClient, sample_post):
        created = client.post("/posts", json=sample_post).json()
        response = client.get(f"/posts/{created['id']}")
        assert response.status_code == 200
        assert response.json()["id"] == created["id"]

    def test_get_nonexistent_post_returns_404(self, client: TestClient):
        response = client.get("/posts/9999")
        assert response.status_code == 404


class TestUpdatePost:
    def test_update_post_returns_200(self, client: TestClient, sample_post):
        created = client.post("/posts", json=sample_post).json()
        updated_body = {
            "title": "My Updated Blog Post",
            "content": "This is the updated content of my first blog post.",
            "category": "Technology",
            "tags": ["Tech", "Programming"],
        }
        response = client.put(f"/posts/{created['id']}", json=updated_body)
        assert response.status_code == 200
        data = response.json()
        assert data["title"] == updated_body["title"]
        assert data["content"] == updated_body["content"]
        assert data["id"] == created["id"]
        assert data["createdAt"] == created["createdAt"]
        assert "updatedAt" in data

    def test_update_nonexistent_post_returns_404(self, client: TestClient, sample_post):
        response = client.put("/posts/9999", json=sample_post)
        assert response.status_code == 404

    def test_update_post_with_invalid_body_returns_400(self, client: TestClient):
        response = client.put("/posts/1", json={"title": ""})
        assert response.status_code == 400


class TestDeletePost:
    def test_delete_post_returns_204(self, client: TestClient, sample_post):
        created = client.post("/posts", json=sample_post).json()
        response = client.delete(f"/posts/{created['id']}")
        assert response.status_code == 204
        assert client.get(f"/posts/{created['id']}").status_code == 404

    def test_delete_nonexistent_post_returns_404(self, client: TestClient):
        response = client.delete("/posts/9999")
        assert response.status_code == 404
