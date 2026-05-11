"""Create DataFrames containing optimized CSP distribution parameters (Weibull)."""

# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

import pandas as pd

from zevampy.load_data_and_prepare_inputs.dimension_names import *


def save_optimum_parameters_weibull(optimum_gamma_per_country, optimum_beta_per_country, max_rsquared_per_country,
                                    country_names):
    """
    Create a DataFrame with optimized Weibull parameters.

    Parameters:
        optimum_gamma_per_country (list):
            Optimized Weibull gamma parameters.

        optimum_beta_per_country (list):
            Optimized Weibull beta parameters.

        max_rsquared_per_country (list):
            R-squared values for the Weibull fit.

        country_names (list):
            Country labels corresponding to the parameter values.

    Returns:
        pandas.DataFrame:
            DataFrame containing country labels, Weibull parameters, and R-squared values.
    """
    optimum_parameters_diff_evol_algorithm = pd.DataFrame()
    optimum_parameters_diff_evol_algorithm[country_dim] = country_names
    optimum_parameters_diff_evol_algorithm[gamma_weibull_dim] = optimum_gamma_per_country
    optimum_parameters_diff_evol_algorithm[beta_weibull_dim] = optimum_beta_per_country
    optimum_parameters_diff_evol_algorithm[r_squared_weibull_dim] = max_rsquared_per_country
    return optimum_parameters_diff_evol_algorithm


"""Create DataFrames containing optimized CSP distribution parameters (Weibull-Gaussian)."""


def save_optimum_parameters_gaussian(optimum_parameters_diff_evol_algorithm, parameters):
    """
    Add optimized Weibull-Gaussian parameters to a parameter DataFrame.

    Parameters:
        optimum_parameters_diff_evol_algorithm (pandas.DataFrame):
            DataFrame containing optimized Weibull parameters.

        parameters (list):
            List containing optimized Weibull-Gaussian parameters and R-squared values.

    Returns:
        pandas.DataFrame:
            Updated DataFrame containing Weibull and Weibull-Gaussian parameters.
    """
    optimum_parameters_diff_evol_algorithm[k_weibull_gaussian_dim] = parameters[0]
    optimum_parameters_diff_evol_algorithm[mu_weibull_gaussian_dim] = parameters[1]
    optimum_parameters_diff_evol_algorithm[sigma_weibull_gaussian_dim] = parameters[2]
    optimum_parameters_diff_evol_algorithm[delta_weibull_gaussian_dim] = parameters[3]
    optimum_parameters_diff_evol_algorithm[r_squared_weibull_gaussian_dim] = parameters[4]
    return optimum_parameters_diff_evol_algorithm
