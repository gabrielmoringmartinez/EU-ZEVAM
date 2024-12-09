from src.load_data_and_prepare_inputs.dimension_names import *


def select_optimum_distribution(row, **kwargs):
    """
    Determines the stock value based on the optimal distribution for each country.

    Parameters:
        row (Series): A row of stock data.
        optimal_distribution_dict (dict): Dictionary specifying which distribution (Weibull or WG)
                                              to use per country.

    Returns:
        float: Stock value based on the optimal distribution, or None if no match is found.
    """
    optimal_distribution_dict = kwargs.get(optimal_distribution_dict_label, {}) # Retrieve the opt_dist_dict from kwargs
    if row[country_dim] in optimal_distribution_dict.get(weibull_label, {}):
        return row[stock_weibull_dim]
    elif row[country_dim] in optimal_distribution_dict.get(weibull_gaussian_label, {}):
        return row[stock_wg_dim]
    else:
        return None
