def generate_columns_to_plot(columns_to_plot, countries_selected, country_adjectives):
    """
    Updates and returns a dictionary mapping column names to their display labels for plot legends.

    Parameters:
        - columns_to_plot (dict): A dictionary where keys are column names and values arethe corresponding labels for
         the plot legend.
        - countries_selected (list of str): list of countries for which CSP (Country-Specific Parameters) values are
        selected and substituted in all countries to observe the effect.
        - country_adjectives (dict): A dictionary mapping each country to its descriptive adjective.
        Example: {"Germany": "German", "France": "French"}.

    Returns:
        - dict: Updated `columns_to_plot` dictionary where new entries are added with keys in the form `share_<country>`
            and values as "Share with <adjective> CSP".
    """
    for country in countries_selected:
        column_name = f"share_{country}"
        columns_to_plot[column_name] = f"Share with {country_adjectives[country]} CSP"
    return columns_to_plot
