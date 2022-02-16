CONTAINER_NAME=alura-recipe-app

local/docker/start/api:
	docker-compose up --build $(CONTAINER_NAME)

local/docker/start/postgres:
	docker-compose up postgresql