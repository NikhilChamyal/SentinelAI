# SentinelAI — AI-Powered Cloud-Native DevOps Observability Platform

## Overview

SentinelAI is a production-style cloud-native DevOps observability platform built using Kubernetes, Docker, FastAPI, Prometheus, Grafana, Loki, GitHub Actions, and AI-powered incident analysis.

The platform simulates real-world DevOps and SRE workflows including:
- Kubernetes orchestration
- CI/CD automation
- centralized logging
- monitoring dashboards
- autoscaling infrastructure
- rolling deployments
- intelligent incident analysis

---

# Architecture

```text
Users
   ↓
Ingress Controller
   ↓
Backend Service
   ↓
Backend Pods
   ↓
AI Analysis Service
   ↓
AI Pods

Observability Stack:
Prometheus
Grafana
Loki
Promtail

CI/CD:
GitHub Actions
Docker Hub
Kubernetes

Features
Kubernetes-based microservices architecture
Dockerized backend and AI services
AI-powered incident analysis engine
Prometheus monitoring stack
Grafana dashboards
Loki centralized logging
Promtail log collection
Kubernetes Horizontal Pod Autoscaling (HPA)
Rolling updates with zero downtime
GitHub Actions CI/CD pipeline
Docker Hub integration
Kubernetes Ingress routing
Production-style deployment workflow
Tech Stack
DevOps & Cloud
Kubernetes
Docker
GitHub Actions
Docker Hub
Minikube
Monitoring & Logging
Prometheus
Grafana
Loki
Promtail
Backend
Python
FastAPI
AI & Analysis
AI-based log analysis engine
Incident recommendation system
Kubernetes Features
Deployments
Services
Ingress
Horizontal Pod Autoscaling (HPA)
Rolling Updates
Multi-Pod Architecture
Internal Service Discovery
CI/CD Pipeline

Implemented CI/CD automation using GitHub Actions.

Pipeline workflow:

Source code pushed to GitHub
GitHub Actions triggers automatically
Docker image built automatically
Image pushed to Docker Hub
Kubernetes deployment updated
Monitoring & Observability

Implemented production-style observability stack using:

Prometheus for metrics collection
Grafana for visualization dashboards
Loki for centralized logging
Promtail for log aggregation

Monitored:

Kubernetes pods
CPU usage
memory usage
application logs
cluster activity
AI Incident Analysis

SentinelAI includes an AI-powered incident analysis engine capable of:

detecting pod crashes
identifying memory issues
analyzing timeout failures
generating intelligent recommendations

Example output:

{
  "severity": "critical",
  "issue": "Kubernetes pod crash detected",
  "recommendation": "Check pod logs and container health"
}

How to Run
Clone Repository
git clone https://github.com/NikhilChamyal/SentinelAI.git
cd SentinelAI
Start Minikube
minikube start
Apply Kubernetes Deployments
kubectl apply -f kubernetes/
Verify Pods
kubectl get pods
Access Backend Service
kubectl port-forward service/backend-service 9999:80

Open:

http://localhost:9999
Future Improvements
ArgoCD GitOps deployment
Terraform Infrastructure as Code
AWS EKS deployment
Helm charts
OpenTelemetry tracing
Slack alert integration
AI anomaly prediction
Security scanning integration

Author

Nikhil Chamyal

MCA Student | Cloud Computing | DevOps | Kubernetes | AI Integration