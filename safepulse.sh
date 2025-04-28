#!/bin/bash

# SafePulse - Cyber Hygiene Auto-Scanner
# Version 0.1.0

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check if running as root
if [ "$(id -u)" -ne 0 ]; then
    echo -e "${YELLOW}Warning: Some checks require root privileges. Consider running with sudo.${NC}"
fi

# Main menu
echo -e "${GREEN}"
echo "   _____       _____           _ "
echo "  / ____|     |  __ \         | |"
echo " | (___   __ _| |__) |__  _ __| |"
echo "  \___ \ / _\` |  ___/ _ \| '__| |"
echo "  ____) | (_| | |  | (_) | |  | |"
echo " |_____/ \__, |_|   \___/|_|  |_|"
echo "          __/ |                  "
echo "         |___/                   "
echo -e "${NC}"
echo "Your System's Heartbeat of Security"
echo "----------------------------------"

# Run basic checks
echo -e "\n${YELLOW}[*] Starting basic system checks...${NC}"

# Check internet connection
if ping -c 1 google.com &> /dev/null; then
    echo -e "${GREEN}[+] Internet connection: OK${NC}"
else
    echo -e "${RED}[-] No internet connection detected${NC}"
fi

# Check for root
if [ "$(id -u)" -eq 0 ]; then
    echo -e "${GREEN}[+] Running as root${NC}"
else
    echo -e "${YELLOW}[!] Not running as root (some checks may be limited)${NC}"
fi

# Call Python scanner
echo -e "\n${YELLOW}[*] Running security checks...${NC}"
python3 src/scanner.py

# Final message
echo -e "\n${GREEN}Scan complete!${NC}"
echo "For detailed recommendations, please visit https://safepulse.github.io"
