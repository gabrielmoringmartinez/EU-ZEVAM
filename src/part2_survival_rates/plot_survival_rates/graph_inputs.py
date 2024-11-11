# Define your configuration dictionary
YEAR = '2021'
X_COLUMN = "vehicle age"
Y_COLUMN = "survival rate"
X_LABEL = "Age of Vehicle"
Y_LABEL = "Cumulative Survival Probability (CSP)"
FIGURE_HEIGHT = 40
FIGURE_WEIGHT = 40
MARKER_SIZE = 6
LINE_WIDTH = 2
SPACE_BETWEEN_PLOTS = 0.22
NUMBER_OF_COUNTRIES_PER_PLOT = 16

file_info = {
    "save_figure": True,
    "year": YEAR,
    "additional_info": 'all_countries',
    "group_info": '',  # Can update this dynamically if needed
    "comparison_type": '',  # Optional: e.g., 'comparison' for side-by-side analyses
    "own_calculation": True,  # Set True if calculations are from own model or study
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
    "x_column": X_COLUMN,
    "y_column": Y_COLUMN,
    "x_label": X_LABEL,
    "y_label": Y_LABEL,
    "number_of_countries_group": NUMBER_OF_COUNTRIES_PER_PLOT,
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
        "legend_fontsize": 40,
        "title_fontsize": 56,  # Overridden values for grouped plot
    },
    "file_info": file_info,
}