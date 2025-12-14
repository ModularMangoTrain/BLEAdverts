# Use Python slim for Raspberry Pi (ARM32)
FROM arm32v7/python:3.13-slim

# Install system dependencies for BLE
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        bluetooth \
        bluez \
        libdbus-1-dev \
        libglib2.0-dev \
        dbus \
        && rm -rf /var/lib/apt/lists/*

# Set workdir
WORKDIR /app

# Copy Python script
COPY scan.py .

# Install Python dependencies
RUN pip install --no-cache-dir bleak

# Default command
CMD ["python3", "scan.py"]
