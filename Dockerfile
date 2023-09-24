#FROM python:3.11.2

#ENV PYTHONUNBUFFERED 1

#COPY app /app/app
#WORKDIR /app

#COPY pyproject.toml poetry.lock /app/
#RUN pip install poetry && poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

#EXPOSE 8000
#CMD ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
# Use the official Python image as the base image
FROM python:3.9-slim

# Set environment variables to ensure that Python outputs are not buffered
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the poetry files and install dependencies
COPY pyproject.toml poetry.lock /app/
RUN pip install poetry && poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

# Copy the FastAPI application code into the container
COPY app /app/app

# Expose port 8000
EXPOSE 8000

# Run the FastAPI application using Uvicorn
CMD ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
