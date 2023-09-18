#!/bin/zsh

# Start the backend application
echo "Starting backend..."
python ~/PycharmProjects/MyBalance/main.py

# Start the frontend in a new Zsh terminal window
echo "Starting frontend in a new terminal window..."
osascript -e 'tell application "Terminal" to do script "cd ~/PycharmProjects/MyBalance/frontend/frontend-mybalance/ && yarn dev"'
