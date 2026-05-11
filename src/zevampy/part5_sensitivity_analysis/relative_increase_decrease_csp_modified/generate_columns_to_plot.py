"""Generate legend mappings for CSP increase and reduction scenarios."""

# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT


def generate_columns_to_plot(columns_to_plot, increase_selected):
    """
    Generate plot-column mappings for CSP adjustment scenarios.

    This function creates legend labels for stock-share
    sensitivity analyses using increased or decreased cumulative
    survival probability (CSP) values.

    Parameters:
        columns_to_plot (dict):
            Dictionary storing plot-column and legend-label
            mappings.

        increase_selected (list[float]):
            Relative CSP adjustments applied during the
            sensitivity analysis.

    Returns:
        dict:
            Updated dictionary containing plot-column mappings
            for CSP adjustment scenarios.
    """
    for increase in increase_selected:
        increase_in_percentage = int(increase * 100)
        column_name = f"share_{increase}"
        if increase < 0:
            columns_to_plot[column_name] = f"Share with a {increase_in_percentage}% reduction"
        elif increase > 0:
            columns_to_plot[column_name] = f"Share with a {increase_in_percentage}% increase"
        elif increase == 0:
            columns_to_plot[column_name] = "Share with empirical CSP"

    return columns_to_plot


