# Loan Approval Prediction API

A production-style machine learning API for predicting loan approval / repayment risk using FastAPI, Docker, and Google Cloud Run.

## Live API

API Base URL:

```text
https://loan-app-1026558337999.asia-south1.run.app
```

Swagger Documentation:

```text
https://loan-app-1026558337999.asia-south1.run.app/docs
```

---

# Project Overview

This project demonstrates an end-to-end machine learning deployment pipeline for a credit risk / loan approval prediction system.

The application:
- accepts applicant financial information,
- preprocesses incoming data,
- loads trained ML artefacts,
- performs inference,
- returns prediction probabilities and approval decisions through a REST API.

The system is containerized using Docker and deployed serverlessly on Google Cloud Run.

---

# Tech Stack

## Machine Learning
- Python
- Scikit-learn
- Pandas
- NumPy

## API & Backend
- FastAPI
- Uvicorn
- Pydantic

## Deployment & Infrastructure
- Docker
- Google Cloud Run
- Google Container Registry (GCR)

---

# Features

- REST API for loan approval prediction
- FastAPI Swagger UI documentation
- Dockerized deployment
- Cloud-native deployment on GCP
- Production-style inference serving
- Input validation using Pydantic
- Portable container architecture

---

# Project Structure

```text
loan_repayment_credit_score_detection/
│
├── app/
│   ├── main.py
│   ├── predictor.py
│   ├── schemas.py
│   └── ...
│
├── artefacts/
│   ├── model.pkl
│   ├── encoder.pkl
│   └── ...
│
├── Dockerfile
├── requirements_docker.txt
├── .dockerignore
├── .gitignore
└── README.md
```

---

# API Endpoint

## Prediction Endpoint

```http
POST /predict
```

### Example Request

```json
{
  "income": 50000,
  "loan_amount": 200000,
  "credit_score": 720,
  "employment_years": 5
}
```

### Example Response

```json
{
  "prediction": "Approved",
  "probability": 0.87
}
```

---

# Local Development

## Clone Repository

```bash
git clone <your-repo-url>
cd loan_repayment_credit_score_detection
```

---

## Create Virtual Environment

```bash
python -m venv .venv
```

Activate environment:

### Windows

```bash
.venv\Scripts\activate
```

### Linux / Mac

```bash
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements_docker.txt
```

---

# Run Locally

```bash
uvicorn app.main:app --reload
```

Open:

```text
http://localhost:8000/docs
```

---

# Docker Setup

## Build Docker Image

```bash
docker build -t loan_approval_prediction .
```

---

## Run Docker Container

```bash
docker run -e PORT=8080 -p 8080:8080 loan_approval_prediction
```

Open:

```text
http://localhost:8080/docs
```

---

# Google Cloud Deployment

## Container Registry Push

```bash
docker tag loan_approval_prediction gcr.io/<PROJECT_ID>/loan-app

docker push gcr.io/<PROJECT_ID>/loan-app
```

---

## Deploy to Cloud Run

```bash
gcloud run deploy loan-app \
--image gcr.io/<PROJECT_ID>/loan-app \
--platform managed \
--region asia-south1 \
--allow-unauthenticated
```

---

# Deployment Architecture

```text
User Request
      ↓
Cloud Run
      ↓
FastAPI Application
      ↓
ML Model Inference
      ↓
Prediction Response
```

---

# Future Improvements

- CI/CD using GitHub Actions
- API authentication
- Rate limiting
- Monitoring and logging
- Model versioning
- Frontend dashboard
- Kubernetes deployment
- Vertex AI integration

---

# Author

San D
