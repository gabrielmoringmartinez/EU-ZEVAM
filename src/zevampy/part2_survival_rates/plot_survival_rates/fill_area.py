"""Fill plot areas between CSP curves for visual comparisons."""

# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

from zevampy.load_data_and_prepare_inputs.dimension_names import *


def fill_area_based_on_label(ax, merged_df_country, x_column, columns_to_plot_keys, fill_between_label):
    """
    Fill plot areas according to the selected comparison type.

    Parameters:
        ax (matplotlib.axes.Axes):
            Axes object where filled areas are drawn.

        merged_df_country (pandas.DataFrame):
            DataFrame containing data for one plotted country or group.

        x_column (str):
            Column name used for the x-axis.

        columns_to_plot_keys (list[str]):
            Column names used for the compared y-axis values.

        fill_between_label (str):
            Label defining which fill-area logic should be applied.

    Returns:
        matplotlib.axes.Axes:
            Updated axes object.
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
    Fill areas between two CSP curves.

    Parameters:
        ax (matplotlib.axes.Axes):
            Axes object where filled areas are drawn.

        df (pandas.DataFrame):
            DataFrame containing x-axis and y-axis values.

        x_label (str):
            Column name used for the x-axis.

        y_label (list[str]):
            Column names used for the compared y-axis values.

    Returns:
        matplotlib.axes.Axes:
            Updated axes object with filled areas.
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
    Fill areas between historical CSP comparison curves.

    Parameters:
        ax (matplotlib.axes.Axes):
            Axes object where filled areas are drawn.

        df (pandas.DataFrame):
            DataFrame containing x-axis and y-axis values.

        x_label (str):
            Column name used for the x-axis.

        y_label (list[str]):
            Column names used for the compared y-axis values.

    Returns:
        matplotlib.axes.Axes:
            Updated axes object with filled historical comparison areas.
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
    Fill areas indicating increases or decreases relative to a reference curve.

    Parameters:
        ax (matplotlib.axes.Axes):
            Axes object where filled areas are drawn.

        df (pandas.DataFrame):
            DataFrame containing x-axis and y-axis values.

        x_label (str):
            Column name used for the x-axis.

        y_label (list[str]):
            Column names used for the compared y-axis values. The middle
            column is treated as the reference curve.

    Returns:
        matplotlib.axes.Axes:
            Updated axes object with filled increase/decrease areas.
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
