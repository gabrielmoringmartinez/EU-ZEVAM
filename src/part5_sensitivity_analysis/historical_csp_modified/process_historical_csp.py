# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

from src.part3_stock_calculation.calculate_stock.compute_csp_values_and_compute_stock import \
    compute_csp_values_and_compute_stock
from src.part5_sensitivity_analysis.historical_csp_modified.calculate_2008_survival_rates import \
    calculate_2008_survival_rates
from src.part5_sensitivity_analysis.merge_stock_shares import merge_stock_shares

from src.load_data_and_prepare_inputs.dimension_names import *


def process_stock_shares_with_historical_csps(registrations, survival_rates_2021, survival_rates_2016, stock_years,
                                              optimum_parameters_2008, optimal_distribution_dict, bound_distributions,
                                              csp_available_years, simulation_years):
    """
    Compute stock shares using different empirical survival rates (2008, 2016, 2021) and merge them into a
    single DataFrame for further analysis and plotting.

    Parameters:
        - registrations (pd.DataFrame): Registration data by year, powertrain, and country.
        - survival_rates_2021 (pd.DataFrame): Empirical survival rates for vehicles by country for the year 2021.
        - survival_rates_2016 (pd.DataFrame): Empirical survival rates for vehicles by country for the year 2016.
            Extracted from (Held, 2021).
        - stock_years (list of int): Range of years for stock modelling (e.g., [2014, 2050]).
        - optimum_parameters_2008 (dict): Optimal parameters from the 2008 CSP analysis. Extracted from (Oguchi, 2014).
        - optimal_distribution_dict (dict): Dictionary specifying the optimal distribution (Weibull or Weibull-Gaussian)
          for each country.
        - bound_distributions (dict): Bounds for the parameters of the CSP distributions used in the analysis.
        - csp_available_years (int): Number of years for which country-specific CSP data is available
        (e.g., [45] years).

    Returns:
        pd.DataFrame: Merged DataFrame containing stock shares using CSP data from 2008, 2016, and 2021,
        ready for plotting or further analysis.

    Notes:
        - The function computes the stock shares using empirical survival rates from three historical years
        (2008, 2016, 2021). 2021 is the reference year used for the analysis.
        - The stock shares are renamed according to the year (e.g., `share_2021`, `share_2016`, `share_2008`).
        - The stock shares DataFrames for the different years are then merged into a single DataFrame for further
        analysis.
    """
    # Compute stock shares for different years
    stock_values_2021, stock_shares_2021, *_ = compute_csp_values_and_compute_stock(survival_rates_2021, registrations,
                                                                                    stock_years, bound_distributions,
                                                                                    historical_csp_label,
                                                                                    csp_available_years)
    stock_values_2016, stock_shares_2016, *_ = compute_csp_values_and_compute_stock(survival_rates_2016, registrations,
                                                                                    stock_years, bound_distributions,
                                                                                    historical_csp_label,
                                                                                    csp_available_years)
    stock_shares_2008 = calculate_2008_survival_rates(optimum_parameters_2008, survival_rates_2021,
                                                      optimal_distribution_dict, registrations, csp_available_years,
                                                      simulation_years)

    # Rename columns to match the year-specific share columns
    stock_shares_2021.rename(columns={share_dim: f'{share_dim}_{2021}'}, inplace=True)
    stock_shares_2016.rename(columns={share_dim: f'{share_dim}_{2016}'}, inplace=True)
    stock_shares_2008.rename(columns={share_dim: f'{share_dim}_{2008}'}, inplace=True)

    # Merge all stock shares into one DataFrame
    stock_shares_df = None
    for stock_shares in [stock_shares_2021, stock_shares_2016, stock_shares_2008]:
        stock_shares_df = merge_stock_shares(stock_shares_df, stock_shares)

    return stock_shares_df
