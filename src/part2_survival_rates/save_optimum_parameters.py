# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

import pandas as pd

from src.load_data_and_prepare_inputs.dimension_names import *


def save_optimum_parameters_weibull(optimum_gamma_per_country, optimum_beta_per_country, max_rsquared_per_country,
                                    country_names):
    """
    Compiles the optimized Weibull distribution parameters for each country into a DataFrame.

    Parameters:
        optimum_gamma_per_country (list): List of optimized gamma parameters for each country.
        optimum_beta_per_country (list): List of optimized beta parameters for each country.
        max_rsquared_per_country (list): List of maximum R-squared values for each country (model goodness-of-fit).
        country_names (list): List of country labels corresponding to the parameter lists.

    Returns:
        pd.DataFrame: A DataFrame containing the following columns:
            - 'geo country' (or the name specified by `country_dim`): Country labels.
            - 'gamma (Weibull)' (or the name specified by `gamma_weibull_dim`): Optimized gamma parameters.
            - 'beta (Weibull)' (or the name specified by `beta_weibull_dim`): Optimized beta parameters.
            - 'R-squared (Weibull)' (or the name specified by `r_squared_weibull_dim`): R-squared values.
    """
    optimum_parameters_diff_evol_algorithm = pd.DataFrame()
    optimum_parameters_diff_evol_algorithm[country_dim] = country_names
    optimum_parameters_diff_evol_algorithm[gamma_weibull_dim] = optimum_gamma_per_country
    optimum_parameters_diff_evol_algorithm[beta_weibull_dim] = optimum_beta_per_country
    optimum_parameters_diff_evol_algorithm[r_squared_weibull_dim] = max_rsquared_per_country
    return optimum_parameters_diff_evol_algorithm


def save_optimum_parameters_gaussian(optimum_parameters_diff_evol_algorithm, parameters):
    """
    Compiles the optimized Weibull-Gaussian distribution parameters to an existing DataFrame.

    Parameters:
        optimum_parameters_diff_evol_algorithm (pd.DataFrame): A DataFrame containing the optimized Weibull parameters
            (gamma, beta, and R-squared) for each country.
        parameters (list): A list of Gaussian parameters for each country, structured as:
            - parameters[0] (list): Optimized k parameters.
            - parameters[1] (list): Optimized mu parameters.
            - parameters[2] (list): Optimized sigma parameters.
            - parameters[3] (list): Optimized delta parameters.
            - parameters[4] (list): R-squared values for the Weibull-Gaussian fit.

    Returns:
        pd.DataFrame: An updated DataFrame that includes the following additional columns:
            - 'k (WG)' (or the name specified by `k_weibull_gaussian_dim`): Optimized k parameters.
            - 'mu (WG)' (or the name specified by `mu_weibull_gaussian_dim`): Optimized mu parameters.
            - 'sigma (WG)' (or the name specified by `sigma_weibull_gaussian_dim`): Optimized sigma parameters.
            - 'delta (WG)' (or the name specified by `delta_weibull_gaussian_dim`): Optimized delta parameters.
            - 'R-squared (WG)' (or the name specified by `r_squared_weibull_gaussian_dim`): R-squared values for the
                Weibull-Gaussian fit.
        """
    optimum_parameters_diff_evol_algorithm[k_weibull_gaussian_dim] = parameters[0]
    optimum_parameters_diff_evol_algorithm[mu_weibull_gaussian_dim] = parameters[1]
    optimum_parameters_diff_evol_algorithm[sigma_weibull_gaussian_dim] = parameters[2]
    optimum_parameters_diff_evol_algorithm[delta_weibull_gaussian_dim] = parameters[3]
    optimum_parameters_diff_evol_algorithm[r_squared_weibull_gaussian_dim] = parameters[4]
    return optimum_parameters_diff_evol_algorithm
