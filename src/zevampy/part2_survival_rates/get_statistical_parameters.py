"""Extract statistical distribution parameters for CSP calculations."""

# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

from zevampy.load_data_and_prepare_inputs.dimension_names import *


def get_statistical_parameters(pdf_parameters):
    """
    Extract Weibull and Gaussian distribution parameters.

    Parameters:
        pdf_parameters (pandas.DataFrame):
            DataFrame containing fitted Weibull and
            Weibull-Gaussian distribution parameters.

    Returns:
        tuple:
            Tuple containing DataFrames for:
            - gamma Weibull parameters
            - beta Weibull parameters
            - k Gaussian parameters
            - mu Gaussian parameters
            - sigma Gaussian parameters
    """
    gamma_variable = pdf_parameters[[gamma_weibull_dim, country_dim]]
    beta_variable = pdf_parameters[[beta_weibull_dim, country_dim]]
    k_variable = pdf_parameters[[k_weibull_gaussian_dim, country_dim]]
    mu_variable = pdf_parameters[[mu_weibull_gaussian_dim, country_dim]]
    sigma_variable = pdf_parameters[[sigma_weibull_gaussian_dim, country_dim]]
    return gamma_variable, beta_variable, k_variable, mu_variable, sigma_variable



