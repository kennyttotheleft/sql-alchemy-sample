FROM python:3.10-buster as base
ENV PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1

WORKDIR /app

FROM base as builder
ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VERSION=1.7.1
RUN pip install "poetry==$POETRY_VERSION"

COPY ["./app/pyproject.toml", "./app/poetry.lock", "/app/"]
RUN poetry config virtualenvs.in-project true && \
    poetry config virtualenvs.create false &&\
    poetry install

EXPOSE 8000

CMD ["uvicorn", "backend.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
