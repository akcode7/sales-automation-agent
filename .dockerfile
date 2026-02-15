FROM python:3.11-slim-bookworm

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy files
COPY pyproject.toml .
RUN pip install .

COPY . .

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Archestra uses stdio for communication by default
ENTRYPOINT ["python", "-m", "src.server"]