# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

# Import required modules
import os
from src.load_data_and_prepare_inputs import load_data_and_prepare_inputs
from src.load_data_and_prepare_inputs.ensure_clean_directory import ensure_clean_directory
from src.part3_stock_calculation import calculate_and_plot_csps_and_stock
from src.part4_validate_model import compare_model_and_actual_stock_results
from src.part5_sensitivity_analysis import perform_sensitivity_analysis


def model_european_bev_stock_shares_using_csp_curves():
    """
    Main function to model the Battery Electric Vehicle (BEV) stock shares across European countries using Cumulative
    Survival Probability (CSP) curves. This function performs the full modeling workflow, including input loading,
    CSP curve generation, stock modeling, comparison with historical BEV data, and a sensitivity analysis.

    Steps:
    1. Load data and creates a dictionary for the user inputs.
    2. Calculates and plots CSPs and the stock share of BEVs across European countries.
    3. Compares the modeled results with actual BEV stock shares to evaluate the model's accuracy.
    4. Conducts a sensitivity analysis to explore how changes in input variables affect the model's results.

    Returns:
        None: This function performs the analysis and saves .csv and .pdf results to the 'outputs' folder.
    """
    # Clean and recreate 'outputs' and 'outputs/figures'
    ensure_clean_directory('outputs')
    ensure_clean_directory(os.path.join('outputs', 'figures'))

    # Step 1: Load data
    data, inputs = load_data_and_prepare_inputs()

    # Step 2: Calculate and plot CSPs and stock
    csp_and_stock_calculated_data = calculate_and_plot_csps_and_stock(data, inputs)

    # Step 3: Compare model results with actual stock results
    compare_model_and_actual_stock_results(data, csp_and_stock_calculated_data, inputs)

    # Step 4: Perform sensitivity analysis
    perform_sensitivity_analysis(data, csp_and_stock_calculated_data, inputs)


# Execute the main function when the script is run
if __name__ == "__main__":
    model_european_bev_stock_shares_using_csp_curves()


