# Import required modules
from src.load_data import load_data
from src.part3_stock_calculation import calculate_and_plot_csps_and_stock
from src.part4_validate_model import compare_model_and_actual_stock_results
from src.part5_sensitivity_analysis import perform_sensitivity_analysis


def model_european_bev_stock_shares_using_csp_curves():
    """
    Main function to model European BEV stock shares using CSP curves, compare the model to actual shares from 2014 to
    2023 and perform a sensitivity analysis modifying different variable parameters.

    Steps:
    1. Load data.
    2. Calculate and plot CSPs and stock.
    3. Compare model results with actual stock results.
    4. Perform sensitivity analysis.
    """
    # Step 1: Load data
    data = load_data()

    # Step 2: Calculate and plot CSPs and stock
    csp_and_stock_calculated_data = calculate_and_plot_csps_and_stock(data)

    # Step 3: Compare model results with actual stock results
    compare_model_and_actual_stock_results(data, csp_and_stock_calculated_data)

    # Step 4: Perform sensitivity analysis
    perform_sensitivity_analysis(data, csp_and_stock_calculated_data)


# Execute the main function when the script is run
if __name__ == "__main__":
    model_european_bev_stock_shares_using_csp_curves()



