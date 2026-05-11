"""Process stock shares using historical CSP sensitivity scenarios."""

# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

from zevampy.part3_stock_calculation.calculate_stock.compute_csp_values_and_compute_stock import \
    compute_csp_values_and_compute_stock
from zevampy.part5_sensitivity_analysis.historical_csp_modified.calculate_2008_survival_rates import \
    calculate_2008_survival_rates
from zevampy.part5_sensitivity_analysis.merge_stock_shares import merge_stock_shares

from zevampy.load_data_and_prepare_inputs.dimension_names import *


def process_stock_shares_with_historical_csps(registrations, survival_rates_2021, survival_rates_2016, stock_years,
                                              optimum_parameters_2008, optimal_distribution_dict, bound_distributions,
                                              csp_available_years, simulation_years, countries_selected, output_path):
    """
    Compute stock shares using historical CSP datasets.

    This function calculates stock shares based on historical cumulative survival probability (CSP) curves from multiple
    reference years and merges the results into a single dataset.

    Parameters:
        registrations (pandas.DataFrame):
            Vehicle registration data.

        survival_rates_2021 (pandas.DataFrame):
            Empirical survival-rate data for 2021.

        survival_rates_2016 (pandas.DataFrame):
            Empirical survival-rate data for 2016.

        stock_years (list[int]):
            Simulation year range for stock calculations.

        optimum_parameters_2008 (pandas.DataFrame):
            Optimized CSP parameters derived from 2008 data.

        optimal_distribution_dict (dict):
            Mapping between countries and selected CSP distributions.

        bound_distributions (dict):
            Parameter bounds used for CSP fitting.

        csp_available_years (int):
            Number of CSP years used in the calculations.

        simulation_years (list[int]):
            Simulation year range for stock calculations.

        countries_selected (list[str]):
            Countries included in the simulation.

        output_path (str):
            Directory where outputs are saved.

    Returns:
        pandas.DataFrame:
            Combined stock-share dataset for historical CSP sensitivity analyses.
    """
    # Compute stock shares for different years
    stock_values_2021, stock_shares_2021, *_ = compute_csp_values_and_compute_stock(survival_rates_2021, registrations,
                                                                                    stock_years, bound_distributions,
                                                                                    historical_csp_label,
                                                                                    csp_available_years,
                                                                                    countries_selected, [country_dim],
                                                                                    output_path)
    survival_rates_2016 = survival_rates_2016[survival_rates_2016[age_dim] <= csp_available_years].copy()
    stock_values_2016, stock_shares_2016, *_ = compute_csp_values_and_compute_stock(survival_rates_2016, registrations,
                                                                                    stock_years, bound_distributions,
                                                                                    historical_csp_label,
                                                                                    csp_available_years,
                                                                                    countries_selected, [country_dim],
                                                                                    output_path)
    stock_shares_2008 = calculate_2008_survival_rates(optimum_parameters_2008, survival_rates_2021,
                                                      optimal_distribution_dict, registrations, csp_available_years,
                                                      simulation_years, countries_selected, output_path)

    # Rename columns to match the year-specific share columns
    stock_shares_2021.rename(columns={share_dim: f'{share_dim}_{2021}'}, inplace=True)
    stock_shares_2016.rename(columns={share_dim: f'{share_dim}_{2016}'}, inplace=True)
    if not stock_shares_2008.empty:
        stock_shares_2008.rename(columns={share_dim: f"{share_dim}_{2008}"}, inplace=True)
    # Merge all stock shares into one DataFrame
    stock_share_frames = [
        stock_shares_2021,
        stock_shares_2016,
    ]
    if stock_shares_2008 is not None and not stock_shares_2008.empty:
        stock_share_frames.append(stock_shares_2008)

    stock_shares_df = None

    for stock_shares in stock_share_frames:
        stock_shares_df = merge_stock_shares(stock_shares_df, stock_shares)
    return stock_shares_df
