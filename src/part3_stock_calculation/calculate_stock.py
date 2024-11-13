from src.part3_stock_calculation.repeat_csp_data_for_all_years import repeat_csp_data_for_all_years
from src.part3_stock_calculation.calculate_year_of_first_registration import calculate_year_of_first_registration
from src.part3_stock_calculation.merge_survival_rates_with_registrations import merge_survival_rates_with_registrations
from src.part3_stock_calculation.compute_stock_data import compute_stock_values
from src.part3_stock_calculation.select_optimum_distribution import select_optimum_distribution
from src.part3_stock_calculation.cleanup_stock_data import cleanup_stock_data

time_dim = 'time'
registrations_dim = 'registrations by powertrain'
merge_keys = ['geo country', time_dim]
columns_to_drop = ['survival rate Weibull', 'survival rate WG', 'distribution', 'cluster', 'stock_weibull',
                   'stock_wg', 'new vehicle registrations', 'relative sales', registrations_dim]


def calculate_stock(registrations, csp_values, optimal_distribution_dict, stock_years):
    """
    Calculates stock data for each country over a specified range of years.

    Parameters:
        registrations (DataFrame): A DataFrame with vehicle registrations by powertrain, including historical
        and projected data.
        csp_values (DataFrame): DataFrame containing fitted CSP values for each country by vehicle age,
        distribution model (Weibull and Weibull Gaussian), and distribution type.
        optimal_distribution_dict (dict): Dictionary specifying the optimal distribution type per country.
        stock_years (list): List with start and end year, specifying the range of years to expand data.

    Returns:
        DataFrame: Final stock data by country, powertrain and vehicle age with
         calculation columns (unnecessary) columns removed.
    """

    # Step 1: Expand CSP data for all years in the specified range
    survival_rates = repeat_csp_data_for_all_years(csp_values, stock_years)

    # Step 2: Calculate the year of first registration
    survival_rates = calculate_year_of_first_registration(survival_rates, time_dim)

    # Step 3: Merge survival rates with registrations data
    stock_data = merge_survival_rates_with_registrations(survival_rates, registrations, merge_keys)

    # Step 4: Compute stock values based on Weibull and Weibull-Gaussian parameters
    stock_data = compute_stock_values(stock_data, registrations_dim)

    # Step 5: Select the optimal distribution and assign it to the 'stock' column
    stock_data['stock'] = stock_data.apply(select_optimum_distribution, axis=1, optimal_distribution_dict=optimal_distribution_dict)
    stock_data = stock_data.rename(columns={time_dim: "year of first registration"})

    # Step 6: Clean up unnecessary columns and save to CSV
    #stock_data.to_csv(f'outputs/stock_data_with_calculation_columns.csv', sep=';', index=False, decimal=',')
    stock_data = cleanup_stock_data(stock_data, columns_to_drop)
    stock_data.to_csv(f'outputs/3_1_stock_data.csv', sep=';', index=False, decimal=',')
    return stock_data












