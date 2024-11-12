import pandas as pd

time_dim = 'time'
registrations_dim = 'registrations by powertrain'
merge_keys = ['geo country', time_dim]
columns_to_drop = ['survival rate Weibull', 'survival rate WG', 'distribution', 'cluster', 'stock_weibull',
                   'stock_wg', 'new vehicle registrations', 'relative sales', registrations_dim]


def calculate_stock(registrations, csp_values, optimal_distribution_dict, stock_years):
    survival_rates = repeat_data_for_years(csp_values, stock_years)
    survival_rates = calculate_registration_year(survival_rates, time_dim)
    stock_data = merge_survival_rates_with_registrations(survival_rates, registrations, merge_keys)
    # Compute stock values based on Weibull and Weibull-Gaussian CSP values
    stock_data = compute_stock_values(stock_data, registrations_dim)
    # Stock based on the optimum distribution is obtained
    stock_data['stock'] = stock_data.apply(select_column, axis=1, optimal_distribution_dict=optimal_distribution_dict)
    stock_data = stock_data.rename(columns={time_dim: "year of first registration"})
    # Cleanup calculation columns before saving
    #stock_data.to_csv(f'outputs/stock_data_with_calculation_columns.csv', sep=';', index=False, decimal=',')
    stock_data = cleanup_stock_data(stock_data, columns_to_drop)
    stock_data.to_csv(f'outputs/3_1_stock_data.csv', sep=';', index=False, decimal=',')


def repeat_data_for_years(original_df, stock_years):
    """
    Expands the original DataFrame to include each year in the specified range.
    """
    start_year, end_year = stock_years
    years = pd.DataFrame({'stock_year': range(start_year, end_year + 1)})
    result_df = original_df.merge(years, how='cross')
    return result_df


def select_column(row, **kwargs):
    optimal_distribution_dict = kwargs.get('optimal_distribution_dict', {})  # Retrieve the opt_dist_dict from kwargs
    if row['geo country'] in optimal_distribution_dict.get('Weibull', {}):
        return row['stock_weibull']
    elif row['geo country'] in optimal_distribution_dict.get('WG', {}):
        return row['stock_wg']
    else:
        return None  # You can handle the case when the country is not in any key


def calculate_registration_year(survival_rates, time_dimension, stock_year_col='stock_year', age_col='vehicle age'):
    """
    Calculates the registration year for each entry based on stock year and vehicle age.
    """
    survival_rates[time_dimension] = survival_rates[stock_year_col] - survival_rates[age_col] + 1
    return survival_rates


def merge_survival_rates_with_registrations(survival_rates_df, registrations_df, merge_keys):
    """
    Merges survival rates with vehicle registrations on specified keys.
    """
    return pd.merge(survival_rates_df, registrations_df, on=merge_keys, how='inner')


def compute_stock_values(stock_df, registrations_dimension):
    """
    Computes stock values for Weibull and Weibull-Gaussian distributions.
    """
    stock_df['stock_weibull'] = stock_df['survival rate Weibull'] * stock_df[registrations_dimension]
    stock_df['stock_wg'] = stock_df['survival rate WG'] * stock_df[registrations_dimension]
    return stock_df


def cleanup_stock_data(stock_data, drop_columns):
    """
    Drops unnecessary columns from the stock data.
    """
    return stock_data.drop(columns=drop_columns)
