# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

import numpy as np
import math

from src.part3_stock_calculation.calculate_stock.input_data import csp_available_years


def loss_function_weibull(x : list, *args) -> float:
    """
    Calculates the error (loss) between the predicted survival rates from a Weibull distribution
    and the actual survival rate data. The error is computed using normalized mean squared error (NMSE),
    which indicates how well the Weibull model fits the observed data.

    Parameters:
        x (list): Parameters for the Weibull distribution.
            - x[0] (float): gamma (scale parameter) – defines the scale parameter of the weibull or the
                            weibull average lifespan.
            - x[1] (float): beta (shape parameter) – defines the shape of the Weibull curve.
        actual_data (np.ndarray): Array of observed survival rates, representing the actual data
                                  the Weibull model is trying to fit.

    Returns:
        float: Normalized mean squared error (NMSE), where lower values indicate a better fit
               between the Weibull model and the actual data.
    """
    year = np.linspace(1, csp_available_years, csp_available_years)
    predict = np.exp(-(year/x[0])**x[1]*(math.gamma(1+1/x[1]))**x[1])
    actual = args
    return sum((predict-actual)**2)/sum((actual-np.average(actual))**2)


def loss_function_weibull_and_normal(x: list, *args) -> float:
    """
    Calculates the error (loss) between the predicted survival rates from a combined
    Weibull-Gaussian model and the actual survival rate data. The error is computed using
    normalized mean squared error (NMSE), showing how well this composite model fits
    the observed data.

    Parameters:
        x (list): Parameters for the Gaussian (normal) component.
            - x[0] (float): k – scales the Gaussian component.
            - x[1] (float): mu – mean of the Gaussian distribution (controls the location).
            - x[2] (float): sigma – standard deviation of the Gaussian (controls the spread).
        gamma (float): Gamma (scale parameter) for the Weibull distribution.
        beta (float): Beta (shape parameter) for the Weibull distribution.
        actual_data (np.ndarray): Array of observed survival rates, representing the actual data
                                  the Weibull-Gaussian model is trying to fit.

    Returns:
        float: Normalized mean squared error (NMSE), where lower values indicate a better fit
               between the Weibull-Gaussian model and the actual data.
    """
    gamma_country = args[0]
    beta_country = args[1]
    year = np.linspace(1, csp_available_years, csp_available_years)
    weibull = np.exp(-(year/gamma_country)**beta_country*(math.gamma(1+1/beta_country))**beta_country)
    delta = x[0]/(np.sqrt(np.pi*2)*x[2])
    normal = delta*np.exp(-0.5*((year-x[1])/x[2])**2)
    predict = weibull + normal
    actual = args[2]
    return sum((predict-actual)**2)/sum((actual-np.average(actual))**2)
