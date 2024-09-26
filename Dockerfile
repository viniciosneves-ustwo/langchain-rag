FROM python:latest
WORKDIR /app
COPY pyproject.toml poetry.lock ./
RUN pip install poetry
RUN poetry install --no-dev
COPY . .
EXPOSE 8000
CMD ["poetry", "run", "uvicorn", "rag:app", "--host", "0.0.0.0", "--port", "8000"]