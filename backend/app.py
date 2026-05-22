from fastapi import FastAPI
from datetime import datetime
import platform

app = FastAPI()


@app.get("/")
def home():
    return {
        "project": "SentinelAI",
        "status": "running",
        "message": "AI Incident Management Platform",
        "time": str(datetime.now())
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.get("/system")
def system_info():
    return {
        "system": platform.system(),
        "node": platform.node(),
        "release": platform.release(),
        "processor": platform.processor()
    }