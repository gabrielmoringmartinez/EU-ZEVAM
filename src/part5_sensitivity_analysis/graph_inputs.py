from src.load_data_and_prepare_inputs.dimension_names import *

# Define a base configuration for all cases
base_config = {
    "x_column": stock_year_dim,
    "x_label": "year",
    "y_label": "Battery Electric Vehicle (BEV) stock share (in %)",
    "powertrain_to_plot": "BEV",
    "x_lim": (2014, 2050),
    "y_lim": (0, 1),
    "decimals": 0,
    "num_columns": 5,
    "num_rows": 7,
    "figure_height": 50,
    "figure_width": 50,
    "marker_size": 6,
    "line_width": 2,
    "space_between_plots": 0.4,
    "file_extension": '.pdf',
    "title_font": 40,
    "title_vertical_position": 0.91,
    "axis_title_font": 40,
    "x_axis_title_vertical_position": 0.19,
    "y_axis_title_horizontal_position": 0.07,
    "share": True,
    "tick_fontsize": 28,
    "title_fontsize": 36,
    "show_grid": True,
    "number_of_decimals": 0,
    "legend_show": True,
    "stock_years": [2014, 2050],
    "historical_csp": 'no',  # Default value; can be overridden
    "file_info": {
        "save_figure": True,
        "folder": "outputs/figures/",
        "additional_info": '',
        "group_info": '',  # Can update this dynamically if needed
        "comparison_type": '',  # Optional: e.g., 'comparison' for side-by-side analyses
        "own_calculation": True,  # Set True if calculations are from own model or study
        "file_extension": '.pdf'
    },
}

# Create specialized configurations by updating only unique fields
config_sensitivity_1 = {
    "plot_params": {
        **base_config,
        "title": "BEV stock shares modifying country CSPs for all EU-27 countries and Norway",
        "countries_selected": ["Bulgaria", "Poland", "Italy", "Netherlands", "Germany", "Luxembourg"],
        "fill_between": country_csp_label,
        "legend_loc": "lower right",
        "legend_bbox_to_anchor": (0.97, 0.197),
        "legend_fontsize": 38,
    },
    "file_info": {
        **base_config["file_info"],
        "main title": "battery_electric_vehicle_stock_shares_eu_27_and_norway_up_to_2050_with_modified_country_csps",
    },
}

config_sensitivity_2 = {
    "plot_params": {
        **base_config,
        "title": "BEV stock shares using empirical CSP curves from 2008, 2016 and 2021 for all EU-27 countries and Norway",
        "years_selected": [2021, 2016, 2008],
        "historical_csp": historical_csp_label,
        "fill_between": historical_csp_label,
        "legend_loc": "lower center",
        "legend_bbox_to_anchor": (0.5, 0.12),
        "legend_fontsize": 40,
    },
    "file_info": {
        **base_config["file_info"],
        "main title": "battery_electric_vehicle_stock_shares_eu_27_and_norway_up_to_2050_with_modified_historical_country_csps",
    },
}

config_sensitivity_3 = {
    "plot_params": {
        **base_config,
        "title": "BEV stock shares in relation to different Weibull average lifespans, γ, and different normal Gaussian distributions, µ, for high-importing countries",
        "percentages_selected": [-0.4, -0.2, 0, 0.2, 0.4],
        "fill_between": increase_decrease_csp_label,
        "legend_loc": "lower right",
        "legend_bbox_to_anchor": (0.95, 0.22),
        "legend_fontsize": 40,
    },
    "file_info": {
        **base_config["file_info"],
        "main title": "battery_electric_vehicle_stock_shares_eu_27_and_norway_up_to_2050_with_increased_decreased_country_csps",
    },
}

config_sensitivity_4 = {
    "plot_params": {
        **base_config,
        "title": "BEV stock shares modifying country registrations for all EU-27 countries and Norway",
        "countries_selected": ["Poland", "France", "Norway"],
        "fill_between": country_csp_label,
        "legend_loc": "lower right",
        "legend_bbox_to_anchor": (1, 0.234),
        "legend_fontsize": 36,
    },
    "file_info": {
        **base_config["file_info"],
        "main title": "battery_electric_vehicle_stock_shares_eu_27_and_norway_up_to_2050_with_modified_registrations",
    },
}