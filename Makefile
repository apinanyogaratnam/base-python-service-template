shell:
	pipenv shell

format:
	black .
	isort .

start:
	python main.py
