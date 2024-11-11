from src.loader.loader import *
from src.part1_transportation_model.input_data import eu_countries_and_norway
from src.part1_transportation_model.calculate_registrations import calculate_registrations
from src.part2_survival_rates.calculate_csp_parameters import calculate_csp_parameters


def adapt_registrations_to_vehicle_stock_year(historical_registrations):
    # This is necessary to afterwards calculate the stock!!!
    country_label = []
    vehicle_age = []
    new_registrations = []

    for index, row in historical_registrations.iterrows():
        if row['stock year'] >= row['time']:
            country_label.append(row['country label'])
            vehicle_age.append(row['stock year'] - row['time'] + 1)
            new_registrations.append(row['new vehicle registrations'])

    my_dict = {'country label': country_label, 'vehicle age': vehicle_age, 'new registrations': new_registrations}
    return my_dict


historical_registrations_ = pd.merge(historical_registrations, stock_year, how='left')
historical_registrations_ = adapt_registrations_to_vehicle_stock_year(historical_registrations_)

# START

registrations = calculate_registrations(historical_registrations, eu_countries_and_norway, country_labels,
                                        registrations_eu_cam_scenario, clusters, registration_shares_by_cluster)
optimum_parameters_wg = calculate_csp_parameters(survival_rates_2021, 2021)

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
import numpy as np
import math

# Define your configuration dictionary
config = {
    "plot_params": {
        "tick_fontsize": 28,
        "legend_fontsize": 28,
        "title_fontsize": 36,
        "space_between_plots": 0.22,
        "figure_height": 40,
        "figure_width": 40,
        "marker_size": 6,
        "line_width": 2,
        "show_grid": True,
        "x_column": "vehicle age",
        "y_column": "survival rate",
        "x_label": "Age of vehicle",
        "y_label": "Cumulative Survival Probability (CSP)",
        "number_of_countries_group": 16,
        "titles": "",
    },
    "file_info": {
        "save_figure": True,
        "year": '2021',
        "file_add_info": 'all_countries',
        "group_info": '',
        "comparison_info": '',
        "own_calculation": True,
    },
}


def get_multiple_plots(survival_rates, pdf_parameters, config):
    plot_all_countries(pdf_parameters, survival_rates, config)
    country_group = 1
    plot_group_of_countries(pdf_parameters, survival_rates, country_group, config)
    country_group = 2
    plot_group_of_countries(pdf_parameters, survival_rates, country_group, config)
    plot_all_countries(pdf_parameters, survival_rates, config, activate_weibull=1,
                       activate_weibull_and_normal=0)
    plot_all_countries(pdf_parameters, survival_rates, config, activate_weibull=0,
                       activate_weibull_and_normal=1)


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


def plot_csp_countries(survival_rates, country_names, pdf_parameters, plot_params, file_info,
                       activate_weibull=1, activate_weibull_and_normal=1):
    country_rows, country_columns = get_number_rows_and_columns(len(country_names))
    fig = setup_subplot_figure(plot_params)

    survival_rates_weibull = pd.DataFrame()
    survival_rates_weibull_and_normal = pd.DataFrame()
    i = 1
    for country_name in country_names:
        ax = fig.add_subplot(country_rows, country_columns, i)
        survival_rates_country = survival_rates[survival_rates["country label"] == country_name]
        plot_survival_rate_country(ax, "Data points", survival_rates_country[plot_params["x_column"]],
                                   survival_rates_country[plot_params["y_column"]], country_name, plot_params, i)

        pdf_df = pdf_parameters
        gamma, beta, k, mu, sigma = get_statistical_parameters(pdf_df)
        gamma_country, beta_country, k_country, mu_country, sigma_country = \
            get_statistical_parameters_of_each_country(gamma, beta, k, mu, sigma, country_name)
        weibull_values = get_weibull_function(gamma_country, beta_country)
        wg_values = get_weibull_and_normal_function(gamma_country, beta_country, k_country, mu_country, sigma_country)
        if activate_weibull:
            plot_survival_rate_country(ax, f"Weibull fit", survival_rates_country[plot_params["x_column"]],
                                       weibull_values, country_name, plot_params, i)
        if activate_weibull_and_normal:
            plot_survival_rate_country(ax, f"WG fit", survival_rates_country[plot_params["x_column"]],
                                       wg_values, country_name, plot_params, i)

        survival_rates_weibull = get_distribution_function_discrete_points(survival_rates_weibull,
                                                                           survival_rates_country, weibull_values)
        survival_rates_weibull_and_normal = get_distribution_function_discrete_points(survival_rates_weibull_and_normal,
                                                                                      survival_rates_country, wg_values)
        i=i+1
    save_figure(fig, file_info, activate_weibull, activate_weibull_and_normal)
    return survival_rates_weibull, survival_rates_weibull_and_normal


def get_pdf_label(activate_weibull, activate_weibull_and_normal):
    if activate_weibull == 1 and activate_weibull_and_normal == 0:
        return 'Weibull_'
    elif activate_weibull == 0 and activate_weibull_and_normal == 1:
        return 'WeibullGaussian_'
    else:
        return ''


def get_folder_and_paper_info(own_calculation):
    if own_calculation:
        return 'own_calculation', '_own_calculation'
    else:
        return 'external_paper', '_external_paper'


def get_comparison_info(comparison_info):
    if comparison_info:
        return 'comparison'
    else:
        return ''


def generate_output_filepath(folder_info, year, pdf_label, group_info, file_add_info, paper_info, comparison_info):
    if comparison_info == 'comparison':
        return f'outputs/figures/CSP_{year}_{pdf_label}_{comparison_info}' \
               f'{paper_info}.png'
    else:
        return f'outputs/figures/CSP_{year}_{pdf_label}{group_info}{file_add_info}' \
               f'{paper_info}.png'


def get_number_rows_and_columns(number_of_countries):
    country_rows = math.ceil(np.sqrt(number_of_countries))  # Rows and columns are defined
    country_columns = country_rows
    return country_rows, country_columns


def setup_subplot_figure(plot_params):
    plt.rc('xtick', labelsize=plot_params["tick_fontsize"])
    plt.rc('ytick', labelsize=plot_params["tick_fontsize"])
    fig = plt.figure()
    fig.subplots_adjust(hspace=plot_params["space_between_plots"], wspace=plot_params["space_between_plots"])
    fig.set_figheight(plot_params["figure_height"])
    fig.set_figwidth(plot_params["figure_width"])
    return fig


def plot_survival_rate_country(ax, label, x, y, country_name, plot_params, i):
    ax.plot(x, y, '-o', markersize=plot_params["marker_size"], linewidth=plot_params["line_width"], label=label)
    if i == 2:
        ax.legend(fontsize=plot_params["legend_fontsize"])
    ax.set_title(country_name, fontsize=plot_params["title_fontsize"])
    plt.style.use('seaborn-v0_8-white')
    ax = plt.gca()
    customize_axes(ax, plot_params["show_grid"])


def customize_axes(ax, show_grid):
    if show_grid:
        plt.grid(True)  # Enable grid lines
    else:
        plt.grid(False)  # Disable grid lines
    # Set y-axis tick format to display one decimal place
    ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.1f'))
    plt.xlim(0, 45)  # Set x-axis limits
    plt.ylim(0, None)  # Set x-axis limits
    # Set tick positions for y-axis to avoid overlapping at 0
    y_ticks = ax.get_yticks()
    ax.set_yticks([0] + y_ticks[y_ticks != 0])

    # Set tick positions for x-axis to avoid overlapping at 0
    x_ticks = ax.get_xticks()
    return ax


def customize_axes(ax, show_grid):
    ax.grid(show_grid)
    ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.1f'))
    ax.set_xlim(0, 45)
    ax.set_ylim(0, None)
    y_ticks = ax.get_yticks()
    ax.set_yticks([0] + y_ticks[y_ticks != 0])


def save_figure(fig, file_info, activate_weibull, activate_weibull_and_normal):
    if file_info["save_figure"]:
        folder, paper_info = get_folder_and_paper_info(file_info["own_calculation"])
        pdf_label = get_pdf_label(activate_weibull, activate_weibull_and_normal)
        filepath = f'outputs/figures/CSP_{file_info["year"]}_{pdf_label}{file_info["group_info"]}{file_info["file_add_info"]}{paper_info}.png'
        fig.savefig(filepath)


def get_weibull_function(gamma_variable, beta_variable):
    year_a = np.linspace(1, 45, 45)
    CSP = []
    for x in year_a:
        CSP_value = np.exp(
            -(x / gamma_variable) ** beta_variable * (math.gamma(1 + 1 / beta_variable)) ** beta_variable)
        CSP.append(float(CSP_value))
    return CSP


def get_weibull_and_normal_function(gamma_variable, beta_variable, k, mu, sigma):
    year_a = np.linspace(1, 45, 45)
    CSP = []
    for x in year_a:
        weibull = np.exp(-(x / gamma_variable) ** beta_variable * (math.gamma(1 + 1 / beta_variable)) ** beta_variable)
        delta = k / (np.sqrt(np.pi * 2) * sigma)
        normal = delta * np.exp(-0.5 * ((x - mu) / sigma) ** 2)
        CSP_value = weibull + normal
        CSP.append(float(CSP_value))
    return CSP


def get_distribution_function_discrete_points(survival_rate_distribution_function, survival_rates_country,
                                              predicted_function_value):
    survival_rates_country = survival_rates_country.reset_index()  # for reseting the index
    survival_rates_country = survival_rates_country.drop(['index'], axis=1)  # deleting the new column of index
    survival_rates_country['survival rate'] = predicted_function_value
    survival_rate_distribution_function = pd.concat([survival_rate_distribution_function, survival_rates_country],
                                                    ignore_index=True)
    survival_rate_distribution_function.to_excel(f'outputs/test_survival_rate_distribution_function.xlsx', index=False)
    return survival_rate_distribution_function


def get_statistical_parameters(pdf_parameters):
    gamma_variable = pdf_parameters[["gamma (Weibull)", "country label"]]
    beta_variable = pdf_parameters[["beta (Weibull)", "country label"]]
    k_variable = pdf_parameters[["k (Import-Gaussian)", "country label"]]
    mu_variable = pdf_parameters[["mu (Import-Gaussian)", "country label"]]
    sigma_variable = pdf_parameters[["sigma (Import-Gaussian)", "country label"]]
    return gamma_variable, beta_variable, k_variable, mu_variable, sigma_variable


def get_statistical_parameters_of_each_country(gamma, beta, k, mu, sigma, country_name):
    gamma_country = gamma[gamma["country label"] == country_name]["gamma (Weibull)"]
    beta_country = beta[beta["country label"] == country_name]["beta (Weibull)"]
    k_country = k[k["country label"] == country_name]["k (Import-Gaussian)"]
    mu_country = mu[mu["country label"] == country_name]["mu (Import-Gaussian)"]
    sigma_country = sigma[sigma["country label"] == country_name]["sigma (Import-Gaussian)"]
    return gamma_country, beta_country, k_country, mu_country, sigma_country


get_multiple_plots(survival_rates_2021, optimum_parameters_wg, config)
