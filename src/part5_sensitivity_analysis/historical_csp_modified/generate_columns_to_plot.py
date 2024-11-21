def generate_columns_to_plot(columns_to_plot, years_selected):
    """
    Generates the columns_to_plot dictionary for the plot legend.
    """
    for year in years_selected:
        column_name = f"share_{year}"
        columns_to_plot[column_name] = f"Share with CSP from {year}"
    return columns_to_plot


