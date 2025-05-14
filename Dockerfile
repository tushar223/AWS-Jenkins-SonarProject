# Use official Python image
FROM python:3.9

# Set working directory inside container
WORKDIR /app

# Copy all files into container
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables for Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Expose the port Flask will run on
EXPOSE 5000

# Command to run the app
CMD ["flask", "run"]
