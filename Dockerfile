# Use the official lightweight Python image as a base image
FROM python:3.11.7

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install Jupyter
RUN pip install jupyter

# Install flasgger
RUN pip install flasgger

# Define environment variable
ENV FLASK_APP=finalproject.py

# Expose port 5003 to the outside world
EXPOSE 5003

# Run flask when the container launches
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5003"]
