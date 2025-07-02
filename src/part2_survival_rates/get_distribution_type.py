# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

from src.load_data_and_prepare_inputs.dimension_names import r_squared_weibull_dim, r_squared_weibull_gaussian_dim, \
    weibull_label, weibull_gaussian_label


def get_distribution_type(row):
    """
    Determines the optimal distribution type for a row based on the comparison
    between R-squared values of the Weibull and Weibull-Gaussian models.

    If the R-squared value of the Weibull model is within 0.025 of the
    Weibull-Gaussian model's R-squared value, it selects Weibull; otherwise, it selects Weibull Gaussian.

    Parameters:
        row (pd.Series): A row from the DataFrame containing 'r squared (Weibull)' and
                         'r squared (Weibull and Import-Gaussian)' columns.

    Returns:
        str: The optimal distribution type, either 'Weibull' or 'WG' (Weibull-Gaussian).
    """
    if row[r_squared_weibull_dim] + 0.025 > row[r_squared_weibull_gaussian_dim]:
        return weibull_label
    else:
        return weibull_gaussian_label
