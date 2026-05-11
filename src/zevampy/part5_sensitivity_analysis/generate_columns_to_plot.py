"""Generate plot-legend mappings for selected data columns."""

# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT


def generate_columns_to_plot(columns_to_plot, items_selected, general_legend_text):
    """
    Generate plot-column and legend-label mappings.

    This function creates entries mapping column names to corresponding legend labels for plotting.

    Parameters:
        columns_to_plot (dict):
            Dictionary storing plot-column and legend-label mappings.

        items_selected (list):
            List of selected items used to generate column names.

        general_legend_text (str):
            Base legend text appended to each selected item.

    Returns:
        dict:
            Updated dictionary containing plot-column mappings.
    """
    for item in items_selected:
        column_name = f"share_{item}"
        columns_to_plot[column_name] = f"{general_legend_text} {item}"
    return columns_to_plot
