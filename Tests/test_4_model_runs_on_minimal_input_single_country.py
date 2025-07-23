# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

import pandas as pd
import os
import pytest


from src.load_data_and_prepare_inputs import load_data_and_prepare_inputs
from src.load_data_and_prepare_inputs.ensure_clean_directory import ensure_clean_directory
from src.part3_stock_calculation import calculate_and_plot_csps_and_stock
from src.part4_validate_model import compare_model_and_actual_stock_results


@pytest.mark.parametrize("input_dir", [
    "Tests/test_inputs_single_country",
    "Tests/test_inputs_single_country_reduced_years"
])
def test_model_runs_on_minimal_input(input_dir):
    """
    Test that the full BEV stock modeling workflow runs successfully on minimal input datasets.

    This test is parameterized to run twice:
    1. Using a dataset for a single country.
    2. Using a dataset for a single country with a reduced year range.

    For each case, the test:
    - Clears the output directories.
    - Loads data from the specified test input folder.
    - Runs CSP curve generation and BEV stock calculation.
    - Asserts that all output DataFrames are non-empty.
    - Executes the model validation step to confirm it handles reduced input gracefully.

    This ensures the model runs end-to-end without errors, even when working with small or simplified datasets.

    Raises:
        AssertionError: If any output DataFrame is unexpectedly empty.
    """
    # Clean output directories before running test
    ensure_clean_directory('outputs')
    ensure_clean_directory(os.path.join('outputs', 'figures'))
    # Use test-specific input folder
    test_data, test_inputs = load_data_and_prepare_inputs(input_dir)
    test_csp_and_stock_calculated_data = calculate_and_plot_csps_and_stock(test_data, test_inputs)
    # Simple assertion — check result is not empty
    for key, value in test_csp_and_stock_calculated_data.items():
        if isinstance(value, pd.DataFrame):
            assert not value.empty, f"'{key}' DataFrame is unexpectedly empty"
    compare_model_and_actual_stock_results(test_data, test_csp_and_stock_calculated_data, test_inputs)