# Define your configuration dictionary
TITLE = "Actual BEV stock shares compared to estimated BEV shares using 2021 CSP curves and actual new BEV registrations"
X_COLUMN = "stock_year"
Y_COLUMN = "survival rate"
X_LABEL = "year"
Y_LABEL = "Cumulative Survival Probability (CSP)"
X_LIM = (2014, 2023)
X_TICKS_VALUES = [2015, 2017, 2019, 2021, 2023]
Y_LIM = (0, None)
NUM_COLUMNS = 5
NUM_ROWS = 7
FIGURE_HEIGHT = 40
FIGURE_WEIGHT = 40
MARKER_SIZE = 6
LINE_WIDTH = 2
SPACE_BETWEEN_PLOTS = 0.4
FILE_EXTENSION = '.pdf'
TITLE_FONT = 36
TITLE_VERTICAL_POSITION = 0.91
AXIS_TITLE_FONT = 48
X_AXIS_TITLE_VERTICAL_POSITION = 0.19
Y_AXIS_TITLE_HORIZONTAL_POSITION = 0.07
SHARE = True

file_info = {
    "save_figure": True,
    "folder": "outputs/figures/",
    "main title": "validation_step_1_actual_new_bev_registrations_and_empirical_csp_curves",
    "additional_info": 'all_countries',
    "group_info": '',  # Can update this dynamically if needed
    "comparison_type": '',  # Optional: e.g., 'comparison' for side-by-side analyses
    "own_calculation": True,  # Set True if calculations are from own model or study
    "file_extension": FILE_EXTENSION
}

base_plot_params = {
    "tick_fontsize": 28,
    "title_fontsize": 36,
    "space_between_plots": SPACE_BETWEEN_PLOTS,
    "figure_height": 40,
    "figure_width": 40,
    "marker_size": MARKER_SIZE,
    "line_width": LINE_WIDTH,
    "show_grid": True,
    "title": TITLE,
    "x_column": X_COLUMN,
    "y_column": Y_COLUMN,
    "x_label": X_LABEL,
    "y_label": Y_LABEL,
    "x_lim": X_LIM,
    "y_lim": Y_LIM,
    "x_ticks": X_TICKS_VALUES,
    "num_rows": NUM_ROWS,
    "num_columns": NUM_COLUMNS,
    "share": True,
    "title_font": TITLE_FONT,
    "title_vertical_position": TITLE_VERTICAL_POSITION,
    "axis_title_font": AXIS_TITLE_FONT,
    "x_axis_title_vertical_position": X_AXIS_TITLE_VERTICAL_POSITION,
    "y_axis_title_horizontal_position": Y_AXIS_TITLE_HORIZONTAL_POSITION,
    # Legend parameters
    "legend_show": True,
    "legend_loc": "lower right",
    "legend_bbox_to_anchor": (0.91, 0.235),  # Adjust to place the legend outside the figure
    "legend_fontsize": 40,
}

# Configurations for "all countries" and "grouped countries"
config_validation_step1 = {
    "plot_params": base_plot_params,
    "file_info": file_info,
}

config_validation_step2 = {
    "file_info": {
        **file_info,
        "main title": "validation_step_2_actual_new_bev_registrations_and_empirical_csp_curves",
    },
    "plot_params": {
        **base_plot_params,
        "title": "Actual BEV stock shares compared to estimated BEV shares using 2021 CSP curves and estimated new BEV registrations (Möring, 2024)",
    },
}