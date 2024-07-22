FROM python:3.12-slim AS requirements-stage

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /tmp

RUN pip install poetry

COPY pyproject.toml poetry.lock* ./

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM python:3.12-slim AS runtime

FROM python:3.12-slim AS runtime

WORKDIR /code

COPY --from=requirements-stage /tmp/requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
