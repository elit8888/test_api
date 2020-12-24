all: build run

build:
	docker-compose build

run:
	docker-compose up

test:
	docker-compose run api_server pytest -v /code/tests

test_local:
	docker exec -t apitest sh -c 'pytest -v /code/tests'

clean:
	docker-compose down -v
