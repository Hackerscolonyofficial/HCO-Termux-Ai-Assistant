#!/data/data/com.termux/files/usr/bin/bash

set -e

CYAN='\033[96m'
GREEN='\033[92m'
YELLOW='\033[93m'
RESET='\033[0m'

echo -e "${CYAN}==============================================${RESET}"
echo -e "${CYAN}     HCO TERMUX ASSISTANT INSTALLER${RESET}"
echo -e "${CYAN}==============================================${RESET}"

echo

echo -e "${YELLOW}Updating Termux packages...${RESET}"

pkg update -y

echo -e "${YELLOW}Installing required packages...${RESET}"

pkg install -y python git iproute2 net-tools

chmod +x hco_termux_assistant.py

echo

echo -e "${GREEN}Installation complete.${RESET}"

echo

echo -e "${GREEN}Run the tool with:${RESET}"

echo "python hco_termux_assistant.py"

echo

echo "The YouTube redirect URL is already configured in the script."
