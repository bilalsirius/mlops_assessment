# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Upgrade pip 
RUN python -m pip install --upgrade pip
# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org --verbose -r requirements.txt

# Copy the rest of the application code into the container at /app
COPY . /app/

# Expose the port on which the application will listen
EXPOSE 8080

# Run the command to start the application
CMD ["python", "app.py"]