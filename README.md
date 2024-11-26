# Company Service

This repository contains Company API service.

## Prerequisites

- Docker
- Docker Compose

## Quickstart

Run service and load test data:

```bash
make dev
```

API is now hosted at: http://localhost:8080/

View API docs at: http://localhost:8000/

## Usage

### Build the Docker Image

```bash
make build
```

This command builds the Docker image for the web service.

### Start the Service

```bash
make up
```

This command starts the Docker service in detached mode.

### Build and Start the Service

```bash
make buildup
```

This command combines the build and up commands to build the Docker image and start the service.

### Stop the Service

```bash
make down
```

This command stops all Docker containers.

### View Logs

```bash
make logs
```

This command displays the logs of the Docker containers.

### Open Shell

```bash
make shell
```

This command opens a shell inside the Docker container.

### Create Database Migrations

```bash
make makemigrations <message>
```

This command creates database migration with the provided message.

### Run Database Migrations

```bash
make migrate
```

This command runs database migrations.

### Load Data

```bash
make loaddata
```

This command loads data into the database.

### Build Documentation

```bash
make builddocs
```

This command builds the documentation.

### Serve Documentation

```bash
make docs
```

This command builds ans serves the documentation at localhost:8000/

## Directory Structure

- `src`: Contains the API source files.
- `docs/source`: Contains the documentation source files.
- `scripts`: Contains scripts for managing data.
- `docker-compose.yml`: Docker Compose configuration file.
- `Makefile`: Makefile for managing Docker commands and database migrations.
