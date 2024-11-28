from src.part5_sensitivity_analysis.historical_csp_modified.process_historical_csp import process_stock_shares_with_historical_csps
from src.part5_sensitivity_analysis.historical_csp_modified.generate_columns_to_plot import generate_columns_to_plot
from src.part2_survival_rates.plot_survival_rates.plot_countries import plot_all_countries

from src.load_data_and_prepare_inputs.dimension_names import *


def do_sensitivity_analysis_with_historical_country_csps(registrations, survival_rates_2021, survival_rates_2016,
                                                         optimum_parameters_2008, optimal_distribution_dict, config,
                                                         bound_distributions, csp_available_years):
    """
    Perform sensitivity analysis using historical country-specific CSP data (from 2008 and 2016), processes stock shares
    based on this data, and generates a plot comparing the results.

    Parameters:
        - registrations (pd.DataFrame): Registration data by year, powertrain and country.
        - survival_rates_2021 (pd.DataFrame):2021 empirical survival rates for vehicles by country.
        - survival_rates_2016 (pd.DataFrame): 2016 empirical survival rates for vehicles by country.
            Extracted from (Held, 2021)
        - optimum_parameters_2008 (dict): Optimal parameters from 2008 CSP analysis. Extracted from (Oguchi, 2014).
        - optimal_distribution_dict (dict): Dictionary specifying the optimal distribution per country
            (Weibull or Weibull-Gaussian).
        - config (dict): A dictionary containing configuration settings for the sensitivity analysis and plotting,
        including:
          - "plot_params": A dictionary containing settings related to plotting such as selected years, countries,
            and powertrain types.
            - simulation_stock_years_label (list): Range of years for stock simulation.
            - csp_available_years_label (int): Number of years for which CSP data is available (e.g 45 years)
            - years_selected_label (list): CSP historical data which is available and used (e.g [2021, 2016, 2008])
            - powertrain_to_plot_label (str): Powertrain type (e.g., 'BEV') to plot.
        - bound_distributions (dict): Bounds for the parameters of the CSP distributions.
        - csp_available_years (int): Number of years for which CSP data is available (e.g 45 years)

    Returns:
        None: Generates plots and updates dataframes as part of the sensitivity analysis.

    This analysis provides insights into how the historical CSPs are evolving and how they affect the stock share
    projections, enabling insights into the effect of the fleet turnover dynamics in the last 20 years
    in the whole fleet electrification.
    """
    plot_params = config[plot_params_dim]
    columns_to_plot = {}
    stock_shares_df = process_stock_shares_with_historical_csps(registrations, survival_rates_2021, survival_rates_2016,
                                                                plot_params[simulation_stock_years_label],
                                                                optimum_parameters_2008, optimal_distribution_dict,
                                                                bound_distributions, csp_available_years)
    bev_stock_shares = stock_shares_df[stock_shares_df['powertrain'] == plot_params["powertrain_to_plot"]]
    columns_to_plot = generate_columns_to_plot(columns_to_plot, plot_params["years_selected"])
    plot_all_countries(bev_stock_shares, config, columns_to_plot, None)

