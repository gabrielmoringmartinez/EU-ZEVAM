from src.part2_survival_rates.plot_survival_rates.plot_csp_countries import plot_csp_countries


def plot_all_countries(pdf_parameters, survival_rates, config, own_calculation=False, activate_weibull=1,
                       activate_weibull_and_normal=1):
    plot_params = config["plot_params"]
    file_info = config["file_info"]
    country_names = survival_rates['country label'].unique()
    number_of_countries = len(country_names)  # Number of countries is defined
    pdf_parameters.to_excel(f'outputs/test_pdf_parameters.xlsx', index=False)
    survival_rates_weibull, survival_rates_weibull_and_normal = \
        plot_csp_countries(survival_rates, country_names, pdf_parameters, plot_params, file_info,
                           activate_weibull, activate_weibull_and_normal)
    return


def plot_group_of_countries(pdf_parameters, survival_rates, group_of_countries, config, own_calculation=False,
                            activate_weibull=1, activate_weibull_and_normal=1):
    plot_params = config["plot_params"]
    file_info = config["file_info"]
    country_names = survival_rates['country label'].unique()
    if group_of_countries == 1:
        country_names = country_names[0:plot_params["number_of_countries_group"]]
    else:
        country_names = country_names[plot_params["number_of_countries_group"]:len(country_names)]
    file_info["group_info"] = f'group{group_of_countries}'
    plot_csp_countries(survival_rates, country_names, pdf_parameters, plot_params, file_info,
                       activate_weibull, activate_weibull_and_normal)
    return