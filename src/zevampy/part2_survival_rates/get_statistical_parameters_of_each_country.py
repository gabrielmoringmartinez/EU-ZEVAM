"""Extract country-specific statistical parameters for CSP calculations."""

# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

from zevampy.load_data_and_prepare_inputs.dimension_names import *


def get_statistical_parameters_of_each_country(gamma, beta, k, mu, sigma, country_name):
    """
    Extract distribution parameters for a specific country.

    Parameters:
        gamma (pandas.DataFrame):
            DataFrame containing Weibull gamma parameters.

        beta (pandas.DataFrame):
            DataFrame containing Weibull beta parameters.

        k (pandas.DataFrame):
            DataFrame containing Gaussian scaling parameters.

        mu (pandas.DataFrame):
            DataFrame containing Gaussian mean parameters.

        sigma (pandas.DataFrame):
            DataFrame containing Gaussian standard deviation parameters.

        country_name (str):
            Name of the country for which parameters are extracted.

    Returns:
        tuple:
            Tuple containing:
            - gamma parameter
            - beta parameter
            - k parameter
            - mu parameter
            - sigma parameter
            for the selected country.
    """
    gamma_country = gamma[gamma[country_dim] == country_name][gamma_weibull_dim]
    beta_country = beta[beta[country_dim] == country_name][beta_weibull_dim]
    k_country = k[k[country_dim] == country_name][k_weibull_gaussian_dim]
    mu_country = mu[mu[country_dim] == country_name][mu_weibull_gaussian_dim]
    sigma_country = sigma[sigma[country_dim] == country_name][sigma_weibull_gaussian_dim]
    return gamma_country, beta_country, k_country, mu_country, sigma_country
