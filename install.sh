#!/bin/bash

echo "Installing SafePulse Cyber Hygiene Scanner"

# Check for Python
if ! command -v python3 &> /dev/null; then
    echo "Python3 is required but not installed. Please install Python3 first."
    exit 1
fi

# Check for pip
if ! command -v pip3 &> /dev/null; then
    echo "pip3 is required but not installed. Please install pip3 first."
    exit 1
fi

# Install dependencies
echo "Installing Python dependencies..."
pip3 install -r requirements.txt

# Install optional tools (for Kali Linux)
if grep -qi "kali" /etc/os-release; then
    echo "Kali Linux detected. Installing recommended tools..."
    sudo apt update
    sudo apt install -y chkrootkit nmap ufw
fi

# Make scripts executable
chmod +x src/safepulse.sh
chmod +x src/scanner.py

echo "Installation complete!"
echo "Run SafePulse with: ./src/safepulse.sh"
