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
    optimal_distribution_dict = kwargs.get('optimal_distribution_dict', {})  # Retrieve the opt_dist_dict from kwargs
    if row['geo country'] in optimal_distribution_dict.get('Weibull', {}):
        return row['stock_weibull']
    elif row['geo country'] in optimal_distribution_dict.get('WG', {}):
        return row['stock_wg']
    else:
        return None
