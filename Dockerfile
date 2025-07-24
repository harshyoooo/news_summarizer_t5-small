# Use official Python 3.10 base image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Expose port
EXPOSE 8000
WORKDIR /app/summarizer_project1
# Run server using Gunicorn
CMD ["gunicorn", "summarizer_project.wsgi:application", "--bind", "0.0.0.0:8000"]
