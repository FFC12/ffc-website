# Python
FROM python:3.11-alpine

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install git
RUN apk add --no-cache git

# Install virtualenv
RUN pip install virtualenv

# Create a virtual environment and activate it
RUN virtualenv venv

# Activate the virtual environment
RUN source venv/bin/activate

# Install poetry
RUN pip install poetry

# Install poetry dependencies
RUN poetry export --without-hashes -f requirements.txt -o requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 8000

# Set environment variables
ENV PORT=8000

# Run main.py when the container launches background
CMD ["python", "main.py", "&"]


