# SPDX-FileCopyrightText: 2025 German Aerospace Center
# SPDX-License-Identifier: CC0-1.0
#!/bin/bash

# Exit when any command fails
set -e

# Install required dependencies
pip install -r stock_model_requirements.txt
echo "Successfully installed required packages"

# Run tests
#pytest model_european_passenger_car_stock_test.py --junitxml=pytest.xml
#echo "Successfully ran tests"

# Check the code using the ruff linter
#ruff check --select ALL --ignore PTH,T,PLR,ANN,D205 --output-file=ruff.json --output-format=gitlab model_european_passenger_car_stock.py
#echo "Successfully ran ruff checks"
# Check that copyright and license information for all files is available

# Check that the script is basically working and creating the same results
python model_european_passenger_car_stock.py
#test -f "outputs/figures/CSP 2021_all_countries.pdf"
test -f "outputs/figures/battery_electric_vehicle_stock_shares_eu_27_and_norway_up_to_2050_model_reference_scenario_.pdf"
test -f "outputs/figures/validation_step_1_actual_new_bev_registrations_and_empirical_csp_curves_all_countries.pdf"
test -f "outputs/figures/validation_step_2_actual_new_bev_registrations_and_empirical_csp_curves_all_countries.pdf"
test -f "outputs/figures/battery_electric_vehicle_stock_shares_eu_27_and_norway_up_to_2050_with_modified_country_csps_.pdf"
test -f "outputs/figures/battery_electric_vehicle_stock_shares_eu_27_and_norway_up_to_2050_with_modified_historical_country_csps_.pdf"
test -f "outputs/figures/battery_electric_vehicle_stock_shares_eu_27_and_norway_up_to_2050_with_increased_decreased_country_csps_.pdf"
test -f "outputs/figures/battery_electric_vehicle_stock_shares_eu_27_and_norway_up_to_2050_with_modified_registrations_.pdf"
echo "Successfully created the plots"

reuse lint