FROM ubuntu:22.04

# Avoid interactive prompts during installation
ENV DEBIAN_FRONTEND=noninteractive

# Update and install Ansible, Python, and Pip
RUN apt-get update && \
    apt-get install -y ansible python3-pip && \
    rm -rf /var/lib/apt/lists/*

# Numpy library for the Python script
RUN pip3 install numpy

# Set the working directory inside the container
WORKDIR /project