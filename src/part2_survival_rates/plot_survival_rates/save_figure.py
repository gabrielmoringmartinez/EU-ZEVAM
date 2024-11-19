

def save_figure(fig, file_info, distribution_type):
    """
        Saves the generated figure to the specified file path if the `save_figure` flag is set in `file_info`.

        Parameters:
        - fig (matplotlib.figure.Figure): The figure object that needs to be saved.
        - file_info (dict): Dictionary containing file information, such as file name and save options.
        - activate_weibull (int): If 1, includes Weibull fit in the plot; 0 excludes it.
        - activate_weibull_and_normal (int): If 1, includes Weibull-Gaussian fit in the plot; 0 excludes it.

        Returns:
        - None
        """
    if file_info["save_figure"]:
        if distribution_type == None:
            distribution_type =""
        filepath = f'{file_info["folder"]}{file_info["main title"]}_{distribution_type}{file_info["group_info"]}' \
                   f'{file_info["additional_info"]}{file_info["file_extension"]}'
        fig.savefig(filepath)