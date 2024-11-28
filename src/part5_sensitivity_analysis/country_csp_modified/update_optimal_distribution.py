from src.load_data_and_prepare_inputs.dimension_names import weibull_label, weibull_gaussian_label


def update_optimal_distribution_based_on_country_csp(country, opt_dist):
    """
    Updates the optimal distribution for a specified country by adjusting the Weibull and Weibull-Gaussian
    country lists based on whether the country appears in either list.

    Parameters:
        - country (str): The country for which the distribution update is required.
        - opt_dist (dict): A dictionary with two keys, representing countries that follow Weibull and
                           Weibull-Gaussian distributions:
                           - weibull_label: List of countries using the Weibull distribution.
                           - weibull_gaussian_label: List of countries using the Weibull-Gaussian distribution.

    Behavior:
        - If the `country` is in the Weibull list, all countries from the Weibull-Gaussian list are appended
          to the Weibull list, and the Weibull-Gaussian list is cleared.
        - If the `country` is in the Weibull-Gaussian list, all countries from the Weibull list are appended
          to the Weibull-Gaussian list, and the Weibull list is cleared.
        - If the `country` is not found in either list, both lists are cleared.

    Returns:
        - dict: A dictionary containing the updated country lists:
                - weibull_label: Updated list of countries for Weibull distribution.
                - weibull_gaussian_label: Updated list of countries for Weibull-Gaussian distribution.

    Example:
        opt_dist = {
            weibull_label: ["France", "Germany"],
            weibull_gaussian_label: ["Poland", "Bulgaria"]
        }

        result = update_optimal_distribution_based_on_country_csp("Germany", opt_dist)

        # result will be:
        # {
        #     weibull_label: ["France", "Germany", "Poland", "Bulgaria"],
        #     weibull_gaussian_label: []
        # }
    """
    weibull_countries = opt_dist[weibull_label]
    wg_countries = opt_dist[weibull_gaussian_label]
    # Checking if the provided country is present in weibull_countries and wg_countries
    if country in weibull_countries:
        weibull_countries.extend(wg_countries)
        wg_countries = []
    elif country in wg_countries:
        wg_countries.extend(weibull_countries)
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
