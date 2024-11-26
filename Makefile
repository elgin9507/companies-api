IMAGE_NAME=company
DOCS_SOURCE=docs/source

build:
	docker build -t $(IMAGE_NAME) .

up:
	docker-compose up -d

buildup: build up

down:
	docker-compose down

logs:
	docker-compose logs -f

shell: up
	docker-compose exec company /bin/bash

makemigrations: up
	docker-compose exec company alembic revision --autogenerate -m "$(filter-out $@,$(MAKECMDGOALS))"

migrate: up
	docker-compose exec company alembic upgrade head

loaddata: up migrate
	docker-compose exec company python scripts/loaddata.py

builddocs: $(DOCS_SOURCE)
	docker-compose exec company sphinx-build docs/source/ docs/build/

docs: builddocs
	docker-compose up -d docs

wait_for_postgres:
	@echo "Waiting for PostgreSQL to initialize..."
	@sleep 3

dev: build up wait_for_postgres migrate loaddata builddocs
	@echo "Development environment is ready"
