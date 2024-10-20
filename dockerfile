# Dockerfile
FROM python:3.12-slim

WORKDIR /app

# Copy and install requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire app to the container
COPY . .

# Environment variable to keep Python output unbuffered
ENV PYTHONUNBUFFERED=1

# Expose port 8000 for Django
EXPOSE 8000

# Run the Django application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
