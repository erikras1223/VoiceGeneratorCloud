# Remove default nginx configuration
# # Stage 1: Install and build frontend assets
FROM node:12-alpine as build-stage
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY ./ ./
RUN npm run build-prod

# # Stage 2: Serve the frontend files using nginx
# FROM nginx:alpine
# COPY --from=build-stage /app/dist/VoiceGeneratorCloud/ /usr/share/nginx/html
# COPY nginx.conf /etc/nginx/conf.d/default.conf
# EXPOSE 8080
# CMD ["nginx", "-g", "daemon off;"]


FROM debian:buster


ARG BUILD_NGINX_VERSION=1.23.4
ARG INSTALL_AT=/opt/nginx

ENV NGINX_VERSION=$BUILD_NGINX_VERSION
ENV INSTALL_LOCATION=$INSTALL_AT

RUN set -x \
    && apt-get update \
    && apt-get install --no-install-recommends --no-install-suggests -y \
        build-essential \
        wget \
        git \
        libpcre3-dev \
        zlib1g-dev \
        ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Download, untar and symlink
WORKDIR /src
RUN set -x \
    && wget http://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz \
    && tar -xzf nginx-${NGINX_VERSION}.tar.gz \
    && ln -sf nginx-${NGINX_VERSION} nginx \
    && git clone https://github.com/perusio/nginx-auth-request-module.git

# Build
WORKDIR /src/nginx
RUN set -x \
    && ./configure \
    --user=nginx \
    --group=nginx \
    --prefix=${INSTALL_LOCATION} \
    --with-http_stub_status_module \
    --with-pcre \
    --with-http_realip_module \
    --with-http_auth_request_module \
    --without-http_scgi_module \
    --without-http_uwsgi_module \
    --without-http_fastcgi_module \
    --with-debug 
    

COPY --from=build-stage /app/dist/VoiceGeneratorCloud/ /opt/nginx/html
COPY ./nginx/nginx.conf  /opt/nginx/conf/nginx.conf
COPY ./nginx/conf.d/default.conf  /opt/nginx/conf.d/default.conf


# Compile and instasll
RUN set -x && make && make install

# Add the user to the system
RUN set -x && useradd -r nginx

# Forward request and error logs to docker log collector
RUN ln -sf /dev/stdout ${INSTALL_LOCATION}/logs/access.log \
    && ln -sf /dev/stderr ${INSTALL_LOCATION}/logs/error.log

# Start nginx
EXPOSE 8080
STOPSIGNAL SIGTERM
WORKDIR ${INSTALL_LOCATION}
CMD ["./sbin/nginx", "-g", "daemon off;"]


# # Copy the rest of the application code to the working directory
# COPY . .

# WORKDIR /app/frontend