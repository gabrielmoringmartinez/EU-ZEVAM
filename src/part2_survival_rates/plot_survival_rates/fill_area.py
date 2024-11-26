from src.load_data_and_prepare_inputs.dimension_names import *


def fill_area_based_on_label(ax, merged_df_country, x_column, columns_to_plot_keys, fill_between_label):
    """
    Fills the area under the CSP curve based on the specified fill-between label.

    Parameters:
        - ax (matplotlib.axes): The axes object for the plot.
        - merged_df_country (pd.DataFrame): DataFrame filtered for a specific country.
        - x_column (str): The column name for the x-axis.
        - columns_to_plot_keys (list): List of column names to fill areas for.
        - fill_between_label (str): The label indicating the type of fill area operation to perform.

    Returns:
        - ax (matplotlib.axes): The updated axes object.
    """
    if fill_between_label == country_csp_label:
        ax = fill_area(ax, merged_df_country, x_column, columns_to_plot_keys)
    elif fill_between_label == historical_csp_label:
        ax = fill_area_historical_values(ax, merged_df_country, x_column, columns_to_plot_keys)
    elif fill_between_label == increase_decrease_csp_label:
        ax = fill_area_increase_decrease(ax, merged_df_country, x_column, columns_to_plot_keys)
    return ax


def fill_area(ax, df, x_label, y_label):
    """
    Fills the area between two CSP curves for a given country  with predefined rules.

    Parameters:
        - ax (matplotlib.axes): The axes object for the plot.
        - df (pd.DataFrame): DataFrame containing the x and y data to plot.
        - x_label (str): The column name for the x-axis.
        - y_label (list): A list of column names specifying the y-values to plot and compare.

    Returns:
        - ax (matplotlib.axes): The updated axes object with the filled area.
    """
    ax.fill_between(
        df[x_label], df[y_label[0]], df[y_label[1]], where=(df[y_label[0]] > df[y_label[1]]),
        interpolate=True, color="red", alpha=0.25)

    ax.fill_between(
        df[x_label], df[y_label[0]], df[y_label[-1]], where=(df[y_label[0]] <= df[y_label[-1]]),
        interpolate=True, color="green", alpha=0.25)
    return ax


def fill_area_historical_values(ax, df, x_label, y_label):
    """
    Fills the area under the historical CSP curve for a given country with predefined rules.

    Parameters:
        - ax (matplotlib.axes): The axes object for the plot.
        - df (pd.DataFrame): DataFrame containing the x and y data to plot.
        - x_label (str): The column name for the x-axis.
        - y_label (list): A list of column names specifying the y-values to plot and compare.

    Returns:
        - ax (matplotlib.axes): The updated axes object with the filled area under historical CSP curves.
        """
    ax.fill_between(
        df[x_label], df[y_label[0]], df[y_label[1]], where=(df[y_label[0]] <= df[y_label[1]]),
        interpolate=True, color="red", alpha=0.25)

    ax.fill_between(
        df[x_label], df[y_label[0]], df[y_label[-1]], where=(df[y_label[0]] <= df[y_label[-1]]),
        interpolate=True, color="red", alpha=0.25)

    ax.fill_between(
        df[x_label], df[y_label[1]], df[y_label[-1]], where=(df[y_label[1]] <= df[y_label[-1]]),
        interpolate=True, color="red", alpha=0.25)

    ax.fill_between(
        df[x_label], df[y_label[0]], df[y_label[1]], where=(df[y_label[0]] > df[y_label[1]]),
        interpolate=True, color="green", alpha=0.25)
    return ax


def fill_area_increase_decrease(ax, df, x_label, y_label):
    """
    Fills areas between CSP curves to indicate increases or decreases in survival probabilities.

    Parameters:
        - ax (matplotlib.axes): The axes object for the plot.
        - df (pd.DataFrame): DataFrame containing the x and y data to plot.
        - x_label (str): The column name for the x-axis.
        - y_label (list): A list of column names specifying the y-values to plot and compare.
                          The middle column is treated as the reference line.

    Returns:
        - ax (matplotlib.axes): The updated axes object with areas filled to indicate changes.
    """
    ref_line_pos = len(y_label) // 2
    ax.fill_between(
        df[x_label], df[y_label[0]], df[y_label[ref_line_pos]], where=(df[y_label[ref_line_pos]] < df[y_label[0]]),
        interpolate=True, color="green", alpha=0.25)

    ax.fill_between(
        df[x_label], df[y_label[ref_line_pos]], df[y_label[-1]], where=(df[y_label[ref_line_pos]] >= df[y_label[-1]]),
        interpolate=True, color="red", alpha=0.25)

    ax.fill_between(
        df[x_label], df[y_label[0]], df[y_label[ref_line_pos]], where=(df[y_label[ref_line_pos]] > df[y_label[0]]),
        interpolate=True, color="red", alpha=0.25)

    ax.fill_between(
        df[x_label], df[y_label[ref_line_pos]], df[y_label[-1]], where=(df[y_label[ref_line_pos]] <= df[y_label[-1]]),
        interpolate=True, color="green", alpha=0.25)
    return ax
