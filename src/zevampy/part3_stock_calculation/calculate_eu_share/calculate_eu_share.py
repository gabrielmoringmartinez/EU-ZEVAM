# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

from zevampy.part3_stock_calculation.calculate_eu_share.filter_calculate_and_add_eu_share import add_eu_stock_share
from zevampy.part3_stock_calculation.calculate_stock.input_data import eu_9, eu_26_and_norway, \
    eu_countries_and_norway
from zevampy.load_data_and_prepare_inputs.dimension_names import *


def calculate_eu_share(stock_share, historical_csp, countries_selected):
    """
    Calculates the stock share for the EU-27+Norway or for other EU groups.

    Parameters:
    - stock_share (pd.DataFrame): DataFrame containing stock data with columns like 'geo country', 'stock', and 'share'.
    - historical_csp (str): Flag indicating if historical CSP calculations are needed.
                            If set to 'historical CSP', calculates EU-9 and EU-26+Norway shares because data for all
                            EU-27+Norway countries is not available for historical years 2016 and 2008
    - share_label (str): Label for the share column to be added to the resulting DataFrame.

    Returns:
    - pd.DataFrame: DataFrame containing the original stock share data along with the calculated EU region shares.
    """
    countries_selected = set(countries_selected)
    has_full_eu27_norway = set(eu_countries_and_norway).issubset(countries_selected)
    has_full_eu9 = set(eu_9).issubset(countries_selected)
    has_full_eu26_norway = set(eu_26_and_norway).issubset(countries_selected)
    if has_full_eu27_norway:
        stock_share = add_eu_stock_share(stock_share, eu_27_plus_norway_label)

    if historical_csp == historical_csp_label:
        if has_full_eu9:
            stock_share = add_eu_stock_share(stock_share, eu_9_label)

        if has_full_eu26_norway:
            stock_share = add_eu_stock_share(stock_share, eu_26_plus_norway_label)
    return stock_share


