all: build run

build:
	docker-compose build

run:
	docker-compose up

test:
	docker exec -t apitest sh -c 'pytest -v /code/tests'

clean:
	docker-compose down -v
