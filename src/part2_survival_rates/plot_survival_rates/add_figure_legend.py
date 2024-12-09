from src.load_data_and_prepare_inputs.dimension_names import *


def add_figure_legend(fig, ax, plot_params):
    """
    Adds a legend when desired to the figure based on the provided plot parameters.

    Parameters:
        - fig (matplotlib.figure.Figure): The figure object where the legend will be added.
        - ax (matplotlib.axes.Axes): The axes object to retrieve handles and labels for the legend.
        - plot_params (dict): Dictionary containing legend-related parameters, such as location and font size.

    Returns:
        None
    """
    if plot_params.get(legend_show_dim, True):
        handles, labels = ax.get_legend_handles_labels()
        fig.legend(
            handles, labels,
            loc=plot_params.get(legend_loc_dim, "center right"),
            bbox_to_anchor=plot_params.get(legend_bbox_to_anchor_dim, (1.2, 0.5)),
            fontsize=plot_params.get(legend_fontsize_dim, 14)
        )
