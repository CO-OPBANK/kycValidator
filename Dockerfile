FROM ubuntu:20.04

# Set proxy environment variables
ENV http_proxy http://172.30.100.1:8080
ENV https_proxy http://172.30.100.1:8080

# Set DEBIAN_FRONTEND to non-interactive mode
ENV DEBIAN_FRONTEND=noninteractive

# Install Python 3.10
RUN apt-get update && apt-get install -y python3.10 python3-pip

# Set the path to the pip binary in the PATH environment variable
ENV PATH="/usr/bin:$PATH"

# Set the Python path
ENV PYTHONPATH=/usr/local/lib/python3.10/site-packages

# Install Tesseract
RUN apt-get update && apt-get install -y tesseract-ocr

# Install FastAPI and other dependencies
RUN pip install --no-cache-dir --upgrade fastapi uvicorn pytesseract

# Copy the FastAPI app code
COPY . /app

# Set the working directory
WORKDIR /app

# Start the FastAPI app
CMD ["uvicorn", "app.main:app", "--host", "0.00.0.0", "--port", "8000"]
