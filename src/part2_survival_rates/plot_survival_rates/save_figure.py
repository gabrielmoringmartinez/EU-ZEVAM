

def save_figure(fig, file_info, activate_weibull, activate_weibull_and_normal):
    if file_info["save_figure"]:
        folder, paper_info = get_folder_and_paper_info(file_info["own_calculation"])
        pdf_label = get_pdf_label(activate_weibull, activate_weibull_and_normal)
        filepath = f'outputs/figures/CSP_{file_info["year"]}_{pdf_label}{file_info["group_info"]}' \
                   f'{file_info["additional_info"]}_{paper_info}{file_info["file_extension"]}'
        fig.savefig(filepath)


def get_pdf_label(activate_weibull, activate_weibull_and_normal):
    if activate_weibull == 1 and activate_weibull_and_normal == 0:
        return 'Weibull_'
    elif activate_weibull == 0 and activate_weibull_and_normal == 1:
        return 'WeibullGaussian_'
    else:
        return ''


def get_folder_and_paper_info(own_calculation):
    if own_calculation:
        return 'own_calculation', 'own_calculation'
    else:
        return 'external_paper', 'external_paper'