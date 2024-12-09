import math
import numpy as np

from src.load_data_and_prepare_inputs.dimension_names import num_rows_dim, num_columns_dim


def get_number_rows_and_columns(number_of_countries, plot_params):
    """
    Determines the optimal number of rows and columns for the plot grid based on the number of countries to be plotted.

    Parameters:
    - number_of_countries (int): The total number of countries to be plotted.
    - plot_params (dict): A dictionary containing plot configuration parameters.
                          Expected keys: 'num_rows_dim' and 'num_columns_dim' which may specify
                          the number of rows and columns respectively.

    Returns:
    - tuple: A tuple containing two integers, (num_rows, num_columns), which specify the number of rows
             and columns for the plot grid. If no specific values are provided in `plot_params`,
             the function calculates a square grid based on the square root of the number of countries.
    """
    default_num_rows = None
    default_num_columns = None
    country_rows = plot_params.get(num_rows_dim, default_num_rows)  # Replace default_num_rows with a sensible default, e.g., 1
    country_columns = plot_params.get(num_columns_dim, default_num_columns)  # Replace default_num_columns with a sensible default, e.g., 1
    if country_rows is None and country_columns is None:
        country_rows = math.ceil(np.sqrt(number_of_countries))  # Rows and columns are defined
        country_columns = country_rows
    return country_rows, country_columns
