# 1. Base Image: Use official lightweight Python image
FROM python:3.11-slim

# 2. Set working directory in container
WORKDIR /app

# 3. Optimize Python execution (avoid .pyc files & enable immediate stdout logging)
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# 4. Copy dependency definition file
COPY requirements.txt .

# 5. Install Python dependencies without caching wheels to keep image lean
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copy remaining application files
COPY . .

# 7. Expose the port the app listens on
EXPOSE 5000

# 8. Define default command to start the web service
CMD ["python", "app.py"]
