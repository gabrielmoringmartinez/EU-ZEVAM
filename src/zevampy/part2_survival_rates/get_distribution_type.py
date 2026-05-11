"""Select the preferred CSP distribution model based on R-squared values."""

# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

from zevampy.load_data_and_prepare_inputs.dimension_names import r_squared_weibull_dim, r_squared_weibull_gaussian_dim, \
    weibull_label, weibull_gaussian_label


def get_distribution_type(row):
    """
    Determine the preferred CSP distribution model for a dataset row.

    The function compares the R-squared values of the Weibull and Weibull-Gaussian models and selects the preferred
    distribution type. The Weibull model is preferred when its R-squared value is within 0.025 of the
    Weibull-Gaussian model.

    Parameters:
        row (pandas.Series):
            Row containing the R-squared values of the Weibull and
            Weibull-Gaussian models.

    Returns:
        str:
            Selected distribution type label (`"Weibull"` or `"WG"`).
    """
    if row[r_squared_weibull_dim] + 0.025 > row[r_squared_weibull_gaussian_dim]:
        return weibull_label
    else:
        return weibull_gaussian_label
