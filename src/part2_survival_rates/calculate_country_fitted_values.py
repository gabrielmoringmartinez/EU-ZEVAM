# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

from src.part2_survival_rates.get_statistical_parameters import get_statistical_parameters
from src.part2_survival_rates.get_statistical_parameters_of_each_country import \
    get_statistical_parameters_of_each_country
from src.part2_survival_rates.get_function_values import get_weibull_function, get_weibull_and_normal_function
from src.part2_survival_rates.get_distribution_function_discrete_points import get_distribution_function_discrete_points

from src.load_data_and_prepare_inputs.dimension_names import country_dim


def calculate_country_fitted_values(country_name, survival_rates, pdf_parameters, weibull_results, wg_results,
                                    csp_available_years):
    """
    Helper function to calculate Weibull and Weibull-Gaussian fitted CSP values for a single country.

    Parameters:
    - country_name (str): Name of the country to calculate fitted values for.
    - survival_rates (pd.DataFrame): DataFrame with survival rates.
    - pdf_parameters (pd.DataFrame): DataFrame with distribution parameters.
    - weibull_results (pd.DataFrame): DataFrame to store Weibull CSP results.
    - wg_results (pd.DataFrame): DataFrame to store WG CSP results.
    - csp_available_years (int): Number of years (vehicle ages) for which CSP values are calculated.

    Returns:
    - tuple:
        - pd.DataFrame: Updated `weibull_results` with calculated Weibull CSP values.
        - pd.DataFrame: Updated `wg_results` with calculated WG CSP values.
    """
    survival_rates_country = survival_rates[survival_rates[country_dim] == country_name]
    gamma, beta, k, mu, sigma = get_statistical_parameters(pdf_parameters)
    gamma_country, beta_country, k_country, mu_country, sigma_country = \
        get_statistical_parameters_of_each_country(gamma, beta, k, mu, sigma, country_name)

    predicted_weibull_value = get_weibull_function(gamma_country, beta_country, csp_available_years)
    predicted_weibull_and_normal_value = get_weibull_and_normal_function(gamma_country, beta_country, k_country,
                                                                         mu_country, sigma_country, csp_available_years)
    weibull_results = get_distribution_function_discrete_points(weibull_results, survival_rates_country,
                                                                predicted_weibull_value)

    wg_results = get_distribution_function_discrete_points(wg_results, survival_rates_country,
                                                           predicted_weibull_and_normal_value)
    return weibull_results, wg_results
