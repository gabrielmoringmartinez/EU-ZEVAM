#!/bin/bash

# Exit when any command fails
set -e

# Install required dependencies
pip install -r stock_model_requirements.txt
echo "Successfully installed required packages"

# Run tests
#pytest model_european_passenger_car_stock_test.py --junitxml=pytest.xml
#echo "Successfully ran tests"
