#!/bin/bash

set -e

# Ensure script runs from its own directory
cd "$(dirname "$0")"

# Create virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv .venv
fi

# Activate virtual environment
source .venv/bin/activate

# Install dependencies if requirements.txt exists
if [ -f "requirements.txt" ]; then
    echo "Installing dependencies..."
    python -m pip install -r requirements.txt
else
    echo "No requirements file to install from."
fi

# Create .env if it doesn't exist
if [ ! -f ".env" ]; then
    echo "Creating .env file..."

    cat > .env <<EOF
DISCORD_TOKEN=""
LOGGING_DIRECTORY=""
EOF

    echo ".env created. Please fill in the required values before running the application."
    exit 0
fi

# Start application
echo "Starting application..."
python -m app.main