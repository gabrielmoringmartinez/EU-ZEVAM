#!/bin/bash

# Exit when any command fails
set -e

# Install required dependencies
pip install -r stock_model_requirements.txt
echo "Successfully installed required packages"

# Check the code using the flake8 linter
flake8 --max-line-length 120 astronaut-analysis.py

# Check that the script is basically working and creating the same results
python model_european_passenger_car_stock.py
test -f outputs/figures/CSP 2021_all_countries.pdf
test -f outputs/figures/battery_electric_vehicle_stock_shares_eu_27_and_norway_up_to_2050_model_reference_scenario_.pdf
test -f outputs/figures/validation_step_1_actual_new_bev_registrations_and_empirical_csp_curves_all_countries.pdf
test -f outputs/figures/validation_step_2_actual_new_bev_registrations_and_empirical_csp_curves_all_countries.pdf
test -f outputs/figures/battery_electric_vehicle_stock_shares_eu_27_and_norway_up_to_2050_with_modified_country_csps_.pdf
test -f outputs/figures/battery_electric_vehicle_stock_shares_eu_27_and_norway_up_to_2050_with_modified_historical_country_csps_.pdf
test -f outputs/figures/battery_electric_vehicle_stock_shares_eu_27_and_norway_up_to_2050_with_increased_decreased_country_csps_.pdf
test -f outputs/figures/battery_electric_vehicle_stock_shares_eu_27_and_norway_up_to_2050_with_modified_registrations_XXX.pdf
echo "Successfully created the plots"
