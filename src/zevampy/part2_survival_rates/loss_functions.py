"""Define loss functions for Weibull CSP fitting."""

# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

import numpy as np
from scipy.special import gamma


def loss_function_weibull(x: list, *args) -> float:
    """
    Calculate the normalized mean squared error for a Weibull fit.

    The function compares Weibull-predicted survival rates with observed survival-rate data.

    Parameters:
        x (list):
            Weibull distribution parameters:
            - x[0]: gamma (scale parameter)
            - x[1]: beta (shape parameter)

        *args:
            args[0] (numpy.ndarray):
                Observed survival-rate data.

    Returns:
        float:
            Normalized mean squared error (NMSE) between the Weibull model and observed data.
    """
    actual = np.asarray(args[0], dtype=float)
    csp_years = len(actual)
    year = np.linspace(1, csp_years, csp_years)
    predict = np.exp(
        -(year / x[0]) ** x[1] *
        (gamma(1 + 1 / x[1])) ** x[1]
    )
    denominator = np.sum((actual - np.average(actual)) ** 2)
    if denominator == 0:
        return np.inf
    return np.sum((predict - actual) ** 2) / denominator

"""
Define loss functions for Weibull-Gaussian CSP fitting.
"""


def loss_function_weibull_and_normal(x: list, *args) -> float:
    """
    Calculate the normalized mean squared error for a Weibull-Gaussian fit.

    The function compares combined Weibull-Gaussian predicted survival rates with observed survival-rate data.

    Parameters:
        x (list):
            Gaussian distribution parameters:
            - x[0]: k (scaling parameter)
            - x[1]: mu (mean parameter)
            - x[2]: sigma (standard deviation parameter)

        *args:
            args[0] (float):
                Weibull gamma parameter.

            args[1] (float):
                Weibull beta parameter.

            args[2] (numpy.ndarray):
                Observed survival-rate data.

    Returns:
        float:
            Normalized mean squared error (NMSE) between the Weibull-Gaussian model and observed data.
    """
    gamma_country = float(args[0])
    beta_country = float(args[1])
    actual = np.asarray(args[2], dtype=float)
    csp_years = len(actual)
    year = np.linspace(1, csp_years, csp_years)
    weibull = np.exp(
        -(year / gamma_country) ** beta_country *
        (gamma(1 + 1 / beta_country)) ** beta_country
    )
    delta = x[0] / (np.sqrt(np.pi * 2) * x[2])
    normal = delta * np.exp(-0.5 * ((year - x[1]) / x[2]) ** 2)
    predict = weibull + normal
    denominator = np.sum((actual - np.average(actual)) ** 2)
    if denominator == 0:
        return np.inf
    return np.sum((predict - actual) ** 2) / denominator
