def analyze_logs(log_text):
    
    log_text = log_text.lower()

    if "crashloopbackoff" in log_text:
        return {
            "severity": "critical",
            "issue": "Kubernetes pod crash detected",
            "recommendation": "Check pod logs and container health"
        }

    elif "memory" in log_text:
        return {
            "severity": "high",
            "issue": "High memory usage detected",
            "recommendation": "Increase memory limits or optimize application"
        }

    elif "timeout" in log_text:
        return {
            "severity": "medium",
            "issue": "Service timeout detected",
            "recommendation": "Check service connectivity and latency"
        }

    elif "error" in log_text:
        return {
            "severity": "medium",
            "issue": "Application error detected",
            "recommendation": "Review logs for detailed exception traces"
        }

    else:
        return {
            "severity": "low",
            "issue": "No major issue detected",
            "recommendation": "System operating normally"
        }