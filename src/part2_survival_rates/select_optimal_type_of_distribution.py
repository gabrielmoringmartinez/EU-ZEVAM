# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

from src.load_data_and_prepare_inputs.dimension_names import distribution_dim
from src.part2_survival_rates.get_distribution_type import get_distribution_type


def select_optimal_type_of_distribution(optimal_parameters):
    """
     Adds a column indicating the optimal distribution type for each row based on
     the R-squared values of different distribution models (Weibull or Weibull-Gaussian).

     Parameters:
         optimal_parameters (pd.DataFrame): DataFrame containing R-squared values and parameters
                                            for each distribution (e.g., Weibull, Weibull-Gaussian).
         dist_column (str): The name of the new column to add, which will store the optimal
                            distribution type for each row.

     Returns:
         pd.DataFrame: The input DataFrame with an added column specifying the optimal distribution type.
     """
    optimal_parameters[distribution_dim] = optimal_parameters.apply(get_distribution_type, axis=1)
    return optimal_parameters
