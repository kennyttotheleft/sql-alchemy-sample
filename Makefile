
build: build-container install

build-container:
	docker compose up -d --build

up:
	docker compose up -d

restart:
	docker compose restart

stop:
	docker compose stop

down:
	docker compose down

remove:
	docker compose down --volumes

install:
	docker compose exec app poetry install --no-interaction
	docker compose exec app-test poetry install --no-interaction

migrate:
	docker compose exec app poetry run python backend/db_migration.py
	docker compose exec app poetry run python backend/db_seed.py

test-migrate:
	docker compose exec app-test poetry run python backend/db_migration.py

logs:
	docker compose logs app --follow

test:
	docker compose exec app-test poetry run pytest

test-debug:
	docker compose exec app-test poetry run pytest --log-cli-level=DEBUG

.PHONY: build, build-container, install, up, restart, stop, down, remove, logs, migrate, test-migrate, test, test-debug, test-ci
