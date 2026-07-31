from datetime import datetime
import socket

from fastapi import FastAPI


app = FastAPI(
    title="DevOps Cloud API",
    description="API used to demonstrate cloud-native deployment and monitoring.",
    version="1.0.0",
)


@app.get("/")
def home():
    return {
        "message": "DevOps Cloud Platform is running!",
        "hostname": socket.gethostname(),
        "version": "1.0.0",
        "timestamp": datetime.now(),
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
    }