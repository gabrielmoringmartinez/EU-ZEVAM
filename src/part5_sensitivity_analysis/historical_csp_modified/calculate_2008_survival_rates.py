# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

from src.part2_survival_rates.get_fitted_csp_values import get_fitted_csp_values
from src.part3_stock_calculation.calculate_stock.calculate_stock import calculate_stock
from src.part3_stock_calculation.calculate_stock.input_data import historical_csp

from src.load_data_and_prepare_inputs.dimension_names import *


def calculate_2008_survival_rates(optimum_parameters_2008, survival_rates_2021, optimal_distribution_dict,
                                  registrations, csp_available_years, simulation_stock_years):
    """
    Calculate the stock shares for 2008 based on the CSP optimal parameters defining the survival rates from year 2008.

    Parameters:
        - optimum_parameters_2008 (pd.DataFrame): The optimal parameters from the empirical 2008 CSP data.
        - survival_rates_2021 (pd.DataFrame): 2021 empirical survival rates for vehicles by country.
        - optimal_distribution_dict (dict): A dictionary specifying the optimal distribution per country
          (Weibull or Weibull-Gaussian).
        - registrations (pd.DataFrame): Registration data by year, powertrain, and country.
        - csp_available_years (int): Number of years for which CSP data is available (e.g., 45 years).
        - simulation_stock_years (list of int): List of years for which the stock simulation is performed,
        e.g., [2014, 2050].

    Returns:
        pd.DataFrame: Stock shares DataFrame for the year 2008

    Notes:
        - The function first filters survival rates for the countries included in the 2008 optimum parameters.
        - It then calculates the fitted CSP values for 2008 using the provided 2008 optimal parameters.
        - The optimal distribution dictionary is prepared for 2008, combining Weibull and Weibull-Gaussian
         distributions.
        - The stock shares for 2008 are computed using these fitted CSP values, and the registrations.
    """
    country_names = optimum_parameters_2008[country_dim].unique()
    filtered_survival_rates_2021 = survival_rates_2021[survival_rates_2021[country_dim].isin(country_names)]
    fitted_csp_values_2008 = get_fitted_csp_values(filtered_survival_rates_2021, optimum_parameters_2008,
                                                   csp_available_years, False)
    optimal_distribution_dict_2008 = prepare_optimal_distribution_dict(optimal_distribution_dict)
    stock_values_2008, stock_shares_2008 = calculate_stock(registrations, fitted_csp_values_2008,
                                                           optimal_distribution_dict_2008, simulation_stock_years,
                                                           historical_csp)
    stock_shares_2008[country_dim] = stock_shares_2008[country_dim].replace(eu_27_plus_norway_label, eu_9_label)
    return stock_shares_2008


def prepare_optimal_distribution_dict(distribution_dict):
    """
    Prepare the optimal distribution dictionary for 2008 by defining all countries as Weibull distributions. The model
    developed by (Oguchi, 2014) was only measuring CSPs using Weibull distributions.

    This function updates the provided distribution dictionary by appending all elements from the Weibull-Gaussian list
    into the Weibull list and then clearing the Weibull-Gaussian list. This is done to combine the two distributions
    for the 2008 analysis.

    Parameters:
        - distribution_dict (dict): Dictionary containing the distribution types for each country
        (Weibull or Weibull-Gaussian).

    Returns:
        dict: Updated dictionary where the Weibull-Gaussian list is merged into the Weibull list, and the
                Weibull-Gaussian list is cleared.

    """

    updated_dict = distribution_dict.copy()

    weibull_countries = updated_dict.get(weibull_label, [])
    wg_countries = updated_dict.get(weibull_gaussian_label, [])

    updated_dict[weibull_label] = weibull_countries + wg_countries # Add all elements from WG to Weibull
    updated_dict[weibull_gaussian_label] = [] # Clear WG list
    return updated_dict
