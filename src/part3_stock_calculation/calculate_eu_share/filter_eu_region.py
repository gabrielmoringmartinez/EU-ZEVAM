from src.part3_stock_calculation.calculate_stock.input_data import eu_country_groups
from src.load_data_and_prepare_inputs.dimension_names import country_dim


def filter_eu_region(df, eu_region):
    """
       Filters the input DataFrame to include only rows for the specified EU region.

       Parameters:
       - df (pd.DataFrame): DataFrame containing stock data with columns like 'geo country', 'stock',
                            and 'share'.
       - eu_region (str): The EU region identifier ('EU-9', 'EU-26+Norway' or 'EU-27+Norway') to filter and calculate.

       Returns:
       - pd.DataFrame: DataFrame containing only the rows that match the specified EU region.
       """
    return df[df[country_dim].isin(eu_country_groups[eu_region])].copy()
