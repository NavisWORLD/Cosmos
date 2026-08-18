"""Compatibility launcher for the COSMOS local JSON API."""
from cosmos.config import CosmosConfig
from cosmos.web import serve

if __name__ == "__main__":
    serve(CosmosConfig.from_env())
