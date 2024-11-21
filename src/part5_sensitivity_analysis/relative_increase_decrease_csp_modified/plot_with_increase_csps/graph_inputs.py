# Define your configuration dictionary
TITLE = "BEV stock shares in relation to different Weibull average lifespans, γ, and different normal Gaussian distributions, µ, for high-importing countries."
X_COLUMN = "stock_year"
X_LABEL = "year"
Y_LABEL = "Battery Electric Vehicle (BEV) stock share (in %)"
X_LIM = (2014, 2050)
#X_TICKS_VALUES = [2015, 2017, 2019, 2021, 2023]
Y_LIM = (0, 1)
DECIMALS = 0
NUM_COLUMNS = 5
NUM_ROWS = 7
FIGURE_HEIGHT = 50
FIGURE_WIDTH = 50
MARKER_SIZE = 6
LINE_WIDTH = 2
SPACE_BETWEEN_PLOTS = 0.4
FILE_EXTENSION = '.pdf'
TITLE_FONT = 40
TITLE_VERTICAL_POSITION = 0.91
AXIS_TITLE_FONT = 40
X_AXIS_TITLE_VERTICAL_POSITION = 0.19
Y_AXIS_TITLE_HORIZONTAL_POSITION = 0.07
SHARE = True
percentages_selected = [-0.4, -0.2, 0, 0.2, 0.4]
stock_years = [2014, 2050]
historical_csp ='No'

file_info = {
    "save_figure": True,
    "folder": "outputs/figures/",
    "main title": "battery_electric_vehicle_stock_shares_eu_27_and_norway_up_to_2050_with_increased_decreased_country_csps",
    "additional_info": '',
    "group_info": '',  # Can update this dynamically if needed
    "comparison_type": '',  # Optional: e.g., 'comparison' for side-by-side analyses
    "own_calculation": True,  # Set True if calculations are from own model or study
    "file_extension": FILE_EXTENSION
}

base_plot_params = {
    "tick_fontsize": 28,
    "title_fontsize": 36,
    "space_between_plots": SPACE_BETWEEN_PLOTS,
    "figure_height": FIGURE_HEIGHT,
    "figure_width": FIGURE_WIDTH,
    "marker_size": MARKER_SIZE,
    "line_width": LINE_WIDTH,
    "show_grid": True,
    "title": TITLE,
    "x_column": X_COLUMN,
    "x_label": X_LABEL,
    "y_label": Y_LABEL,
    "x_lim": X_LIM,
    "y_lim": Y_LIM,
    "percentages_selected": percentages_selected,
    "stock_years": stock_years,
    "historical_csp": historical_csp,
    "number_of_decimals": DECIMALS,
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
    "legend_bbox_to_anchor": (0.95, 0.22),  # Adjust to place the legend outside the figure
    "legend_fontsize": 40,
    "fill_between": 'increased or decreased csp',
}

# Configurations for "all countries" and "grouped countries"
config_sensitivity_3 = {
    "plot_params": base_plot_params,
    "file_info": file_info,
}