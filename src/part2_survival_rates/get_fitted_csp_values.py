# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

import pandas as pd


from src.part2_survival_rates.calculate_country_fitted_values import calculate_country_fitted_values
from src.load_data_and_prepare_inputs.dimension_names import country_dim, age_dim, distribution_dim, weibull_label, \
    weibull_gaussian_label


def get_fitted_csp_values(survival_rates, pdf_parameters, csp_available_years, save_options=False):
    """
    Calculates fitted Cumulative Survival Probability (CSP) values for each country using Weibull and
    Weibull-Gaussian (WG) distribution parameters.

    Parameters:
    - survival_rates (pd.DataFrame): DataFrame containing survival rates by country and vehicle age.
    - pdf_parameters (pd.DataFrame): Parameters of Weibull and WG distributions for each country.
    - save_options (bool): If `True`, saves the fitted CSP values to a CSV file.
    - csp_available_years (int): Number of years (vehicle ages) for which CSP values are calculated.
    - save_options (bool, optional): Bool defining if results should be saved or not


    Returns:
    - pd.DataFrame: DataFrame containing fitted CSP values for each country by vehicle age, distribution model (Weibull
     and Weibull Gaussian), and the selected distribution type.
    """
    country_names = survival_rates[country_dim].unique()
    weibull_results = pd.DataFrame()
    wg_results = pd.DataFrame()
    for country_name in country_names:
        survival_rates_country = survival_rates[survival_rates[country_dim] == country_name]
        weibull_results, wg_results = calculate_country_fitted_values(country_name, survival_rates_country,
                                                                      pdf_parameters, weibull_results, wg_results,
                                                                      csp_available_years)
    fitted_csp_values = pd.merge(weibull_results, wg_results, on=[country_dim, age_dim],
                                 suffixes=(f' {weibull_label}', f' {weibull_gaussian_label}'), how='inner')
    fitted_csp_values = pd.merge(fitted_csp_values, pdf_parameters[[country_dim, distribution_dim]], on=country_dim)
    if save_options:
        fitted_csp_values.to_csv('outputs/2_3_fitted_CSP_curves.csv', sep=';', index=False, decimal=',')
    return fitted_csp_values

