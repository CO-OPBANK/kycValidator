FROM python:3.10

# Set the working directory
WORKDIR /app

# Set DEBIAN_FRONTEND to non-interactive mode
ENV DEBIAN_FRONTEND=noninteractive

# Install Dependencies
RUN apt-get update && apt-get install -y python3-pip tesseract-ocr tesseract-ocr-eng

# Additional dependencies for libGL.so.1
RUN apt-get install -y libgl1-mesa-glx

# Set environment variables
ENV TESS_CONFIG="--psm 11 --oem 3"
ENV AWS_REGION=us-west-2
ENV AWS_ACCESS_KEY_ID=AKIATV7T4KLWHI2ELWWZ
ENV AWS_SECRET_ACCESS_KEY=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

# Copy requirements file
COPY requirements.txt requirements.txt

# Install FastAPI and other dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy FastAPI app code
COPY . /app

# Set proxy environment variables
# ENV http_proxy http://172.30.100.1:8080
# ENV https_proxy http://172.30.100.1:8080

# Start the FastAPI app
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
