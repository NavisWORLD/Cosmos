FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    COSMOS_DATA_DIR=/data \
    COSMOS_HOST=0.0.0.0 \
    COSMOS_PORT=8081

WORKDIR /app
COPY pyproject.toml README.md LICENSE ./
COPY cosmos ./cosmos
RUN pip install --no-cache-dir .
RUN useradd --create-home cosmos && mkdir -p /data && chown -R cosmos:cosmos /data /app
USER cosmos
VOLUME ["/data"]
EXPOSE 8081
CMD ["python", "-m", "cosmos", "web", "--host", "0.0.0.0", "--port", "8081"]
