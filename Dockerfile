# Stage 1: Build React Frontend
FROM node:18-slim as build-step
WORKDIR /app/web
COPY web/package*.json ./
RUN npm install
COPY web/ ./
RUN npm run build

# Stage 2: Python Backend
FROM python:3.10-slim

# Install system dependencies (needed for some compiled Python packages)
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Copy built frontend from Stage 1
COPY --from=build-step /app/web/dist /app/web/dist

# Expose port (Google Cloud Run expects 8080 by default)
EXPOSE 8080

# Run the application
# We use Gunicorn with Uvicorn workers for production
CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "src.api.main:app", "--bind", "0.0.0.0:8080"]
