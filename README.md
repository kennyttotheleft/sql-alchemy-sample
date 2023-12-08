# Fast API sample

This repository serves as a simple example of using FastAPI.

## Prerequisties

- Docker version : 20.10.13, build a224086
- Docker Compose : 2.3.3
- Python : 3.10
- Poetry : 1.7.1
- FastAPI : 0.104.1
- Uvicorn : 0.24.0.post1
- Pytest : 7.4.3

## Development environment

### Starting the Server

```bash
docker compose up -d
```

### API endpoint

- [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- [http://127.0.0.1:8000/items/1](http://127.0.0.1:8000/items/1)

### Swagger UI

- [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### Stopping the Server

```bash
docker compose down
```

### Command Execution

You can execute commands within the container.

Adding a package:

```bash
docker compose exec app poetry add fastapi
docker compose exec app poetry add -D pytest-asyncio
```

Test execution:

```bash
docker compose exec app pytest
```
