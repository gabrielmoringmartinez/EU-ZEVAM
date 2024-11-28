def generate_columns_to_plot(columns_to_plot, increase_selected):
    """
    Updates and returns a dictionary mapping column names to their display labels for plot legends, based on the
    selected percentage increase or reduction.

    Parameters:
          - columns_to_plot (dict): A dictionary where keys are column names and values are the corresponding
            labels for the plot legend.
          - increase_selected (list of float): A list of percentage changes to apply to the CSP values. These values
            can be positive (for increases), negative (for reductions), or zero (for the empirical CSP). Each value
            represents the percentage change applied (e.g., 0.2 for a 20% increase, -0.1 for a 10% decrease, or 0 for
            empirical CSP).

    Returns:
        - dict: Updated `columns_to_plot` dictionary where new entries are added with keys in the form `share_<increase>
        ` (e.g., `share_0.2`, `share_-0.1`) and values as descriptions like  "Share with a <increase_in_percentage>%
         increase", when values are higher than 0, "Share with a <increase_in_percentage>% reduction", when values are
         lower than 0 or "Share with empirical CSP" if the value is zero.
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


