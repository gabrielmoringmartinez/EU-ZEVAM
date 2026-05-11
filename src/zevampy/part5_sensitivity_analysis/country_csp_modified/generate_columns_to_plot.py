"""Generate legend mappings for country-specific CSP sensitivity plots."""

# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT


def generate_columns_to_plot(columns_to_plot, countries_selected, country_adjectives):
    """
    Generate plot-column mappings for country-specific CSP scenarios.

    This function creates legend labels for stock-share scenarios using country-specific cumulative survival probability
    (CSP) curves.

    Parameters:
        columns_to_plot (dict):
            Dictionary storing plot-column and legend-label mappings.

        countries_selected (list[str]):
            Countries whose CSP curves are used in the sensitivity analysis.

        country_adjectives (dict[str, str]):
            Mapping between country names and adjective forms.

    Returns:
        dict:
            Updated dictionary containing plot-column mappings for CSP sensitivity scenarios.
    """
    for country in countries_selected:
        column_name = f"share_{country}"
        columns_to_plot[column_name] = f"Share with {country_adjectives[country]} CSP"
    return columns_to_plot
