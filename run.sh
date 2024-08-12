#!/bin/bash

if [ -z "$VIRTUAL_ENV" ]; then
    echo "Activating virtual environment..."
    # Active l'environnement virtuel
    source env/bin/activate
fi

if [ -z "$VIRTUAL_ENV" ]; then
    echo "Failed to activate virtual environment."
    exit 1
fi

echo "Running main.py..."
python3 main.py
