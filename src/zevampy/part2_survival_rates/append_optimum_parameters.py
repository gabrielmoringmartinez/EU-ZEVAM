"""Store optimized Weibull and Gaussian distribution parameters."""

# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

import numpy as np


def append_optimum_parameters_weibull(result, optimum_gamma_per_country, optimum_beta_per_country,
                                      max_rsquared_per_country):
    """
    Append optimized Weibull parameters for a country.

    The function extracts the optimized Weibull parameters from the differential-evolution optimization result and
     appends them to the corresponding parameter lists.

    Parameters:
        result (scipy.optimize.OptimizeResult):
            Optimization result containing Weibull parameters.

        optimum_gamma_per_country (list):
            List storing optimized Weibull gamma parameters.

        optimum_beta_per_country (list):
            List storing optimized Weibull beta parameters.

        max_rsquared_per_country (list):
            List storing maximum R-squared values.

    Returns:
        tuple:
            Updated lists containing Weibull gamma parameters, Weibull beta parameters, and R-squared values.
    """
    optimum_gamma_per_country.append(result.x[0])
    optimum_beta_per_country.append(result.x[1])
    max_rsquared_per_country.append(1 - result.fun)
    return optimum_gamma_per_country, optimum_beta_per_country, max_rsquared_per_country


def append_optimum_parameters_gaussian(result, optimum_k_per_country, optimum_mu_per_country, optimum_sigma_per_country,
                                       optimum_delta_per_country, max_rsquared_per_country_weibull_gaussian):
    """
    Append optimal Gaussian parameters from the result of the differential evolution algorithm.

    Parameters:
        result (OptimizeResult): Optimization result containing Gaussian parameters [k, mu, sigma].
        Lists to store Gaussian parameters (k, mu, sigma, delta, r-squared) per country.

    Returns:
        tuple: Updated lists of Gaussian parameters (k, mu, sigma, delta, r-squared) per country.
    """
    optimum_k_per_country.append(result.x[0])
    optimum_mu_per_country.append(result.x[1])
    optimum_sigma_per_country.append(result.x[2])
    max_rsquared_per_country_weibull_gaussian.append(1 - result.fun)
    delta = result.x[0] / (np.sqrt(2 * np.pi) * result.x[2])
    optimum_delta_per_country.append(delta)
    return optimum_k_per_country, optimum_mu_per_country, optimum_sigma_per_country, optimum_delta_per_country, \
        max_rsquared_per_country_weibull_gaussian
