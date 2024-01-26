FROM python:3.10.5 as requirements-stage 
WORKDIR /src

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV ENVIRONMENT prod
ENV TESTING 0

RUN pip install poetry

COPY ./pyproject.toml ./poetry.lock* /src/

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes


FROM python:3.10.5


WORKDIR /code


COPY --from=requirements-stage /src/requirements.txt /code/requirements.txt


RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt


COPY ./app /code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0"]