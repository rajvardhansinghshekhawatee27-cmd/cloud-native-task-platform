# ☁️ Cloud-Native Task Management Platform

A production-style **cloud-native DevOps project** built from scratch to demonstrate an end-to-end software delivery and observability workflow.

The project combines a **FastAPI REST API**, **PostgreSQL**, **Docker**, **Kubernetes**, **Terraform**, **AWS**, **GitHub Actions**, **Prometheus**, and **Grafana** into a complete DevOps platform.

---

## 📌 Overview

The application is a simple Task Management REST API.

The main purpose of this project is not the complexity of the application itself, but the **DevOps ecosystem built around it**.

It demonstrates how application code can move through:

**Source Code → Automated Testing → Containerization → Security Scanning → Container Registry → Kubernetes → Monitoring**

---

## 🏗️ Architecture

```text
                         ┌──────────────────────┐
                         │      Developer       │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │       GitHub         │
                         │   Source Repository  │
                         └──────────┬───────────┘
                                    │
                                    ▼
                    ┌──────────────────────────────┐
                    │       GitHub Actions         │
                    │                              │
                    │  • Run tests                 │
                    │  • Build Docker image        │
                    │  • Health check              │
                    │  • Trivy security scan       │
                    │  • AWS OIDC authentication   │
                    │  • Push image to ECR         │
                    └──────────────┬───────────────┘
                                   │
                                   ▼
                         ┌──────────────────────┐
                         │     Amazon ECR       │
                         │   Container Registry │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │      Kubernetes      │
                         │                      │
                         │  ┌────────────────┐  │
                         │  │ FastAPI Pods   │  │
                         │  │   2 replicas   │  │
                         │  └───────┬────────┘  │
                         │          │            │
                         │  ┌───────▼────────┐  │
                         │  │   PostgreSQL    │  │
                         │  └────────────────┘  │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │      Prometheus      │
                         │    Metrics Scraping  │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │       Grafana        │
                         │    Visualization     │
                         └──────────────────────┘
🎯 Project Goals
Build a REST API using FastAPI
Connect the application to PostgreSQL
Implement database models using SQLAlchemy
Manage schema changes using Alembic
Write automated tests using Pytest
Containerize the application using Docker
Run the container as a non-root user
Scan Docker images using Trivy
Build a CI/CD pipeline using GitHub Actions
Publish container images to Amazon ECR
Authenticate GitHub Actions with AWS using OIDC
Provision AWS infrastructure using Terraform
Deploy the application using Kubernetes
Implement Kubernetes health checks
Configure resource requests and limits
Implement Prometheus monitoring
Visualize metrics using Grafana
🛠️ Technology Stack
Application
Python 3.13
FastAPI
SQLAlchemy
PostgreSQL
Alembic
Pytest
Containerization & Security
Docker
Docker Desktop
Local Docker Registry
Trivy
Non-root container execution
Kubernetes
Kubernetes
Docker Desktop Kubernetes
Deployments
Services
Secrets
Readiness Probes
Liveness Probes
Resource Requests & Limits
Database Migration Jobs
ServiceMonitor
CI/CD
GitHub Actions
Automated Testing
Docker Image Builds
Trivy Security Scanning
Amazon ECR
GitHub OIDC
Infrastructure as Code
Terraform
Amazon VPC
Subnets
Route Tables
Internet Gateway
Amazon EKS
IAM
Monitoring
Prometheus
Grafana
ServiceMonitor
Kubernetes Metrics
📁 Project Structure
cloud-native-task-platform/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── app/
│   ├── src/
│   │   ├── main.py
│   │   ├── database.py
│   │   └── models.py
│   │
│   ├── tests/
│   ├── migrations/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── alembic.ini
│
├── kubernetes/
│   └── app.yaml
│
├── scripts/
│
├── terraform/
│   ├── providers.tf
│   ├── variables.tf
│   ├── ecr.tf
│   ├── vpc.tf
│   ├── subnets.tf
│   ├── network.tf
│   ├── eks.tf
│   ├── node-group.tf
│   └── eks-iam.tf
│
├── .gitignore
└── README.md
🔌 REST API

The application provides a simple Task Management REST API.

Health Check
GET /health

Response:

{
  "status": "healthy"
}
Create Task
POST /tasks

Example:

{
  "title": "Learn Kubernetes",
  "completed": false
}
Get All Tasks
GET /tasks
Get Task
GET /tasks/{task_id}
Update Task
PUT /tasks/{task_id}
Delete Task
DELETE /tasks/{task_id}
Application Metrics
GET /metrics

The /metrics endpoint exposes Prometheus-compatible application metrics.

🐳 Docker

The application is packaged as a Docker image using a lightweight Python base image.

The container is configured to run as a dedicated non-root user.

Build
docker build -t task-platform .
Run
docker run -p 8000:8000 task-platform

Application:

http://localhost:8000

API documentation:

http://localhost:8000/docs
🔐 Container Security

Security is integrated into the container build and CI pipeline.

Implemented security practices include:

Non-root Docker user
Lightweight base image
Package updates during image build
Trivy vulnerability scanning
Critical vulnerability checks in CI
GitHub OIDC authentication
IAM-based AWS access
Kubernetes Secrets
Docker health verification
Kubernetes readiness and liveness probes

Example:

trivy image --severity CRITICAL --ignore-unfixed task-platform:latest
☸️ Kubernetes

The application is deployed to Kubernetes with 2 replicas.

The Kubernetes configuration includes:

Deployment
Service
PostgreSQL
Kubernetes Secret
Database migration Job
Readiness Probe
Liveness Probe
CPU and memory resource limits
Prometheus ServiceMonitor
Deploy
kubectl apply -f kubernetes/app.yaml
Check Pods
kubectl get pods -n task-platform
Check Services
kubectl get svc -n task-platform
Check Deployment
kubectl rollout status deployment/task-platform -n task-platform
🗄️ Database

PostgreSQL is used as the application's relational database.

The application uses:

SQLAlchemy for database access
PostgreSQL for persistent data
Alembic for schema migrations

Database migrations are executed through Kubernetes as a migration Job.

🔄 CI/CD Pipeline

GitHub Actions automates the application's validation and container delivery workflow.

                    Git Push
                       │
                       ▼
              Install Dependencies
                       │
                       ▼
                  Run Pytest
                       │
                       ▼
              Build Docker Image
                       │
                       ▼
                Health Check
                       │
                       ▼
             Trivy Security Scan
                       │
                       ▼
            GitHub OIDC → AWS IAM
                       │
                       ▼
                 Login to ECR
                       │
                       ▼
              Push Image to ECR

The pipeline ensures that code is tested and security-scanned before the container image is published.

🔑 GitHub OIDC + AWS

The CI pipeline uses GitHub OIDC to authenticate with AWS.

Instead of storing long-lived AWS access keys in GitHub, the workflow assumes an AWS IAM role using temporary credentials.

This provides a more secure approach for GitHub Actions → AWS authentication.

🏗️ Infrastructure as Code

AWS infrastructure is defined using Terraform.

The Terraform configuration includes:

Amazon VPC
Public subnets
Private subnets
Route tables
Internet Gateway
Amazon EKS
EKS Node Group
IAM roles and policies
Amazon ECR
Initialize Terraform
terraform init
Validate
terraform validate
Create Plan
terraform plan
Apply
terraform apply

When AWS infrastructure is only required for testing or demonstration, destroy it afterward:

terraform destroy

This helps avoid unnecessary AWS costs.

📊 Monitoring & Observability

The application exposes a Prometheus-compatible /metrics endpoint.

Prometheus discovers the Kubernetes application through a ServiceMonitor.

FastAPI
   │
   │ /metrics
   ▼
Kubernetes Service
   │
   ▼
ServiceMonitor
   │
   ▼
Prometheus
   │
   ▼
Grafana
Example PromQL Query
up{namespace="task-platform"}

A value of:

1

indicates that Prometheus is successfully scraping the application.

Grafana is used to visualize application and Kubernetes metrics.

🧪 Testing

Automated tests are implemented using Pytest.

Run the test suite locally:

cd app
pytest

Tests are also executed automatically through GitHub Actions.

💻 Local Development
1. Clone the Repository
git clone https://github.com/rajvardhansinghshekhawatee27-cmd/cloud-native-task-platform.git
cd cloud-native-task-platform
2. Create Python Virtual Environment
cd app
python -m venv venv

Windows PowerShell:

.\venv\Scripts\Activate.ps1
3. Install Dependencies
pip install -r requirements.txt
4. Run the Application
uvicorn src.main:app --reload

Application:

http://localhost:8000

Swagger documentation:

http://localhost:8000/docs
📚 DevOps Concepts Demonstrated

This project demonstrates hands-on experience with:

Linux
Git
GitHub
Python
REST APIs
FastAPI
PostgreSQL
SQLAlchemy
Alembic
Docker
Container Security
Trivy
Kubernetes
Kubernetes Networking
Kubernetes Secrets
Kubernetes Health Probes
Kubernetes Resource Management
Kubernetes Jobs
Terraform
AWS VPC
AWS EKS
AWS ECR
AWS IAM
GitHub Actions
GitHub OIDC
CI/CD
Prometheus
Grafana
Observability
Infrastructure as Code
Cloud-Native Architecture
⭐ Project Highlights
End-to-End CI/CD

Automated testing, Docker image building, security scanning, and Amazon ECR publishing.

Infrastructure as Code

AWS infrastructure is defined using Terraform instead of relying entirely on manual configuration.

Container Security

The application container runs as a non-root user and is scanned using Trivy.

Kubernetes

The application runs with multiple replicas, health checks, resource controls, services, secrets, and database migrations.

Observability

Prometheus automatically discovers and scrapes the application, while Grafana provides visualization.

Secure AWS Authentication

GitHub Actions uses OIDC and IAM roles instead of long-lived AWS access keys.

📈 Future Improvements

Possible future extensions include:

Amazon RDS PostgreSQL
Application Load Balancer
HTTPS/TLS
Amazon S3 integration
AWS CloudWatch integration
Kubernetes Horizontal Pod Autoscaler
Ingress Controller
External Secrets
Advanced application-level metrics
Automated Kubernetes deployment from CI/CD
Blue/Green deployments
Canary deployments
👨‍💻 Author

Rajvardhan Singh Shekhawat
