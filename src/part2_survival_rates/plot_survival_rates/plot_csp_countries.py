from src.part2_survival_rates.plot_survival_rates.setup_subplots import get_number_rows_and_columns, \
    setup_subplot_figure
from src.part2_survival_rates.plot_survival_rates.plot_subplot import plot_survival_rate_country
from src.part2_survival_rates.plot_survival_rates.save_figure import save_figure


def plot_csp_countries(merged_df, country_names, plot_params, file_info, columns_to_plot_dict, distribution_type):
    """
       Plots cumulative survival probability (CSP) curves for the specified countries with optional Weibull
       and/or Weibull-Gaussian fits.

       Parameters:
        - merged_df (pd.DataFrame): DataFrame containing columns to plot for all countries
        - country_names (list): List of country names to be plotted.
        - plot_params (dict): Dictionary containing the settings for the subplot, including font sizes,
                              spacing, figure size, and titles.
        - file_info (dict): Dictionary containing file information, such as file name and save options.
       - columns_to_plot_dict (dict): Name of the columns to be plotted and its corresponding name in the legend graph
       - distribution_type (string): It indicates the distribution type which is plot (None, Weibull, WG)

       """
    country_rows, country_columns = get_number_rows_and_columns(len(country_names), plot_params)
    fig = setup_subplot_figure(plot_params)
    i = 1
    for country_name in country_names:
        ax = fig.add_subplot(country_rows, country_columns, i)
        merged_df_country = merged_df[merged_df["geo country"] == country_name]
        for column, legend in columns_to_plot_dict.items():
            plot_survival_rate_country(ax, legend, merged_df_country[plot_params["x_column"]],
                                       merged_df_country[column], country_name, plot_params, i)

        i = i + 1

    if plot_params.get("legend_show", True):
        handles, labels = ax.get_legend_handles_labels()
        fig.legend(handles, labels, loc=plot_params.get("legend_loc", "center right"),  bbox_to_anchor=
                   plot_params.get("legend_bbox_to_anchor", (1.2, 0.5)), fontsize=plot_params.get("legend_fontsize", 14))

    save_figure(fig, file_info, distribution_type)
    return
