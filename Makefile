lint:
	flake8 .

format:
	black .
	isort .

start:
	python main.py
