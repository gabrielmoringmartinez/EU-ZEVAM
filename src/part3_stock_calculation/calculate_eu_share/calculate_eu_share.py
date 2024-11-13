from src.part3_stock_calculation.calculate_eu_share.filter_calculate_and_add_eu_share import add_eu_stock_share


def calculate_eu_share(stock_share, historical_csp, share_label):
    """
    Calculates the stock share for the EU-27+Norway or for other EU groups.

    Parameters:
    - stock_share (pd.DataFrame): DataFrame containing stock data with columns like 'geo country', 'stock', and 'share'.
    - historical_csp (str): Flag indicating if historical CSP calculations are needed.
                            If set to 'historical CSP', calculates EU-9 and EU-26+Norway shares because data for all
                            EU-27+Norway countries is not available
    - share_label (str): Label for the share column to be added to the resulting DataFrame.

    Returns:
    - pd.DataFrame: DataFrame containing the original stock share data along with the calculated EU region shares.
    """
    stock_share_eu = add_eu_stock_share(stock_share, share_label, 'EU-27+Norway')
    if historical_csp == 'historical CSP':
        stock_share_eu_9 = add_eu_stock_share(stock_share, share_label, 'EU-9')
        stock_share_eu_26 = add_eu_stock_share(stock_share_eu_9, share_label, 'EU-26+Norway')
        return stock_share_eu_26
    return stock_share_eu


