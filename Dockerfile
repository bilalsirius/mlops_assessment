# Use an official Python runtime as a parent image
FROM python:3.8

COPY . /app

WORKDIR /app

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt


# Run the command to start the application
CMD python server.py
