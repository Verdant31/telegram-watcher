# Use the latest Amazon Linux 2023 image
FROM amazonlinux:2023

# Install Python 3.11 and pip
RUN yum update -y && \
    yum install -y python3.11 python3.11-pip git && \
    ln -sf /usr/bin/python3.11 /usr/bin/python3 && \
    ln -sf /usr/bin/pip3.11 /usr/bin/pip3

# Install required Python libraries
RUN pip3 install --upgrade pip && \
    pip3 install telethon boto3 twilio python-dotenv

# Create working directory
WORKDIR /app

# Copy your project files
COPY . .

# Set the default command
CMD ["python3", "monitor.py"]
