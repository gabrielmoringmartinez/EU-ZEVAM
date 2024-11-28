from src.part5_sensitivity_analysis.relative_increase_decrease_csp_modified.modify_csps import modify_csps
from src.part2_survival_rates.get_fitted_csp_values import get_fitted_csp_values
from src.part3_stock_calculation.calculate_stock.calculate_stock import calculate_stock
from src.part5_sensitivity_analysis.relative_increase_decrease_csp_modified.generate_columns_to_plot import \
    generate_columns_to_plot
from src.part2_survival_rates.plot_survival_rates.plot_countries import plot_all_countries
from src.part5_sensitivity_analysis.update_stock_shares import update_stock_shares

from src.load_data_and_prepare_inputs.dimension_names import *

def do_sensitivity_analysis_with_increased_decreased_csps(registrations, survival_rates, optimum_parameters_wg,
                                                          optimal_distribution_dict, config):
    """
    Performs sensitivity analysis by modifying the Country-Specific Parameters (CSPs) for each country
    by increasing or decreasing them by a selected percentage. It recalculates stock shares for each
    modification and generates a plot comparing the results.

    Parameters:
        - registrations (pd.DataFrame): Registration data by year, powertrain, and country.
        - survival_rates (pd.DataFrame): Fitted survival rates for each country and vehicle age.
        - optimum_parameters_wg (dict): Optimal parameters for the CSP distribution (e.g., Weibull-Gaussian) for
            each country.
        - optimal_distribution_dict (dict): Dictionary specifying the optimal CSP distribution for each country
            (e.g., Weibull or Weibull-Gaussian).
        - config (dict): Configuration dictionary containing plotting parameters and sensitivity analysis settings:
            - `plot_params` (dict): Contains plotting settings such as:
                - `percentages_selected_label` (list): List of percentage adjustments to apply to the CSPs.
                - `csp_available_years_label` (str): Specifies which powertrain (e.g., 'BEV') to plot.
                - `simulation_stock_years_label` (list): Range of years for the stock simulation.
                - `powertrain_to_plot_label` (str): Powertrain type (e.g., 'BEV') to plot.


    Returns:
        None: This function updates the stock shares DataFrame and generates a plot for the sensitivity analysis.

    Description:
    1. **CSP Modification**:
       - For each percentage in `plot_params["percentages_selected"]`, the CSP parameters are modified by the specified
        percentage (either increased or decreased).
       - The modified CSP parameters are then fitted to the survival rates for each country.

    2. **Stock Calculation**:
       - The stock values and stock shares are recalculated using the modified CSP parameters.
       - The stock shares DataFrame is updated with the recalculated stock shares for each modification.

    3. **Plot Generation**:
       - The stock shares for the specified powertrain (e.g., 'BEV') are filtered from the recalculated stock shares.
       - The `generate_columns_to_plot` function is used to generate the column names and labels for the plot legend,
       corresponding to the modified CSP percentages.
       - The results are plotted using the `plot_all_countries` function, visualizing the effect of the CSP adjustments
        on stock shares across different countries.

    This analysis provides insights into how changing CSPs (by increasing or decreasing them) affects stock share
     projections, helping to assess the sensitivity of stock projections to CSP variations.
    """
    plot_params = config[plot_params_dim]
    columns_to_plot = {}
    stock_shares_df = None
    for percentage in plot_params[percentages_selected_label]:
        adjusted_parameters = modify_csps(optimum_parameters_wg, percentage)
        fitted_csp_values = get_fitted_csp_values(survival_rates, adjusted_parameters, True,
                                                  plot_params[csp_available_years_label])
        stock_values, stock_shares = calculate_stock(registrations, fitted_csp_values, optimal_distribution_dict,
                                                     plot_params[simulation_stock_years_label], 'non-historical_csp')
        stock_shares_df = update_stock_shares(stock_shares_df, stock_shares, percentage)
    bev_stock_shares = stock_shares_df[stock_shares_df[powertrain_dim] == plot_params[powertrain_to_plot_label]]
    columns_to_plot = generate_columns_to_plot(columns_to_plot, plot_params[percentages_selected_label])
    plot_all_countries(bev_stock_shares, config, columns_to_plot, None)
    return



