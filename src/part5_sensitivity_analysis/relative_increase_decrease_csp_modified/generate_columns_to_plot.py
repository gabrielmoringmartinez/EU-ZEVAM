def generate_columns_to_plot(columns_to_plot, increase_selected):
    """
    Generates the columns_to_plot dictionary for the plot legend.
    """
    for increase in increase_selected:
        increase_in_percentage = increase * 100
        column_name = f"share_{increase}"
        columns_to_plot[column_name] = f"Share with a {increase_in_percentage}% reduction"
    return columns_to_plot


