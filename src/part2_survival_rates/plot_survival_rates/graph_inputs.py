# Define your configuration dictionary
TITLE = "Empirical cumulative survival probability (CSP) curves of year 2021"
X_COLUMN = "vehicle age"
X_LABEL = "Vehicle age"
Y_LABEL = "Cumulative Survival Probability (CSP)"
X_LIM = (0, 45)
Y_LIM = (0, None)
FIGURE_HEIGHT = 40
FIGURE_WEIGHT = 40
MARKER_SIZE = 6
LINE_WIDTH = 2
SPACE_BETWEEN_PLOTS = 0.4
NUMBER_OF_COUNTRIES_PER_PLOT = 16
FILE_EXTENSION = '.pdf'
TITLE_FONT = 64
TITLE_VERTICAL_POSITION = 0.93
AXIS_TITLE_FONT = 48
X_AXIS_TITLE_VERTICAL_POSITION = 0.075

file_info = {
    "save_figure": True,
    "folder": "outputs/figures/",
    "main title": "CSP 2021",
    "additional_info": 'all_countries',
    "group_info": '',  # Can update this dynamically if needed
    "comparison_type": '',  # Optional: e.g., 'comparison' for side-by-side analyses
    "own_calculation": True,  # Set True if calculations are from own model or study
    "file_extension": FILE_EXTENSION
}

base_plot_params = {
    "tick_fontsize": 28,
    "legend_fontsize": 28,
    "title_fontsize": 36,
    "space_between_plots": SPACE_BETWEEN_PLOTS,
    "figure_height": 40,
    "figure_width": 40,
    "marker_size": MARKER_SIZE,
    "line_width": LINE_WIDTH,
    "show_grid": True,
    "title": TITLE,
    "x_column": X_COLUMN,
    "x_label": X_LABEL,
    "y_label": Y_LABEL,
    "x_lim": X_LIM,
    "y_lim": Y_LIM,
    "number_of_countries_group": NUMBER_OF_COUNTRIES_PER_PLOT,
    "title_font": TITLE_FONT,
    "title_vertical_position": TITLE_VERTICAL_POSITION,
    "axis_title_font": AXIS_TITLE_FONT,
    "x_axis_title_vertical_position": X_AXIS_TITLE_VERTICAL_POSITION,
    "y_axis_title_horizontal_position": X_AXIS_TITLE_VERTICAL_POSITION,
    "legend_show": True,
    "legend_loc": "upper left",
    "legend_bbox_to_anchor": (0.265, 0.885),  # Adjust to place the legend outside the figure
    "legend_fontsize": 30,
}

# Configurations for "all countries" and "grouped countries"
config_all = {
    "plot_params": base_plot_params,
    "file_info": file_info,
}

config_group = {
    "plot_params": {
        **base_plot_params,
        "tick_fontsize": 40,
        "title_fontsize": 56,
        "legend_bbox_to_anchor": (0.347, 0.885),  # Adjust to place the legend outside the figure
        "legend_fontsize": 44,
    },
    "file_info": file_info,
}