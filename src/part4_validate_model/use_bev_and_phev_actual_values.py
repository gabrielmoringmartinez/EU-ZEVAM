from src.load_data_and_prepare_inputs.dimension_names import *


def use_bev_and_phev_actual_values(df_model, df_actual, keys=[country_dim, time_dim, powertrain_dim],
                          column_to_update=relative_sales_dim):
    """
    Updates the registrations with actual BEV and PHEV registration values where rows match on the specified keys.

    Parameters:
    df_model (pd.DataFrame): The main DataFrame to update.
    df_actual (pd.DataFrame): The DataFrame with actual values that are used for updating. This includes BEV and PHEV
    data.
    keys (list): List of columns to match between the two DataFrames.
    column_to_update (str): The name of the column in df_model to update.

    Returns:
    pd.DataFrame: The updated df_model with values from df_actual.
    """
    df1 = df_model.copy()
    df2 = df_actual.copy()

    df1.set_index(keys, inplace=True)
    df2.set_index(keys, inplace=True)

    df1.update(df2[[column_to_update]])
    df1.reset_index(inplace=True)
    return df1
