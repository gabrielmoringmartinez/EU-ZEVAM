"""Generate legend mappings for historical CSP sensitivity-analysis plots."""

# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT


def generate_columns_to_plot(columns_to_plot, years_selected):
    """
    Generate plot-column mappings for historical CSP scenarios.

    This function creates legend labels for stock-share
    sensitivity analyses using historical cumulative survival
    probability (CSP) curves.

    Parameters:
        columns_to_plot (dict):
            Dictionary storing plot-column and legend-label
            mappings.

        years_selected (list[int]):
            Historical CSP reference years included in the
            sensitivity analysis.

    Returns:
        dict:
            Updated dictionary containing plot-column mappings
            for historical CSP scenarios.
    """
    for year in years_selected:
        column_name = f"share_{year}"
        columns_to_plot[column_name] = f"Share with CSP from {year}"
    return columns_to_plot


