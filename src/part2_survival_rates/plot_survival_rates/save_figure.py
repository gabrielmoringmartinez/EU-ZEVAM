

def save_figure(fig, file_info, activate_weibull, activate_weibull_and_normal):
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
        folder, paper_info = get_folder_and_paper_info(file_info["own_calculation"])
        pdf_label = get_pdf_label(activate_weibull, activate_weibull_and_normal)
        filepath = f'outputs/figures/CSP_{file_info["year"]}_{pdf_label}{file_info["group_info"]}' \
                   f'{file_info["additional_info"]}_{paper_info}{file_info["file_extension"]}'
        fig.savefig(filepath)


def get_pdf_label(activate_weibull, activate_weibull_and_normal):
    """
        Generates a label for the PDF based on the flags for Weibull and Weibull-Gaussian distributions.

        Parameters:
        - activate_weibull (int): If 1, includes Weibull fit in the plot; 0 excludes it.
        - activate_weibull_and_normal (int): If 1, includes Weibull-Gaussian fit in the plot; 0 excludes it.

        Returns:
        - str: The generated PDF label based on the activation flags (e.g., 'Weibull_' or 'WeibullGaussian_').
        """
    if activate_weibull == 1 and activate_weibull_and_normal == 0:
        return 'Weibull_'
    elif activate_weibull == 0 and activate_weibull_and_normal == 1:
        return 'WeibullGaussian_'
    else:
        return ''


def get_folder_and_paper_info(own_calculation):
    """
        Determines the folder and paper information based on whether the calculation is an "own calculation" or
        from an external paper.

        Parameters:
        - own_calculation (bool): Flag indicating whether the calculation is an own calculation (True) or
         from an external paper (False).

        Returns:
        - tuple: A tuple containing the folder name and the corresponding paper information string.
        """
    if own_calculation:
        return 'own_calculation', 'own_calculation'
    else:
        return 'external_paper', 'external_paper'