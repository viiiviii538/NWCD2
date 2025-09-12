#!/usr/bin/env bash
set -e

# Setup Python virtual environment if requirements.txt or requirements-dev.txt exists
if [ -f "requirements.txt" ] || [ -f "requirements-dev.txt" ]; then
    echo "Creating Python virtual environment..."
    python3 -m venv .venv
    # shellcheck disable=SC1091
    source .venv/bin/activate
    echo "✅ Virtual environment ready."

    echo "Upgrading pip..."
    pip install --upgrade pip
    echo "✅ pip upgraded."

    if [ -f "requirements.txt" ]; then
        echo "Installing Python dependencies from requirements.txt..."
        pip install -r requirements.txt
        echo "✅ requirements.txt installed."
    fi

    if [ -f "requirements-dev.txt" ]; then
        echo "Installing Python development dependencies from requirements-dev.txt..."
        pip install -r requirements-dev.txt
        echo "✅ requirements-dev.txt installed."
    fi
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

echo "✅ Setup complete."
