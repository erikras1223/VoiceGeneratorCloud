

# Use official Python runtime as a parent image
FROM python:3.10-slim-buster

# Set the working directory in the container to /app
WORKDIR /app



# Copy the requirements.txt file to the container's /app directory
COPY . .

# Install the required packages using pip
RUN pip install -r requirements.txt

# Set the working directory to /app/static, where we will copy the static files
#WORKDIR /app/static

# Copy the built Angular files from the build image to the /app/static directory
#COPY --from=build /app/frontend/dist/* .

# Set the working directory back to /app
WORKDIR /app

# # Copy the aiohttp server files to the container's /app directory
# COPY backend/* .
# COPY view.py .
# COPY api.py .
# RUN python -m pip install --upgrade debugpy
# Set the environment variable PYTHONUNBUFFERED to prevent Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED=1

# Set the logging level to DEBUG
ENV LOG_LEVEL=DEBUG

# # Expose port 8080 for the container
EXPOSE 8086



# # Start the aiohttp server when the container starts
CMD ["python", "./src/server.py"]