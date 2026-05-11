"""Determine subplot grid dimensions for CSP plots."""

# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

import math
import numpy as np

from zevampy.load_data_and_prepare_inputs.dimension_names import num_rows_dim, num_columns_dim


def get_number_rows_and_columns(number_of_countries, plot_params):
    """
    Determine subplot grid dimensions for country plots.

    This function calculates the number of rows and columns used for subplot layouts. If no layout is explicitly defined
    in the plot configuration, a square-like grid is generated automatically.

    Parameters:
        number_of_countries (int):
            Total number of countries or groups to plot.

        plot_params (dict):
            Dictionary containing subplot layout settings.

    Returns:
        tuple[int, int]:
            Number of subplot rows and columns.
    """
    default_num_rows = None
    default_num_columns = None
    country_rows = plot_params.get(num_rows_dim, default_num_rows)  # Replace default_num_rows with a sensible default, e.g., 1
    country_columns = plot_params.get(num_columns_dim, default_num_columns)  # Replace default_num_columns with a sensible default, e.g., 1
    if country_rows is None and country_columns is None:
        country_rows = math.ceil(np.sqrt(number_of_countries))  # Rows and columns are defined
        country_columns = country_rows
    return country_rows, country_columns
