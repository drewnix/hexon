FROM python:3.12.1-slim as base

ENV PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1

WORKDIR /app

FROM base as builder

ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VERSION=1.6.1 \
    POETRY_HOME=/opt/poetry

# Install poetry in its own environment
RUN python -m venv $POETRY_HOME
ENV PATH="/opt/poetry/bin:$PATH"
RUN pip install poetry==$POETRY_VERSION

RUN python -m venv /venv
ENV PATH="/venv/bin:$PATH"

COPY pyproject.toml poetry.lock /app/
RUN poetry install --no-dev --no-root

COPY . /app
RUN poetry build

FROM base as final

COPY --from=builder /venv /venv
COPY --from=builder /app/dist .

ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PATH="/venv/bin:$PATH"

RUN pip install *.whl

# Non-root user
RUN useradd --create-home appuser
USER appuser

ENTRYPOINT ["uvicorn", "hexon.main:hexon", "--host=0.0.0.0", "--port=8000"]