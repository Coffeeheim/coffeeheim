FROM python:3.12-slim as builder

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /tmp

RUN pip install poetry

COPY pyproject.toml poetry.lock ./
RUN --mount=type=cache,target=$POETRY_CACHE_DIR poetry install --without dev --no-root

FROM python:3.12-slim as runtime

COPY --from=builder /tmp/.venv /code/.venv

WORKDIR /code

ENV PATH="/code/.venv/bin:$PATH"

#CMD ["python", "-u", "mqtt_sub.py"]
CMD ["tail", "-f", "/dev/null"]