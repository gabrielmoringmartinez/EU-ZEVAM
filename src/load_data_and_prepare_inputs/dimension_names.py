time_dim = 'time'
year_of_first_registration_dim = "year of first registration"
age_dim = 'vehicle age'
stock_year_dim = 'stock year'
stock_year_empirical_csp_data_dim = 'stock year of empirical csp data'
country_dim = 'geo country'
cluster_dim = 'cluster'
powertrain_dim = 'powertrain'
new_registrations_dim = 'new vehicle registrations'
share_dim = 'share'
relative_sales_dim = 'relative sales'
registrations_by_powertrain_dim = 'registrations by powertrain'
survival_rate_dim = "survival rate"
number_registered_vehicles_dim = "number of registered vehicles"
distribution_dim = 'distribution'
stock_dim = 'stock'

gamma_weibull_dim = "gamma (Weibull)"
beta_weibull_dim = "beta (Weibull)"
r_squared_weibull_dim = "r squared (Weibull)"
k_weibull_gaussian_dim = "k (Import-Gaussian)"
mu_weibull_gaussian_dim = "mu (Import-Gaussian)"
sigma_weibull_gaussian_dim = "sigma (Import-Gaussian)"
delta_weibull_gaussian_dim = "delta (Import-Gaussian)"
r_squared_weibull_gaussian_dim = "r squared (Weibull and Import-Gaussian)"


weibull_label = "Weibull"
weibull_gaussian_label = "WG"
survival_rate_weibull_dim = f"{survival_rate_dim} {weibull_label}"
survival_rate_weibull_gaussian_dim = f"{survival_rate_dim} {weibull_gaussian_label}"
stock_weibull_dim = f'{stock_dim}_{weibull_label}'
stock_wg_dim = f'{stock_dim}_{weibull_gaussian_label}'
weibull_plot_label = 'Weibull fit'
weibull_gaussian_plot_label = 'WG fit'
data_points_plot_label = 'data points'

eu_9_label = 'EU-9'
eu_26_plus_norway_label = 'EU-26+Norway'
eu_27_plus_norway_label = 'EU-27+Norway'

# Define dimensions for dictionary keys
plot_params_dim = 'plot_params'
file_info_dim = 'file_info'
group_info_dim = 'group_info'
group_suffix_for_saving_output = 'group'
save_figure_dim = "save_figure"
folder_dim = "folder"
main_title_dim = "main title"
additional_info_dim = "additional_info"
group_info_dim = "group_info"
comparison_type_dim = "comparison_type"
own_calculation_dim = "own_calculation"
file_extension_dim = "file_extension"

tick_fontsize_dim = "tick_fontsize"
legend_fontsize_dim = "legend_fontsize"
title_fontsize_dim = "title_fontsize"
space_between_plots_dim = "space_between_plots"
figure_height_dim = "figure_height"
figure_width_dim = "figure_width"
marker_size_dim = "marker_size"
line_width_dim = "line_width"
show_grid_dim = "show_grid"
title_dim = "title"
x_column_dim = "x_column"
x_label_dim = "x_label"
y_label_dim = "y_label"
x_lim_dim = "x_lim"
y_lim_dim = "y_lim"
x_ticks_dim = "x_ticks"
number_of_countries_group_dim = "number_of_countries_group"
title_font_dim = "title_font"
title_vertical_position_dim = "title_vertical_position"
axis_title_font_dim = "axis_title_font"
x_axis_title_vertical_position_dim = "x_axis_title_vertical_position"
y_axis_title_horizontal_position_dim = "y_axis_title_horizontal_position"
legend_show_dim = "legend_show"
legend_loc_dim = "legend_loc"
legend_bbox_to_anchor_dim = "legend_bbox_to_anchor"
fill_between_dim = "fill_between"
number_of_decimals_dim = "number_of_decimals"
num_rows_dim = "num_rows"
num_columns_dim = "num_columns"

country_csp_label = 'country csp'
historical_csp_label = 'historical csp'
increase_decrease_csp_label = 'increased or decreased csp'



# CSV data labels
country_labels_label = "country_labels"
clusters_label = "clusters"
registration_shares_by_cluster_label = "registration_shares_by_cluster"
historical_registrations_label = "historical_registrations"
registrations_eu_cam_scenario_label = "registrations_eu_cam_scenario"
stock_by_age_2021_label = "stock_by_age_2021"
survival_rates_2021_label = "survival_rates_2021"
stock_year_label = "stock_year"
actual_bev_registration_shares_label = "actual_bev_registration_shares"
actual_bev_stock_shares_label = "actual_bev_stock_shares"
optimum_parameters_2008_label = "optimum_parameters_2008"
survival_rates_2016_label = "survival_rates_2016"
# inputs labels
eu_countries_and_norway_label = "eu_countries_and_norway"
simulation_stock_years_label = "stock_years"
csp_data_ref_year_label = "csp_data_ref_year"
csp_available_years_label = "csp_available_years"
historical_csp_label = "historical_csp"
save_options_stock_label = "save_options_stock"
distribution_bounds_label = "distribution_bounds"
# Inputs for plot configuration labels
config_all_label = "config_all"
config_group_label = "config_group"
config_bev_reference_scenario_label = "config_bev_reference_scenario"
config_validation_step1_label = "config_validation_step1"
config_validation_step2_label = "config_validation_step2"
config_validation_rmse_step1_label = "config_validation_rmse_step1"
config_validation_rmse_step2_label = "config_validation_rmse_step2"
config_sensitivity_1_label = "config_sensitivity_1"
config_sensitivity_2_label = "config_sensitivity_2"
config_sensitivity_3_label = "config_sensitivity_3"
config_sensitivity_4_label = "config_sensitivity_4"

# Output labels of step2: calculate_and_plot_csps_and_stock.py
registrations_label = "registrations"
stock_values_label = "stock_values"
stock_shares_label = "stock_shares"
optimum_parameters_wg_label = "optimum_parameters_wg"
fitted_csp_values_label = "fitted_csp_values"
optimal_distribution_dict_label = 'optimal_distribution_dict'


stock_data_filename_label = 'stock_data_filename'
stock_shares_filename_label = 'stock_shares_filename'

powertrains_rmse_label = "powertrains"
timeframes_rmse_label = "timeframes"