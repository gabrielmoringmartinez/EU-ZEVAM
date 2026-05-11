"""Select the optimal CSP distribution type based on fit quality."""

# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

from zevampy.load_data_and_prepare_inputs.dimension_names import distribution_dim
from zevampy.part2_survival_rates.get_distribution_type import get_distribution_type


def select_optimal_type_of_distribution(optimal_parameters):
    """
    Determine the optimal distribution type for each survival group.

    The function compares Weibull and Weibull-Gaussian model fits using their R-squared values and assigns the preferred
    distribution type.

    Parameters:
        optimal_parameters (pandas.DataFrame):
            DataFrame containing fitted distribution parameters and R-squared values.

    Returns:
        pandas.DataFrame:
            DataFrame with an additional column indicating the selected optimal distribution type.
    """
    optimal_parameters[distribution_dim] = optimal_parameters.apply(get_distribution_type, axis=1)
    return optimal_parameters
