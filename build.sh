#!/bin/bash
set -e

echo "Python version:"
python3 --version

echo "Upgrading pip and build tools..."
pip install --upgrade pip setuptools wheel

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Build completed successfully!"

