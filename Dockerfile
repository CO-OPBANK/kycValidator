FROM python:3.10

#Set the working directory
WORKDIR /app

#Set DEBIAN_FRONTEND to non-interactive mode
ENV DEBIAN_FRONTEND=noninteractive

#Install Dependancies
RUN apt-get update && apt-get install -y python3-pip tesseract-ocr tesseract-ocr-eng

COPY requirements.txt requirements.txt

#Install FastAPI and other dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

#Copy the FastAPI app code
COPY . /app

#Set proxy environment variables
#ENV http_proxy http://172.30.100.1:8080
#ENV https_proxy http://172.30.100.1:8080

# Start the FastAPI app
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
