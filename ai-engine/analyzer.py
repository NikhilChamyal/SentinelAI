from fastapi import FastAPI
from datetime import datetime

app = FastAPI()


@app.get("/")
def home():
    return {
        "service": "AI Engine",
        "status": "running",
        "time": str(datetime.now())
    }


@app.get("/analyze")
def analyze_logs():
    return {
        "incident": "CrashLoopBackOff detected",
        "possible_cause": "Container memory limit exceeded",
        "recommendation": "Increase memory limits or optimize application"
    }