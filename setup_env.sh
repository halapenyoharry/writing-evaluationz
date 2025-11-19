#!/bin/bash

# Create a Python virtual environment
python3 -m venv venv_novel

# Activate the virtual environment
source venv_novel/bin/activate

# Install dependencies from requirements.txt
pip install -r requirements.txt

# Download the NLTK corpora
python -m textblob.download_corpora

echo "Setup complete. To activate the virtual environment, run: source venv_novel/bin/activate"
