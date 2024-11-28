from src.load_data_and_prepare_inputs.dimension_names import *

# Define a base configuration for all cases
base_config = {
    x_column_dim: stock_year_dim,
    x_label_dim: "year",
    y_label_dim: "Battery Electric Vehicle (BEV) stock share (in %)",
    powertrain_to_plot_label: "BEV",
    x_lim_dim: (2014, 2050),
    y_lim_dim: (0, 1),
    year_to_modify_registrations_label: None,
    number_of_decimals_dim: 0,
    num_columns_dim: 5,
    num_rows_dim: 7,
    figure_height_dim: 50,
    figure_width_dim: 50,
    marker_size_dim: 6,
    line_width_dim: 2,
    space_between_plots_dim: 0.4,
    file_extension_dim: '.pdf',
    title_font_dim: 40,
    title_vertical_position_dim: 0.91,
    axis_title_font_dim: 40,
    x_axis_title_vertical_position_dim: 0.19,
    y_axis_title_horizontal_position_dim: 0.07,
    share_dim: True,
    tick_fontsize_dim: 28,
    title_fontsize_dim: 36,
    show_grid_dim: True,
    number_of_decimals_dim: 0,
    legend_show_dim: True,
    simulation_stock_years_label: [2014, 2050],
    historical_csp_label: 'no',  # Default value; can be overridden
    file_info_dim: {
        save_figure_dim: True,
        folder_dim: "outputs/figures/",
        additional_info_dim: '',
        group_info_dim: '',  # Can update this dynamically if needed
        comparison_type_dim: '',  # Optional: e.g., 'comparison' for side-by-side analyses
        own_calculation_dim: True,  # Set True if calculations are from own model or study
        file_extension_dim: '.pdf'
    },
}

# Create specialized configurations by updating only unique fields
config_sensitivity_1 = {
    plot_params_dim: {
        **base_config,
        title_dim: "BEV stock shares modifying country CSPs for all EU-27 countries and Norway",
        countries_selected_label: ["Bulgaria", "Poland", "Italy", "Netherlands", "Germany", "Luxembourg"],
        fill_between_dim: country_csp_label,
        legend_loc_dim: "lower right",
        legend_bbox_to_anchor_dim: (0.97, 0.197),
        legend_fontsize_dim: 38,
    },
    file_info_dim: {
        **base_config["file_info"],
        main_title_dim: "battery_electric_vehicle_stock_shares_eu_27_and_norway_up_to_2050_with_modified_country_csps",
    },
}

config_sensitivity_2 = {
    plot_params_dim: {
        **base_config,
        title_dim: "BEV stock shares using empirical CSP curves from 2008, 2016 and 2021 for all EU-27 countries and Norway",
        years_selected_label: [2021, 2016, 2008],
        historical_csp_label: historical_csp_label,
        fill_between_dim: historical_csp_label,
        legend_loc_dim: "lower center",
        legend_bbox_to_anchor_dim: (0.5, 0.12),
        legend_fontsize_dim: 40,
    },
    file_info_dim: {
        **base_config["file_info"],
        main_title_dim: "battery_electric_vehicle_stock_shares_eu_27_and_norway_up_to_2050_with_modified_historical_country_csps",
    },
}

config_sensitivity_3 = {
    plot_params_dim: {
        **base_config,
        title_dim: "BEV stock shares in relation to different Weibull average lifespans, γ, and different normal Gaussian distributions, µ, for high-importing countries",
        percentages_selected_label: [-0.4, -0.2, 0, 0.2, 0.4],
        fill_between_dim: increase_decrease_csp_label,
        legend_loc_dim: "lower right",
        legend_bbox_to_anchor_dim: (0.95, 0.22),
        legend_fontsize_dim: 40,
    },
    file_info_dim: {
        **base_config["file_info"],
        main_title_dim: "battery_electric_vehicle_stock_shares_eu_27_and_norway_up_to_2050_with_increased_decreased_country_csps",
    },
}

config_sensitivity_4 = {
    plot_params_dim: {
        **base_config,
        title_dim: "BEV stock shares modifying country registrations for all EU-27 countries and Norway",
        countries_selected_label: ["Poland", "France", "Norway"],
        fill_between_dim: country_csp_label,
        legend_loc_dim: "lower right",
        legend_bbox_to_anchor_dim: (1, 0.234),
        legend_fontsize_dim: 36,
        year_to_modify_registrations_label: 2024
    },
    file_info_dim: {
        **base_config["file_info"],
        main_title_dim: "battery_electric_vehicle_stock_shares_eu_27_and_norway_up_to_2050_with_modified_registrations",
    },
}