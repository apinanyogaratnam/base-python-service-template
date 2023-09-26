FROM python:3.10

WORKDIR /app

# copy dependency list
COPY Pipfile Pipfile.lock ./
COPY Makefile /app/Makefile

# install make
RUN apt install make && pip install pipenv==2022.11.30 && pipenv install --system --deploy

# install dependencies
RUN make install

# copy the rest of the files
COPY . .

CMD ["python", "main.py"]
