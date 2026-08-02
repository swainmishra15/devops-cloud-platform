from datetime import datetime, timezone
import os
import socket

from fastapi import FastAPI


APP_VERSION = os.getenv("APP_VERSION", "1.0.0")
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")


app = FastAPI(
    title="DevOps Cloud API",
    description="API used to demonstrate cloud-native deployment and monitoring.",
    version=APP_VERSION,
)


@app.get("/")
def home():
    return {
        "message": "DevOps Cloud API v3 - Kubernetes Rolling Update Successful",
        "hostname": socket.gethostname(),
        "version": APP_VERSION,
        "environment": ENVIRONMENT,
        "timestamp": datetime.now(timezone.utc),
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "version": APP_VERSION,
        "environment": ENVIRONMENT,
    }