FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Railway dynamically assigns PORT via environment variable
# Default to 8000 for local development
ENV PORT=8000

# Run the application - use shell form to allow variable substitution
CMD uvicorn app.main:app --host 0.0.0.0 --port $PORT
