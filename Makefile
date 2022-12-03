IMAGE_NAME = base-python-service-template

.PHONY: build

lint:
	flake8 .

format:
	black .
	isort .

start:
	python main.py

install:
	pip install pipenv==2022.11.30
	pipenv install

build:
	docker build -t ${IMAGE_NAME} .
