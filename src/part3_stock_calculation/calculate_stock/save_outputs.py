from src.load_data_and_prepare_inputs.dimension_names import stock_data_filename_label, stock_shares_filename_label


def save_outputs(stock_data, stock_shares, save_options):
    """
    Saves the stock data and stock shares to specified filenames if indicated in save_options.
    Parameters:
        stock_data (DataFrame): The DataFrame containing stock data.
        stock_shares (DataFrame): The DataFrame containing stock share data.
        save_options (dict): Dictionary with settings for saving outputs. Expected keys:
            - "stock_data_filename" (str): Filename for saving stock data.
            - "stock_shares_filename" (str): Filename for saving stock shares.
    """
    # Set default save options
    stock_data_filename = save_options.get(stock_data_filename_label)
    stock_shares_filename = save_options.get(stock_shares_filename_label)
    # Save stock data and stock shares if specified
    stock_data.to_csv(f'outputs/{stock_data_filename}', sep=';', index=False, decimal=',')
    stock_shares.to_csv(f'outputs/{stock_shares_filename}', sep=';', index=False, decimal=',')
