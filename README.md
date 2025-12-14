# BLE Scanner Docker

## Prerequisites

- Install Docker

## Note

If you're using Windows, use `winscan.py` instead of `scan.py`. Docker is NOT needed for `winscan.py`.

## Build

```bash
docker build -t ble-app .
```

## Run

```bash
docker run --rm --net=host --privileged \
    -v /var/run/dbus/system_bus_socket:/var/run/dbus/system_bus_socket \
    --device /dev/hci0 \
    ble-app
```

## ML Model Checklist

Phase 1: Hardware & Environment Setup

BLE Hardware

 TP-Link USB BLE dongle (already purchased)

 Ensure proper drivers installed on Raspberry Pi (check with hciconfig)

Drone Integration

 Securely mount the Raspberry Pi and BLE dongle on the drone

 Make sure the dongle antenna is unobstructed and consistently oriented

 Verify power and vibration stability

Software Environment

 Install Raspberry Pi OS (Lite or Desktop)

 Install Python 3.13 or latest

 Install Bleak for BLE scanning (pip install bleak)

 Optionally set up Docker if you want containerized deployment

Phase 2: Data Collection

BLE Scanning

 Use your Python BLE scanner to log BLE advertisements

 Capture these fields:

MAC address

RSSI (signal strength)

Local name (if present)

Manufacturer data

Timestamp

Realistic Scenario Logging

 Collect data in environments similar to SAR scenarios

 Include devices carried by humans (phones, trackers)

 Include irrelevant BLE devices (smart home, environmental beacons)

 Vary distance, motion, and drone altitude if possible

Data Storage

 Save logs in a structured format (CSV or JSON)

 Keep track of which devices are human vs. non-human (for labeling)

Phase 3: Data Preprocessing & Feature Engineering

Data Cleaning

 Remove duplicates or corrupted entries

 Filter out incomplete advertisements

Feature Extraction

 RSSI statistics per short time window (mean, variance, trend)

 Encode manufacturer data into numerical features

 Encode local name (optional)

 Include advertisement frequency if detectable

Labeling

 Manually label devices as human/non-human

 Optionally label types: phone, smartwatch, beacon

Data Splitting

 Split data into training, validation, and test sets

 Ensure diverse environments in each set

Phase 4: Model Selection & Training

Model Choice

 Lightweight classifier (Random Forest or small MLP)

 Optional sequence model for tracking (LSTM/GRU)

Training

 Train on extracted features

 Validate accuracy on held-out set

 Track precision, recall (important to avoid false negatives in SAR)

 Tune hyperparameters for best balance of accuracy and speed

Optional Distance / Trend Estimation

 Use RSSI sequences to predict relative approach or retreat

 Could start with moving averages or simple regression

Phase 5: Real-Time Deployment on Pi

Integration

 Integrate trained model into BLE scanner script

 Maintain per-device history to track trends

 Flag human devices in real-time

Optimization

 Make sure model inference is lightweight (fits Pi’s CPU)

 Limit log frequency to avoid bottlenecks

Testing

 Run system indoors/outdoors

 Move devices around to simulate SAR targets

 Verify correct classification and tracking

Fail-Safes

 Ensure logs still save even if model crashes

 Allow manual override or real-time operator alerts

Phase 6: Optional Enhancements

Distance Estimation

 Consider multiple antennas or RSSI trend ML to estimate relative proximity

 Can assign “near/far” zones instead of exact meters

Multi-Drone Coordination

 Share BLE logs between drones to triangulate positions (future step)

Visualization

 Real-time console or web dashboard showing tracked devices and trends
