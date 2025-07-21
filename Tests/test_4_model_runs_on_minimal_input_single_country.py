import pandas as pd
import os


from src.load_data_and_prepare_inputs import load_data_and_prepare_inputs
from src.load_data_and_prepare_inputs.ensure_clean_directory import ensure_clean_directory
from src.part3_stock_calculation import calculate_and_plot_csps_and_stock
from src.part4_validate_model import compare_model_and_actual_stock_results
from src.part5_sensitivity_analysis import perform_sensitivity_analysis



input_dir = 'Tests/test_inputs_single_country'


def test_model_runs_on_minimal_input():
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