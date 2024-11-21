def generate_columns_to_plot(columns_to_plot, items_selected, general_legend_text):
    """
    Generates the columns_to_plot dictionary for the plot legend based on selected items
    and a customizable text template.

    Args:
        columns_to_plot (dict): Dictionary to populate with plot legend mappings.
        items_selected (list): List of items (e.g., years or countries) to process.
        general_legend_text (str): General text, and also'{item}' is replaced
                                   with each item from items_selected.

    Returns:
        dict: Updated columns_to_plot dictionary.
    """
    for item in items_selected:
        column_name = f"share_{item}"
        columns_to_plot[column_name] = f"{general_legend_text} {item}"
    return columns_to_plot
