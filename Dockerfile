FROM python:3.11-slim
RUN pip install "poetry==1.8.2"
COPY pyproject.toml poetry.lock .
RUN poetry config virtualenvs.create false \
  && poetry install --without dev --no-interaction --no-root
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]