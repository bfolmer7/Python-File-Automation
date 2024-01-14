# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container to /app
WORKDIR /app

# Copy the contents of the current directory to the container at /app
COPY . /app

# Install any needed packages specified in setup.py
RUN pip install .

# The USERPROFILE environment variable is Windows-specific and won't be available in the container.
# You need to set a default path for your script or adapt your script to work with a different environment variable.
# For example:
# ENV USERPROFILE=/app/Downloads

# Run file_organizer.py when the container launches
CMD ["python", "./file_organizer.py"]
