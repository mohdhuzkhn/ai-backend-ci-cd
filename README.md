# 🚀 AI Backend CI/CD Pipeline (Capstone)

A production-grade, automated CI/CD pipeline for a FastAPI AI backend service. Built with modern Python tooling, containerized environments, and GitHub Actions orchestration.

## 🏗️ Pipeline Architecture

```text
[ Git Push / PR ]
        │
        ▼
┌─────────────────────────────┐
│  Static Analysis & Types    │
│  (Black, Ruff, mypy)        │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│  Parallel Matrix Testing    │
│  (Python 3.11, 3.12)        │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│  Integration Testing        │
│  (PostgreSQL + Redis)       │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│  Container Build & Scan     │
│  (Docker Build Verification)│
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│  Automated Deployment       │
│  (Production Release)       │
└─────────────────────────────┘



🛠️ Tech Stack
Framework: FastAPI / Uvicorn

Database & Cache: PostgreSQL, Redis

Quality & Linting: Black, Ruff, Mypy

Testing: Pytest, Pytest-Cov

Containerization: Docker

CI/CD Orchestration: GitHub Actions



💻 Local Development Setup


1. Clone & Setup Virtual Environment
Bash
git clone [https://github.com/](https://github.com/)<your-username>/ai-backend-ci-cd.git
cd ai-backend-ci-cd

python -m venv venv
# On Windows:
venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate


2. Install Dependencies
Bash
pip install -r requirements.txt


3. Run Quality Checks Locally
Bash
# Code formatting check
black --check .

# Fast linting
ruff check .

# Static type checking
mypy app/


4. Run Unit Tests
Bash
pytest --cov=app tests/


5. Run API Server
Bash
uvicorn app.main:app --reload
Access the API docs at http://127.0.0.1:8000/docs.

🐳 Docker Setup
Build and run the application container locally:

Bash
docker build -t ai-backend-app .
docker run -p 8000:8000 ai-backend-app