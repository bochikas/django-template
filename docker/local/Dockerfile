FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 POETRY_VERSION=1.8.4

RUN apt-get update && apt-get install -y postgresql-client && rm -rf /var/lib/apt/lists/*

ARG user=nobody
ARG group=nogroup

WORKDIR /usr/src/app

RUN python -m pip install --upgrade pip poetry

COPY poetry.lock pyproject.toml ./

RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

COPY --chown=${user}:${group} ./app .

USER ${user}

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

COPY --chown=${user}:${group} ./docker/dev/entrypoint.sh .

ENTRYPOINT ["sh", "entrypoint.sh"]
