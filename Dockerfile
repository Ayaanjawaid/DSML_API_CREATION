# Use the Python 3.13 Slim image as the base
FROM python:3.11

# Set the working directory in the container
WORKDIR /flask-docker

# Copy the current directory content into the container's /app directory
COPY requirements.txt requirements.txt

RUN python3 -m pip install --upgrade pip

# Install the required libraries from requirements.txt

RUN pip install -r requirements.txt

COPY . .

# Run the Flask application
CMD ["python", "-m", "flask", "--app", "loan_status", "run" ,"--host=0.0.0.0"]