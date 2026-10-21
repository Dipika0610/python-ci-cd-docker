# Python CI/CD Pipeline with Docker & GitHub Actions

## Project Overview
This repository implements an automated, robust **CI/CD (Continuous Integration and Continuous Deployment) pipeline** for a Python web application using **GitHub Actions** and **Docker**.

---

## Architecture & Pipeline Flow
The pipeline is designed with 3 strict sequential stages:

```mermaid
graph LR
    A[Code Push to GitHub] --> B[1. Build Stage]
    B --> C[2. Test Stage]
    C --> D[3. Deploy Stage]
    D --> E[Production Live Container]
```

1. **Build Stage (`build`)**: Sets up Python environment, verifies dependencies from `requirements.txt`, and builds the Docker container image.
2. **Test Stage (`test`)**: Executes automated unit tests using `pytest` and performs a containerized smoke test.
3. **Deploy Stage (`deploy`)**: Packages the validated Docker image, publishes it to GitHub Container Registry (`ghcr.io`), and validates live execution.

---

## Project Structure
```text
ci/
├── .github/
│   └── workflows/
│       └── ci-cd.yml          # GitHub Actions CI/CD Pipeline definition
├── app.py                     # Python Flask Web Application
├── test_app.py                # Automated Pytest Test Suite
├── Dockerfile                 # Container specification
├── .dockerignore              # Ignore unnecessary build context files
├── .gitignore                # Ignore local python virtual environments & cache
├── requirements.txt           # Project dependencies (Flask, Pytest, Requests)
└── README.md                  # Detailed Documentation & Lab Submission Guide
```

---

## Endpoints
- `GET /`: Returns welcome greeting.
- `GET /health`: Returns JSON health status (`{"status": "healthy"}`).

---

## Local Development (Windows)

### 1. Run Python App Locally
```powershell
python -m pip install -r requirements.txt
python app.py
```
Open your browser at `http://localhost:5000/`.

### 2. Run Tests Locally
```powershell
pytest test_app.py -v
```

### 3. Build & Run Docker Container Locally
```powershell
docker build -t python-ci-cd-app:latest .
docker run -p 5000:5000 python-ci-cd-app:latest
```
Visit `http://localhost:5000/` or `http://localhost:5000/health`.
