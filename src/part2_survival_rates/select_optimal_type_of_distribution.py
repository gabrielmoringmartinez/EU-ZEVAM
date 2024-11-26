from src.load_data_and_prepare_inputs.dimension_names import *


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
        return weibull_suffix
    else:
        return weibull_gaussian_suffix
