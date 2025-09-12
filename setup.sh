#!/usr/bin/env bash
set -e

# Setup Python virtual environment
python3 -m venv .venv
# shellcheck disable=SC1091
source .venv/bin/activate
echo "✅ Python virtual environment ready."

# Upgrade pip
pip install --upgrade pip
echo "✅ pip upgraded."

# Install Python dependencies
if [ -f "requirements.txt" ]; then
    echo "Installing dependencies from requirements.txt..."
    pip install -r requirements.txt
    echo "✅ requirements installed."
fi

if [ -f "requirements-dev.txt" ]; then
    echo "Installing dependencies from requirements-dev.txt..."
    pip install -r requirements-dev.txt
    echo "✅ dev requirements installed."
fi

# Install Node dependencies if package.json exists
if [ -f "package.json" ]; then
    echo "Installing Node dependencies..."
    npm install
    echo "✅ Node dependencies installed."
fi

# Initialize Flutter project if pubspec.yaml exists
if [ -f "pubspec.yaml" ]; then
    echo "Fetching Flutter dependencies..."
    flutter pub get
    echo "✅ Flutter dependencies fetched."
fi

echo "✅ Setup complete."
