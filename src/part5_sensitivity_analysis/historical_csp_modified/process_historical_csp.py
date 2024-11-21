from src.part3_stock_calculation.compute_csp_values_and_compute_stock import compute_csp_values_and_compute_stock
from src.part5_sensitivity_analysis.historical_csp_modified.calculate_2008_survival_rates import calculate_2008_survival_rates
from src.part5_sensitivity_analysis.historical_csp_modified.merge_stock_shares import merge_stock_shares


def process_stock_shares_with_historical_csps(registrations, survival_rates_2021, survival_rates_2016, stock_years,
                                              optimum_parameters_2008, optimal_distribution_dict):
    """
    Compute stock shares for different years and merge them into a single DataFrame.

    Returns:
        pd.DataFrame: Merged DataFrame containing stock shares for multiple years.
    """
    # Compute stock shares for different years
    stock_values_2021, stock_shares_2021, *_ = compute_csp_values_and_compute_stock(survival_rates_2021, registrations,
                                                                                    2021, stock_years, 'historical CSP')
    stock_values_2016, stock_shares_2016, *_ = compute_csp_values_and_compute_stock(survival_rates_2016, registrations,
                                                                                    2016, stock_years, 'historical CSP')
    stock_shares_2008 = calculate_2008_survival_rates(optimum_parameters_2008, survival_rates_2021,
                                                      optimal_distribution_dict, registrations)

    # Rename columns to match the year-specific share columns
    stock_shares_2021.rename(columns={'share': f'share_{2021}'}, inplace=True)
    stock_shares_2016.rename(columns={'share': f'share_{2016}'}, inplace=True)
    stock_shares_2008.rename(columns={'share': f'share_{2008}'}, inplace=True)

    # Merge all stock shares into one DataFrame
    stock_shares_df = None
    for stock_shares in [stock_shares_2021, stock_shares_2016, stock_shares_2008]:
        stock_shares_df = merge_stock_shares(stock_shares_df, stock_shares)

    return stock_shares_df