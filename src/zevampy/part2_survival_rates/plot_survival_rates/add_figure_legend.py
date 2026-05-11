"""Add legends to matplotlib figures."""

# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

from zevampy.load_data_and_prepare_inputs.dimension_names import *


def add_figure_legend(fig, ax, plot_params):
    """
    Add a legend to a matplotlib figure.

    Parameters:
        fig (matplotlib.figure.Figure):
            Figure object where the legend is added.

        ax (matplotlib.axes.Axes):
            Axes object used to retrieve legend handles and labels.

        plot_params (dict):
            Dictionary containing legend configuration parameters.

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
