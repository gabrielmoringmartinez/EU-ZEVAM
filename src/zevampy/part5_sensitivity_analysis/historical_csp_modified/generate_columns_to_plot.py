# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

def generate_columns_to_plot(columns_to_plot, years_selected):
    """
    Updates and returns a dictionary mapping column names to their display labels for plot legends.
    Parameters:
        - columns_to_plot (dict): A dictionary where keys are column names and values are  the corresponding labels for
         the plot legend.
        - years_selected (list):  List of years for which empirical CSP data is used and substituted in all countries
        to observe the effect.
    Returns:
        - dict: Updated `columns_to_plot` dictionary where new entries are added with keys in the form `share_<year>`
            and values as "Share with CSP from <year>".
    """
    for year in years_selected:
        column_name = f"share_{year}"
        columns_to_plot[column_name] = f"Share with CSP from {year}"
    return columns_to_plot


