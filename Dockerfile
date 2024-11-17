# Use a lightweight Python base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy requirements and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source and test files
COPY src/ ./src
COPY tests/ ./tests

# Set the default command
CMD ["pytest", "tests/"]