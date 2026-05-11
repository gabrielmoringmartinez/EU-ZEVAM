"""Save CSP figures to disk."""

# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

from zevampy.load_data_and_prepare_inputs.dimension_names import *


def save_figure(fig, file_info, distribution_type):
    """
    Save a figure to disk.

    The figure is saved only if saving is enabled in the provided file configuration dictionary.

    Parameters:
        fig (matplotlib.figure.Figure):
            Figure object to save.

        file_info (dict):
            Dictionary containing output-file settings such as folder, filename components, and file extension.

        distribution_type (str or None):
            Distribution type identifier added to the filename. Supported values include "Weibull", "WG", or None.

    Returns:
        None
    """
    if file_info[save_figure_dim]:
        if distribution_type is None:
            distribution_type = ""
        filepath = f'{file_info[folder_dim]}{file_info[main_title_dim]}_{distribution_type}{file_info[group_info_dim]}'\
                   f'{file_info[additional_info_dim]}{file_info[file_extension_dim]}'
        fig.savefig(filepath)
