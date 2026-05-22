from fastapi import FastAPI
from datetime import datetime
import platform
import requests

from prometheus_client import Counter, generate_latest
from fastapi.responses import Response

app = FastAPI()

REQUEST_COUNT = Counter(
    "app_requests_total",
    "Total App HTTP Requests"
)


@app.get("/")
def home():

    REQUEST_COUNT.inc()

    return {
        "project": "SentinelAI",
        "status": "running",
        "time": str(datetime.now())
    }


@app.get("/health")
def health_check():

    REQUEST_COUNT.inc()

    return {
        "status": "healthy"
    }


@app.get("/system")
def system_info():

    REQUEST_COUNT.inc()

    return {
        "system": platform.system(),
        "release": platform.release(),
        "processor": platform.processor()
    }


@app.get("/incident-analysis")
def incident_analysis():

    REQUEST_COUNT.inc()

    response = requests.get("http://ai-service:8001/analyze")

    ai_result = response.json()

    return {
        "source": "AI Engine",
        "analysis": ai_result
    }


@app.get("/metrics")
def metrics():

    return Response(
        generate_latest(),
        media_type="text/plain"
    )