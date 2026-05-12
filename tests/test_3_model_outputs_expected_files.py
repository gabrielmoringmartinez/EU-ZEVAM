# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

import os
import shutil
from zevampy.run_model import run_model


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
    if os.path.exists("outputs"):
        shutil.rmtree("outputs")

    run_model(config_path="config.yaml")

    expected_csv_files = [
        "1_1_absolute_registrations.csv",
        "1_2_registrations_by_powertrain.csv",
        "2_1_optimum_parameters_csp_curves.csv",
        "2_2_empirical_survival_rates.csv",
        "2_3_fitted_CSP_curves.csv",
        "3_1_stock_data_including_vehicle_age.csv",
        "3_2_stock_shares.csv",
    ]

    assert os.path.exists("outputs"), "Output folder was not created"
    actual_csv_files = os.listdir("outputs")

    missing_csv = [f for f in expected_csv_files if f not in actual_csv_files]
    assert not missing_csv, f"Missing expected CSV output files: {missing_csv}"

    expected_pdf_files = [
        "stock_shares_model_reference_scenario_BEV.pdf",
        "stock_shares_model_reference_scenario_Gasoline.pdf",
    ]

    figures_folder = os.path.join("outputs", "figures")
    assert os.path.exists(figures_folder), "'outputs/figures' folder was not created"
    actual_pdf_files = os.listdir(figures_folder)

    missing_pdfs = [f for f in expected_pdf_files if f not in actual_pdf_files]
    assert not missing_pdfs, f"Missing expected PDF output files in figures: {missing_pdfs}"