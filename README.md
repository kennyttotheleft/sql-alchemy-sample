# Fast API x SQLAlchemy sample

This repository provides a straightforward example of using FastAPI and SQLAlchemy.

## Prerequisties

- Docker version : 20.10.13, build a224086
- Docker Compose : 2.3.3
- Python : 3.10
- Poetry : 1.7.1
- FastAPI : 0.104.1
- Uvicorn : 0.24.0.post1
- psycopg2 : 2.9.9
- SQLAlchemy : 2.0.23
- SQLModel : 0.0.14

### Dev dependencies

- httpx : 0.25.2
- pytest : 7.4.3
- pytest-asyncio : 0.23.2
- pytest-cov : 4.1.0
- pytest-mock : 3.12.0

## Architecture

### Layers of the system

- Infrastructures: Database client, logging, loading env vars
- Routers: API routing logic, DI setup process
- Models: Table model, Data model
- Services: Domain business logic, Data CRUD process control
- Repositories: Data accessing interface

## Development environment

### First setup

```bash
# build and start the containers
% make build
# install modules
% make install
# create dev database
% make migrate
# create testing database
% make test-migrate
```

### Starting the Server

```bash
% make up
```

### Testing

```bash
# execute Unit test and E2E test cases
% make test
# execute with debug output
% make test-debug
```

### API endpoint

- [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- [http://127.0.0.1:8000/items/1](http://127.0.0.1:8000/items/1)

### API documents

- [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

### Stopping and restarting the Server

```bash
# stop
% make stop
# restart
% make restart
```

### Clean-up containers

```bash
# remove containers
% make down
# remove containers and volumes
% make remove
```

### Command Execution

You can execute commands within the container.

Adding a package:

```bash
docker compose exec app poetry add fastapi
docker compose exec app poetry add -D pytest-asyncio
```
