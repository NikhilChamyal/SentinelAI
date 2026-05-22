from fastapi import FastAPI
from log_analyzer import analyze_logs

app = FastAPI()


@app.get("/")
def home():
    return {
        "service": "AI Engine Running"
    }


@app.get("/analyze")
def analyze():

    sample_log = """
    CrashLoopBackOff error detected.
    Memory usage exceeded limit.
    """

    result = analyze_logs(sample_log)

    return result