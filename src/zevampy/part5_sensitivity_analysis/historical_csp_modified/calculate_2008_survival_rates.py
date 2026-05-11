"""Sensitivity analysis using historical 2008 CSP distributions."""

# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

import pandas as pd
from zevampy.part2_survival_rates.get_fitted_csp_values import get_fitted_csp_values
from zevampy.part3_stock_calculation.calculate_stock.calculate_stock import calculate_stock
from zevampy.part3_stock_calculation.calculate_stock.input_data import historical_csp

from zevampy.load_data_and_prepare_inputs.dimension_names import *


def calculate_2008_survival_rates(optimum_parameters_2008, survival_rates_2021, optimal_distribution_dict,
                                  registrations, csp_available_years, simulation_stock_years, countries_selected,
                                  output_path):
    """
    Calculate stock shares using CSP parameters derived from 2008 data.

    This function computes fitted cumulative survival probability (CSP) curves based on historical 2008 parameters
    and uses them to estimate stock shares.

    Parameters:
        optimum_parameters_2008 (pandas.DataFrame):
            Optimized CSP parameters derived from 2008 data.

        survival_rates_2021 (pandas.DataFrame):
            Empirical 2021 survival-rate data.

        optimal_distribution_dict (dict):
            Mapping between countries and CSP distributions.

        registrations (pandas.DataFrame):
            Vehicle registration data.

        csp_available_years (int):
            Number of available CSP years.

        simulation_stock_years (list[int]):
            Simulation year range for stock calculations.

        countries_selected (list[str]):
            Countries included in the stock simulation.

        output_path (str):
            Directory where outputs are saved.

    Returns:
        pandas.DataFrame:
            Stock-share estimates using historical 2008 CSP parameters.
    """
    country_names = optimum_parameters_2008[country_dim].unique()
    filtered_survival_rates_2021 = survival_rates_2021[survival_rates_2021[country_dim].isin(country_names)]
    if filtered_survival_rates_2021.empty:
        return pd.DataFrame()
    survival_grouping = [country_dim]
    fitted_csp_values_2008 = get_fitted_csp_values(filtered_survival_rates_2021, optimum_parameters_2008,
                                                   csp_available_years, output_path, survival_grouping, False)
    optimal_distribution_dict_2008 = prepare_optimal_distribution_dict(optimal_distribution_dict)
    stock_shares_are_valid = True
    stock_values_2008, stock_shares_2008 = calculate_stock(registrations, fitted_csp_values_2008,
                                                           simulation_stock_years, historical_csp, countries_selected,
                                                           stock_shares_are_valid, output_path, survival_grouping)
    stock_shares_2008[country_dim] = stock_shares_2008[country_dim].replace(eu_27_plus_norway_label, eu_9_label)
    return stock_shares_2008


def prepare_optimal_distribution_dict(distribution_dict):
    """
    Convert all CSP distributions to Weibull distributions.

    This function merges Weibull-Gaussian country assignments into the Weibull distribution group for historical 2008
    CSP analyses.

    Parameters:
        distribution_dict (dict):
            Dictionary mapping distribution labels to country lists.

    Returns:
        dict:
            Updated dictionary containing only Weibull distribution assignments.
    """
    updated_dict = distribution_dict.copy()

    weibull_countries = updated_dict.get(weibull_label, [])
    wg_countries = updated_dict.get(weibull_gaussian_label, [])

    updated_dict[weibull_label] = weibull_countries + wg_countries # Add all elements from WG to Weibull
    updated_dict[weibull_gaussian_label] = [] # Clear WG list
    return updated_dict
