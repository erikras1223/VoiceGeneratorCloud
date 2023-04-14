# Remove default nginx configuration
# Stage 1: Install and build frontend assets
FROM node:12-alpine as build-stage
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY ./ ./
RUN npm run build

# Stage 2: Serve the frontend files using nginx
FROM nginx:alpine
COPY --from=build-stage /app/dist/VoiceGeneratorCloud/ /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 8080
CMD ["nginx", "-g", "daemon off;"]



# # Copy the rest of the application code to the working directory
# COPY . .

# WORKDIR /app/frontend