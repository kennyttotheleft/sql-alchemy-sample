build:
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
	docker compose exec app poetry install
	docker compose exec app-test poetry install

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

.PHONY: build, up, restart, stop, down, remove, install, migrate, logs, test, test-debug, test-migrate
