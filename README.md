# DevOps Cloud Platform

FastAPI application deployed on AWS EC2 using Docker,
Kubernetes (K3s), GitHub Actions CI/CD and Prometheus monitoring.

## Tech Stack
- Python / FastAPI
- Docker
- GitHub Actions
- Docker Hub
- AWS EC2
- Kubernetes / K3s
- Prometheus
- Git / GitHub

## Architecture

Developer
   ↓
GitHub
   ↓
GitHub Actions
   ↓
Tests → Docker Build → Docker Hub
                         ↓
                      AWS EC2
                         ↓
                        K3s
                         ↓
                  Kubernetes Service
                         ↓
                    FastAPI Pod
                         ↓
                     /metrics
                         ↓
                    Prometheus

## Features
- Containerized FastAPI REST API
- Automated testing with Pytest
- CI/CD pipeline using GitHub Actions
- Docker image build and publishing
- AWS EC2 cloud deployment
- Kubernetes Deployment and NodePort Service
- ConfigMap-based application configuration
- Readiness and liveness probes
- Kubernetes rolling updates and rollback testing
- Horizontal replica scaling demonstration
- Prometheus application instrumentation
- HTTP request counter and latency metrics
- Prometheus monitoring inside Kubernetes

## API Endpoints
GET /         - Application information
GET /health   - Application health
GET /metrics  - Prometheus metrics

## Monitoring
Prometheus scrapes the FastAPI /metrics endpoint.

Custom metrics include:

http_requests_total
http_request_duration_seconds

Prometheus target health was verified using:

up = 1

## Deployment

The application runs on a lightweight K3s cluster hosted
on AWS EC2.

The production deployment uses one application replica
because the demo EC2 instance has limited resources.

Kubernetes supports scaling the deployment when additional
resources are available.