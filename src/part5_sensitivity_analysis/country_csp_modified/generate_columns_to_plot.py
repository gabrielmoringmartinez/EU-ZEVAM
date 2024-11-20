def generate_columns_to_plot(columns_to_plot, countries_selected, country_adjectives):
    """
    Generates the columns_to_plot dictionary for the plot legend.
    """
    for country in countries_selected:
        column_name = f"share_{country}"
        columns_to_plot[column_name] = f"Share with {country_adjectives[country]} CSP"
    return columns_to_plot
