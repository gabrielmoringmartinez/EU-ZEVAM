"""Update CSP distribution assignments for country-specific sensitivity analyses."""

# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

from zevampy.load_data_and_prepare_inputs.dimension_names import weibull_label, weibull_gaussian_label


def update_optimal_distribution_based_on_country_csp(country, opt_dist):
    """
    Update CSP distribution assignments for a selected country.

    This function assigns all countries to the same cumulative survival probability (CSP) distribution type as the
    selected reference country.

    Parameters:
        country (str):
            Reference country whose CSP distribution type is used.

        opt_dist (dict):
            Dictionary mapping distribution labels to country lists.

    Returns:
        dict:
            Updated dictionary containing revised CSP distribution assignments.
    """
    weibull_countries = opt_dist.get(weibull_label, [])
    wg_countries = opt_dist.get(weibull_gaussian_label, [])
    # Checking if the provided country is present in weibull_countries and wg_countries
    if country in weibull_countries:
        weibull_countries = weibull_countries + wg_countries
        wg_countries = []
    elif country in wg_countries:
        wg_countries = wg_countries + weibull_countries
        weibull_countries = []
    else:
        weibull_countries = []
        wg_countries = []
    # Combine the two lists into a single dictionary variable
    combined_countries = {
        weibull_label: weibull_countries,
        weibull_gaussian_label: wg_countries
    }
    return combined_countries
