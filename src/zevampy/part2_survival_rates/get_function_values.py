"""Calculate fitted survival functions for CSP estimation."""

# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

import numpy as np
import math
import pandas as pd


def get_weibull_function(gamma_variable, beta_variable, csp_available_years):
    """
    Calculate fitted Weibull survival probability values.

    Parameters:
        gamma_variable (float or pandas.Series):
            Gamma parameter of the Weibull distribution.

        beta_variable (float or pandas.Series):
            Beta parameter of the Weibull distribution.

        csp_available_years (int):
            Number of vehicle ages for which CSP values are calculated.

    Returns:
        list[float]:
            Fitted cumulative survival probability values.
    """
    # Extract scalar values if they are single-element Series
    if isinstance(gamma_variable, pd.Series):
        gamma_variable = gamma_variable.iloc[0]
    if isinstance(beta_variable, pd.Series):
        beta_variable = beta_variable.iloc[0]
    year_a = np.linspace(1, csp_available_years, csp_available_years)
    csp = []
    for x in year_a:
        csp_value = float(np.exp(-(x / gamma_variable) ** beta_variable *
                                 (math.gamma(1 + 1 / beta_variable)) ** beta_variable))
        csp.append(csp_value)
    return csp


def get_weibull_and_normal_function(gamma_variable, beta_variable, k, mu, sigma, csp_available_years):
    """
    Calculate combined Weibull-Gaussian survival probability values.

    This function combines a Weibull survival function with a Gaussian
    component to estimate cumulative survival probabilities (CSPs) for
    vehicle fleets.

    Parameters:
        gamma_variable (float or pandas.Series):
            Gamma parameter of the Weibull distribution.

        beta_variable (float or pandas.Series):
            Beta parameter of the Weibull distribution.

        k (float or pandas.Series):
            Scaling parameter of the Gaussian distribution.

        mu (float or pandas.Series):
            Mean value of the Gaussian distribution.

        sigma (float or pandas.Series):
            Standard deviation of the Gaussian distribution.

        csp_available_years (int):
            Number of vehicle ages for which CSP values are calculated.

    Returns:
        list[float]:
            Fitted cumulative survival probability values from the
            combined Weibull-Gaussian distribution.
    """
    if isinstance(gamma_variable, pd.Series):
        gamma_variable = gamma_variable.iloc[0]
    if isinstance(beta_variable, pd.Series):
        beta_variable = beta_variable.iloc[0]
    if isinstance(k, pd.Series):
        k = k.iloc[0]
    if isinstance(mu, pd.Series):
        mu = mu.iloc[0]
    if isinstance(sigma, pd.Series):
        sigma = sigma.iloc[0]
    year_a = np.linspace(1, csp_available_years, csp_available_years)
    csp = []
    for x in year_a:
        weibull = np.exp(-(x / gamma_variable) ** beta_variable * (math.gamma(1 + 1 / beta_variable)) ** beta_variable)
        delta = k / (np.sqrt(np.pi * 2) * sigma)
        normal = delta * np.exp(-0.5 * ((x - mu) / sigma) ** 2)
        csp_value = weibull + normal
        csp.append(csp_value)
    return csp
