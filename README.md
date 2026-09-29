# 📝 Blogging Platform API

A small but production-ready RESTful API for a personal blogging platform. Built with **FastAPI**, **async SQLAlchemy**, and **SQLite**.

## ✨ Features

- Create, read, update, and delete blog posts
- Search posts by title, content, or category
- Strict input validation with `400 Bad Request` responses
- Fully async data layer (SQLite via `aiosqlite`)
- Layered architecture: router → service → repository
- 12 automated tests with pytest

## 🛠 Tech Stack

- **Framework:** [FastAPI](https://fastapi.tiangolo.com/)
- **Language:** Python 3.13+
- **Package Manager:** [uv](https://docs.astral.sh/uv/)
- **Database:** SQLite + async SQLAlchemy (`aiosqlite`)
- **Testing:** pytest + pytest-asyncio + httpx

## 📁 Project Structure

```text
.
├── app/
│   ├── api/
│   │   ├── deps.py              # Dependency injection chain
│   │   └── routes/
│   │       └── posts.py         # HTTP routes for posts
│   ├── core/
│   │   ├── config.py            # Application settings
│   │   └── database.py          # Async engine & session factory
│   ├── models/
│   │   ├── __init__.py          # Public model exports
│   │   ├── post.py              # SQLAlchemy ORM model
│   │   ├── post_create.py       # Pydantic request schema
│   │   └── post_response.py     # Pydantic response schema
│   ├── repositories/
│   │   └── post_repository.py   # Async data access layer
│   ├── services/
│   │   └── post_service.py      # Business logic layer
│   └── main.py                  # FastAPI entry point
├── tests/
│   ├── conftest.py              # Test fixtures & DB override
│   └── test_posts.py            # API test suite
├── pyproject.toml
└── README.md
```

## 🚀 Getting Started

### Prerequisites

- Python 3.13 or newer
- [uv](https://docs.astral.sh/uv/getting-started/installation/) installed

### Install Dependencies

```bash
uv sync
```

### Run the Server

```bash
uv run uvicorn app.main:app --host 0.0.0.0 --port 8000
```

For development with auto-reload:

```bash
uv run uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

The API will be available at [http://localhost:8000](http://localhost:8000).

### Run Tests

```bash
uv run pytest
```

### Run Tests with Coverage

```bash
uv run pytest --cov=app --cov-report=term-missing
```

## API Endpoints

| Method | Endpoint      | Description                          |
|--------|---------------|--------------------------------------|
| POST   | `/posts`      | Create a new blog post               |
| GET    | `/posts`      | Get all blog posts                   |
| GET    | `/posts?term=tech` | Search posts by term          |
| GET    | `/posts/{id}` | Get a single blog post               |
| PUT    | `/posts/{id}` | Update an existing blog post         |
| DELETE | `/posts/{id}` | Delete an existing blog post         |

### Create a Post

```bash
curl -X POST http://localhost:8000/posts \
  -H "Content-Type: application/json" \
  -d '{
    "title": "My First Blog Post",
    "content": "This is the content of my first blog post.",
    "category": "Technology",
    "tags": ["Tech", "Programming"]
  }'
```

**Response:** `201 Created`

```json
{
  "id": 1,
  "title": "My First Blog Post",
  "content": "This is the content of my first blog post.",
  "category": "Technology",
  "tags": ["Tech", "Programming"],
  "createdAt": "2021-09-01T12:00:00Z",
  "updatedAt": "2021-09-01T12:00:00Z"
}
```

### Update a Post

```bash
curl -X PUT http://localhost:8000/posts/1 \
  -H "Content-Type: application/json" \
  -d '{
    "title": "My Updated Blog Post",
    "content": "This is the updated content.",
    "category": "Technology",
    "tags": ["Tech", "Programming"]
  }'
```

**Response:** `200 OK`

### Delete a Post

```bash
curl -X DELETE http://localhost:8000/posts/1
```

**Response:** `204 No Content`

## Status Codes

- `201 Created` — resource created successfully
- `200 OK` — request succeeded
- `204 No Content` — resource deleted successfully
- `400 Bad Request` — validation error
- `404 Not Found` — resource not found

## License

This project is for educational purposes.
