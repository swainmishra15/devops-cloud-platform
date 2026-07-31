# Cloud-Native CI/CD & Observability Platform

A DevOps project demonstrating automated testing, containerization, deployment, orchestration, and monitoring of a FastAPI application using Docker, GitHub Actions, AWS, Kubernetes, Prometheus, and Grafana.

## Architecture

```text
Developer
    │
    │ git push
    ▼
GitHub
    │
    ▼
GitHub Actions
    │
    ├── Test Application
    ├── Build Docker Image
    └── Push Image
            │
            ▼
       Docker Registry
            │
            ▼
          AWS
            │
            ▼
       Kubernetes
       ┌────┴────┐
       │         │
    App Pods   Service
       │
       ▼
   Prometheus
       │
       ▼
     Grafana
```

## Tech Stack

**DevOps:** Docker, Kubernetes, GitHub Actions, Git  
**Cloud:** AWS  
**Monitoring:** Prometheus, Grafana  
**Application:** Python, FastAPI, Pytest  
**Automation:** Bash

## Features

- Containerized FastAPI application using Docker
- Automated testing with Pytest
- CI/CD pipeline using GitHub Actions
- Versioned Docker image publishing
- AWS-based deployment
- Kubernetes deployments and services
- Multiple replicas with self-healing
- Liveness and readiness probes
- Rolling application updates
- Runtime configuration using environment variables
- Non-root container execution
- Prometheus metrics collection
- Grafana monitoring dashboards

## CI/CD Flow

```text
Code Push → GitHub Actions → Test → Docker Build
→ Registry → AWS → Kubernetes Deployment
```

## Run with Docker

```bash
docker build -t devops-cloud-api .
docker run -d -p 8000:8000 --name devops-api devops-cloud-api
```

Application:

`http://localhost:8000`

API documentation:

`http://localhost:8000/docs`

Health check:

`http://localhost:8000/health`

## Project Structure

```text
├── .github/workflows/    # CI/CD
├── app/                  # FastAPI application
├── tests/                # Automated tests
├── kubernetes/           # Kubernetes manifests
├── monitoring/           # Prometheus configuration
├── scripts/              # Automation scripts
├── Dockerfile
└── README.md
```

## Status

CI and Docker containerization are implemented. Cloud deployment, Kubernetes orchestration, and observability components are being added as the project progresses.

## Author

**Swain Mishra**