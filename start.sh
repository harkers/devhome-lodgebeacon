#!/bin/bash
# Display Forge - Startup Script

set -e

echo "🔨 Starting Display Forge..."

# Check if database exists
if [ ! -f "data/display-forge.db" ]; then
    echo "📦 Initializing database..."
    python3 scripts/init-db.py
fi

# Install dependencies if needed
if [ ! -d "backend/__pycache__" ]; then
    echo "📦 Installing dependencies..."
    pip3 install -r backend/requirements.txt
fi

# Start the server
echo "🚀 Starting Flask server on port 5000..."
cd backend
python3 app.py
