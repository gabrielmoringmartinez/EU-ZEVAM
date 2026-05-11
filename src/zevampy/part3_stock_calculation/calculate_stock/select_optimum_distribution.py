"""Select stock values based on the optimal CSP distribution."""

# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

from zevampy.load_data_and_prepare_inputs.dimension_names import *


def select_optimum_distribution(row):
    """
    Select the stock value corresponding to the optimal distribution.

    This function returns the stock value calculated from either the Weibull or Weibull-Gaussian distribution,
    depending on the selected distribution type.

    Parameters:
        row (pandas.Series):
            Row containing stock values and distribution labels.

    Returns:
        float:
            Selected stock value corresponding to the optimal distribution.

    Raises:
        ValueError:
            If the distribution type is unknown.
    """
    if row[distribution_dim] == weibull_label:
        return row[stock_weibull_dim]

    if row[distribution_dim] == weibull_gaussian_label:
        return row[stock_wg_dim]

    raise ValueError(
        f"Unknown distribution type: {row[distribution_dim]}"
    )
