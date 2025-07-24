# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

import os
import shutil
from model_european_passenger_car_stock import model_european_bev_stock_shares_using_csp_curves


def test_model_outputs_expected_files():
    """
    Test that the main BEV stock share model runs successfully and produces all expected output files.

    This test:
    - Removes any existing 'outputs' folder to ensure a clean run.
    - Executes the main modeling function.
    - Checks that the 'outputs' directory is created.
    - Verifies that all expected CSV files are generated in 'outputs'.
    - Verifies that all expected PDF files are generated in 'outputs/figures'.

    Raises:
        AssertionError: If the 'outputs' folder or 'outputs/figures' folder is missing,
                        or if any expected output CSV or PDF files are not found.
    """
    # Clean up any old outputs
    if os.path.exists('outputs'):
        shutil.rmtree('outputs')

    # Run the main model
    model_european_bev_stock_shares_using_csp_curves()

    # Define expected CSV files in 'outputs'
    expected_csv_files = [
        "1_1_absolute_registrations.csv",
        "1_2_registrations_by_powertrain.csv",
        "2_1_optimum_parameters_csp_curves.csv",
        "2_2_empirical_survival_rates_eu_countries_2021.csv",
        "2_3_fitted_CSP_curves.csv",
        "3_1_stock_data_including_vehicle_age.csv",
        "3_2_stock_shares.csv",
        "4_1_rmse_validation_step_1_actual_new_bev_registrations_and_empirical_csp_curves_all_countries.csv",
        "4_2_rmse_validation_step_2_estimated_new_bev_registrations_and_empirical_csp_curves_all_countries.csv",
    ]

    # Check CSVs in 'outputs'
    assert os.path.exists("outputs"), "Output folder was not created"
    actual_csv_files = os.listdir("outputs")

    missing_csv = [f for f in expected_csv_files if f not in actual_csv_files]
    assert not missing_csv, f"Missing expected CSV output files: {missing_csv}"

    # Define expected PDFs in 'outputs/figures'
    expected_pdf_files = [
        "battery_electric_vehicle_stock_shares_eu_27_and_norway_up_to_2050_model_reference_scenario_.pdf",
        "battery_electric_vehicle_stock_shares_eu_27_and_norway_up_to_2050_with_increased_decreased_country_csps_.pdf",
        "battery_electric_vehicle_stock_shares_eu_27_and_norway_up_to_2050_with_modified_country_csps_.pdf",
        "battery_electric_vehicle_stock_shares_eu_27_and_norway_up_to_2050_with_modified_historical_country_csps_.pdf",
        "battery_electric_vehicle_stock_shares_eu_27_and_norway_up_to_2050_with_modified_registrations_.pdf",
        "validation_step_1_actual_new_bev_registrations_and_empirical_csp_curves_all_countries.pdf",
        "validation_step_2_actual_new_bev_registrations_and_empirical_csp_curves_all_countries.pdf",
    ]

    figures_folder = os.path.join("outputs", "figures")
    assert os.path.exists(figures_folder), "'outputs/figures' folder was not created"
    actual_pdf_files = os.listdir(figures_folder)

    missing_pdfs = [f for f in expected_pdf_files if f not in actual_pdf_files]
    assert not missing_pdfs, f"Missing expected PDF output files in figures: {missing_pdfs}"