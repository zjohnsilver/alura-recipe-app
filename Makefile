CONTAINER_NAME=alura-recipe-app

local/docker/start/app:
	docker-compose up --build $(CONTAINER_NAME)

local/docker/start/postgres:
	docker-compose up postgresql

local/start/app:
	python manage.py runserver 0.0.0.0:8000