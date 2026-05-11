"""Modify CSP distribution parameters for sensitivity analyses."""

# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

from zevampy.load_data_and_prepare_inputs.dimension_names import *


def modify_csps(optimum_parameters, percentage):
    """
    Adjust CSP parameters by a relative percentage.

    This function modifies Weibull and Weibull-Gaussian CSP parameters for sensitivity-analysis scenarios.

    Parameters:
        optimum_parameters (pandas.DataFrame):
            Optimized CSP parameter dataset.

        percentage (float):
            Relative adjustment applied to the CSP parameters.

    Returns:
        pandas.DataFrame:
            Adjusted CSP parameter dataset.
    """
    adjusted_parameters = optimum_parameters.copy()
    percentage_value = 1 + percentage
    adjusted_parameters[gamma_weibull_dim] *= percentage_value
    adjusted_parameters[mu_weibull_gaussian_dim] *= percentage_value
    return adjusted_parameters
