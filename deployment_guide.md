# Deployment Guide

This guide explains how to deploy the Power System Agent application. We use a **single container** approach where the Python backend serves the React frontend.

## Prerequisites

- **Docker Installed** (for local testing/building)
- **Google Cloud SDK** (if deploying to Cloud Run)
- **Git**

## Option 1: Google Cloud Run (Recommended)

Google Cloud Run is a fully managed serverless platform.

1.  **Install Google Cloud SDK** and login:
    ```bash
    gcloud auth login
    gcloud config set project YOUR_PROJECT_ID
    ```

2.  **Enable Services**:
    ```bash
    gcloud services enable run.googleapis.com cloudbuild.googleapis.com
    ```

3.  **Deploy**:
    Run this command from the root of your project:
    ```bash
    gcloud run deploy power-system-agent \
      --source . \
      --platform managed \
      --region us-central1 \
      --allow-unauthenticated
    ```
    *(Note: The `--source .` flag automatically builds your Dockerfile in the cloud.)*

4.  **Access**:
    The command will output a service URL (e.g., `https://power-system-agent-xyz-uc.a.run.app`). Open this in your browser.

## Option 2: Render.com / Railway

These platforms connect directly to your GitHub repository.

1.  Push your code to GitHub.
2.  Create a new **Web Service** on Render/Railway.
3.  Connect your repository.
4.  Select **Docker** as the runtime/environment.
5.  Deploy.

## Option 3: Local Docker

To test locally:

1.  **Build the image**:
    ```bash
    docker build -t power-system-agent .
    ```

2.  **Run the container**:
    ```bash
    docker run -p 8080:8080 power-system-agent
    ```

3.  Open `http://localhost:8080` in your browser.
