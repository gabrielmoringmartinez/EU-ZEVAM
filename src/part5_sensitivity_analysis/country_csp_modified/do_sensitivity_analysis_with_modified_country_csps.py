from src.part2_survival_rates.plot_survival_rates.plot_all_countries import plot_all_countries
from src.part3_stock_calculation.calculate_stock.calculate_stock import calculate_stock
from src.part5_sensitivity_analysis.country_adjectives import country_adjectives
from src.part5_sensitivity_analysis.country_csp_modified.replace_survival_rates_with_country_specific_csp import \
    replace_survival_rates_with_country_specific_csp
from src.part5_sensitivity_analysis.country_csp_modified.update_optimal_distribution import \
    update_optimal_distribution_based_on_country_csp
from src.part5_sensitivity_analysis.country_csp_modified.generate_columns_to_plot import generate_columns_to_plot
from src.part5_sensitivity_analysis.update_stock_shares import update_stock_shares

from src.load_data_and_prepare_inputs.dimension_names import *


def do_sensitivity_analysis_with_modified_country_csps(registrations, stock_shares, survival_rates,
                                                      optimal_distribution_dict, config):
    """
    Performs sensitivity analysis by modifying country-specific CSPs (Country Survival Probabilities) to other
    countries and keeps the registrations by powertrain constant. Then, it recalculates stock shares
    to assess the impact of changes.

    Parameters:
        - registrations (pd.DataFrame): Registration data by year, powertrain and country.
        - stock_shares (pd.DataFrame): Stock share data calculated over time, country and powertrain.
        - survival_rates (pd.DataFrame): Fitted survival rates for each country and vehicle age.
        - optimal_distribution_dict (dict): Dictionary containing the optimal CSP distribution
        (e.g., Weibull or Weibull-Gaussian) for each country.
        - config (dict): Configuration dictionary that contains plotting parameters and sensitivity analysis options:
          - `plot_params` (dict): Plotting settings including:
            - `countries_selected` (list): Country CSP are modified to the countries selected
            - `simulation_stock_years_label` (list): Years over which the stock analysis is computed.
            - `historical_csp_label` (str): Indicates if historical CSP data is used.
            - `powertrain_to_plot_label` (str): Powertrain type (e.g., 'BEV') to plot.

        Returns:
        - None: Generates plots and updates dataframes as part of the sensitivity analysis.

        Description:
        1. **Country-Specific CSP Replacement**:
           - Replaces survival rates to all countries with the selected countries.
           - Updates optimal distribution parameters for each country based on the optimal distribution of the selected
           country.

        2. **Stock Calculation**:
           - Recalculates stock values and shares using the modified CSPs and updated distributions.
           - Updates the stock shares dataframe for each country.

        3. **Plot Generation**:
           - Filters BEV (Battery Electric Vehicle) stock shares for the selected powertrain.
           - Plots the recalculated stock shares for all countries using `plot_all_countries`.

        This analysis evaluates how country-specific CSP adjustments affect stock share projections,
        enabling insights into sensitivity across different CSP assumptions.
        """
    plot_params = config[plot_params_dim]
    columns_to_plot = {share_dim: share_dim.capitalize()}
    stock_shares_df = stock_shares
    for country in plot_params[countries_selected_label]:
        updated_survival_rates = replace_survival_rates_with_country_specific_csp(survival_rates, country)
        updated_opt_dist_dict = update_optimal_distribution_based_on_country_csp(country, optimal_distribution_dict)
        stock_values, stock_shares = calculate_stock(registrations, updated_survival_rates, updated_opt_dist_dict,
                                                     plot_params[simulation_stock_years_label],
                                                     plot_params[historical_csp_label])
        stock_shares_df = update_stock_shares(stock_shares_df, stock_shares, country)
        columns_to_plot = generate_columns_to_plot(columns_to_plot, plot_params[countries_selected_label],
                                                   country_adjectives)
    bev_stock_shares = stock_shares_df[stock_shares_df[powertrain_dim] == plot_params[powertrain_to_plot_label]]
    plot_all_countries(bev_stock_shares, config, columns_to_plot, None)
