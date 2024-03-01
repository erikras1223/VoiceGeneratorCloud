# # Base image with Node.js and NPM for building the Angular app
# FROM node:12-alpine AS build

# # Set the working directory to /app
# WORKDIR /app



# # Copy the rest of the application code to the working directory
# COPY . .

# WORKDIR /app/frontend


# # Install the dependencies
# RUN npm install

# # Build the Angular app in production mode
# RUN npm run build-prod


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
# # COPY view.py .
# # COPY api.py .

# # Expose port 8080 for the container
EXPOSE 8084

# # Start the aiohttp server when the container starts
CMD ["python", "./src/server.py"]