#!/usr/bin/env bash
set -e

# Setup Python virtual environment if requirements.txt exists
if [ -f "requirements.txt" ]; then
    echo "Creating Python virtual environment..."
    python3 -m venv .venv
    # shellcheck disable=SC1091
    source .venv/bin/activate
    echo "Installing Python dependencies from requirements.txt..."
    pip install --upgrade pip
    pip install -r requirements.txt
fi

# Install Node dependencies if package.json exists
if [ -f "package.json" ]; then
    echo "Installing Node dependencies..."
    npm install
fi

# Initialize Flutter project if pubspec.yaml exists
if [ -f "pubspec.yaml" ]; then
    echo "Fetching Flutter dependencies..."
    flutter pub get
fi

echo "Setup complete."
