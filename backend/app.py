from fastapi import FastAPI
from datetime import datetime
import platform
import requests

app = FastAPI()


@app.get("/")
def home():
    return {
        "project": "SentinelAI",
        "status": "running",
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
        "release": platform.release(),
        "processor": platform.processor()
    }


@app.get("/incident-analysis")
def incident_analysis():

    response = requests.get("http://ai-engine:8001/analyze")

    ai_result = response.json()

    return {
        "source": "AI Engine",
        "analysis": ai_result
    }