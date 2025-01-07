# HTTP Endpoint Health Checker

## Overview
This program monitors the health of HTTP endpoints, logs their availability, and calculates domain-wise availability percentages over time.

## Features
- Reads HTTP endpoints from a YAML configuration file.
- Sends periodic requests to endpoints and checks their status.
- Logs cumulative availability percentages for each domain.

## Setup Instructions
1. Clone the repository to your local machine.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
3. Run the program with a YAML configuration file:
   ```bash
    python main.py config.yaml

## Test Instructions
   Execute the test Script
   ```bash
   pytest test_health_check.py
   

