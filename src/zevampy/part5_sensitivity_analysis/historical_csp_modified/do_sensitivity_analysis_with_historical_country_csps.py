"""Sensitivity analysis using historical country-specific CSP curves."""

# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

from zevampy.part5_sensitivity_analysis.historical_csp_modified.process_historical_csp import \
    process_stock_shares_with_historical_csps
from zevampy.part5_sensitivity_analysis.historical_csp_modified.generate_columns_to_plot import generate_columns_to_plot
from zevampy.part2_survival_rates.plot_survival_rates.plot_all_countries import plot_all_countries

from zevampy.load_data_and_prepare_inputs.dimension_names import *


def do_sensitivity_analysis_with_historical_country_csps(registrations, survival_rates_2021, survival_rates_2016,
                                                         optimum_parameters_2008, optimal_distribution_dict, config,
                                                         bound_distributions, csp_available_years, simulation_years,
                                                         countries_selected, output_path):
    """
    Perform sensitivity analysis with historical CSP curves.

    This function compares stock-share projections based on
    historical CSP datasets from different reference years and
    generates validation plots for the selected powertrain.

    Parameters:
        registrations (pandas.DataFrame):
            Vehicle registration data.

        survival_rates_2021 (pandas.DataFrame):
            Empirical survival-rate data for 2021.

        survival_rates_2016 (pandas.DataFrame):
            Empirical survival-rate data for 2016.

        optimum_parameters_2008 (pandas.DataFrame):
            Optimized CSP parameters derived from 2008 data.

        optimal_distribution_dict (dict):
            Mapping between countries and selected CSP distributions.

        config (dict):
            Configuration settings for plotting and sensitivity analysis.

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
        None
    """
    plot_params = config[plot_params_dim]
    columns_to_plot = {}
    stock_shares_df = process_stock_shares_with_historical_csps(registrations, survival_rates_2021, survival_rates_2016,
                                                                plot_params[simulation_stock_years_label],
                                                                optimum_parameters_2008, optimal_distribution_dict,
                                                                bound_distributions, csp_available_years,
                                                                simulation_years, countries_selected, output_path)
    bev_stock_shares = stock_shares_df[stock_shares_df[powertrain_dim] == plot_params[powertrain_to_plot_label]]
    available_years = [
        year for year in plot_params[years_selected_label]
        if f"{share_dim}_{year}" in bev_stock_shares.columns
    ]
    plot_params[years_selected_label] = available_years
    columns_to_plot = generate_columns_to_plot(columns_to_plot, plot_params[years_selected_label])
    plot_all_countries(bev_stock_shares, config, columns_to_plot, None)

