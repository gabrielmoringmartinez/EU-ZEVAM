from src.load_data_and_prepare_inputs.dimension_names import *


def save_figure(fig, file_info, distribution_type):
    """
    Saves the generated figure to the specified file path if the `save_figure` flag is set in `file_info`.

    Parameters:
        - fig (matplotlib.figure.Figure): The figure object that needs to be saved.
        - file_info (dict): Dictionary containing file information, such as file name, folder path, and save options.
                        Expected keys include:
                            - 'save_figure_dim': (bool) If True, the figure will be saved.
                            - 'folder_dim': (str) The folder path where the figure will be saved.
                            - 'main_title_dim': (str) The main title of the figure used in the file name.
                            - 'group_info_dim': (str) Additional group-specific information to include in the file name.
                            - 'additional_info_dim': (str) Any extra information to include in the file name.
                            - 'file_extension_dim': (str) The file extension (e.g., '.png', '.pdf').
        - distribution_type (str or None): A string representing the type of distribution used in the plot
                                            (e.g., "Weibull", "WG"). If `None`, no distribution type will be included
                                             in the file name.

    Returns:
        - None
    """
    if file_info[save_figure_dim]:
        if distribution_type is None:
            distribution_type = ""
        filepath = f'{file_info[folder_dim]}{file_info[main_title_dim]}_{distribution_type}{file_info[group_info_dim]}'\
                   f'{file_info[additional_info_dim]}{file_info[file_extension_dim]}'
        fig.savefig(filepath)
