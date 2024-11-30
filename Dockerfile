# Use an official Python runtime as the base image
FROM python:3.9-slim

# RUN apt-get update && apt-get install -y \
#     wget \
#     curl \
#     gnupg \
#     unzip \
#     libnss3 \
#     libgdk-pixbuf2.0-0 \
#     libatk-bridge2.0-0 \
#     libxcomposite1 \
#     libxrandr2 \
#     libasound2 \
#     libxss1 \
#     ca-certificates \
#     fonts-liberation \
#     libnspr4 \
#     libx11-xcb1 \
#     libx11-dev \
#     libdrm2 \
#     libgbm1 \
#     libvulkan1 \
#     xdg-utils \
#     && rm -rf /var/lib/apt/lists/*

# # Install Google Chrome
# RUN curl -sS https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -o google-chrome-stable_current_amd64.deb && \
#     dpkg -i google-chrome-stable_current_amd64.deb && \
#     apt-get install -f && \
#     rm google-chrome-stable_current_amd64.deb
RUN apt-get update && apt-get install -y
RUN apt -f install -y
RUN apt-get install -y wget
RUN wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt-get install ./google-chrome-stable_current_amd64.deb -y
RUN rm google-chrome-stable_current_amd64.deb
# Install chromedriver
RUN apt-get update && apt-get install -y chromium-driver
# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose the port
EXPOSE 5000

# Use Gunicorn to serve the Flask app
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
