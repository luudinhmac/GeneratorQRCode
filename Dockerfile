# Use an official Python runtime as the base image
FROM python:3.8-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn
# Copy the rest of the application files to the container
COPY app/app.py .
COPY . .

# Set the environment variable for Flask
ENV FLASK_APP=app.py

# Set the environment variable for Flask debug mode
ENV FLASK_DEBUG=0

# Expose port 5000 to the host
EXPOSE 5000

# Run the command to start Gunicorn
CMD ["gunicorn", "app:app", "--bind=0.0.0.0:5000"]

