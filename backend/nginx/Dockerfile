# Dockerfile for Nginx
FROM nginx:alpine

RUN mkdir -p /home/app/static
RUN mkdir -p /home/app/media

# Copy Nginx configuration
COPY nginx.conf /etc/nginx/conf.d/default.conf