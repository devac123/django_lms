# Use Python 3.12.6 as the base image
FROM python:3.12.6-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requiremnts.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requiremnts.txt

# Copy the current directory contents into the container at /app
COPY . /app/

# Install additional system dependencies if needed
RUN apt-get update && apt-get install -y \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Expose port 8000 to the outside world
EXPOSE 8000

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Run database migrations, then start Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
