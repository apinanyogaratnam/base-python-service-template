IMAGE_NAME = base-python-service-template

.PHONY: build

lint:
	flake8 .

format:
	ruff --fix .

start:
	python main.py

install:
	pip install pipenv==2022.11.30
	pipenv install

build:
	docker build -t ${IMAGE_NAME} .

run:
	docker run -p 8001:8001 ${IMAGE_NAME}

up:
	docker-compose up --scale base-python-service-template=5 --remove-orphans -d --build

down:
	docker-compose down

dev:
	docker-compose -f docker-compose-dev.yml up --build