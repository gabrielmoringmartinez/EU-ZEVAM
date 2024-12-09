from src.part2_survival_rates.plot_survival_rates.plot_all_countries import plot_all_countries
from src.part3_stock_calculation.calculate_stock.calculate_stock import calculate_stock
from src.part5_sensitivity_analysis.country_adjectives import country_adjectives
from src.part5_sensitivity_analysis.country_registrations_modified.generate_columns_to_plot import \
    generate_columns_to_plot
from src.part5_sensitivity_analysis.country_registrations_modified.replace_powertrain_share_registrations_with_country \
    import replace_powertrain_share_registrations_with_country
from src.part5_sensitivity_analysis.update_stock_shares import update_stock_shares

from src.load_data_and_prepare_inputs.dimension_names import *


def do_sensitivity_analysis_with_modified_country_registrations(registrations, stock_shares, survival_rates,
                                                                optimal_distribution_dict, config):
    """
    Performs a sensitivity analysis by modifying the vehicle registration BEV share to assume it equal to a certain
    country for all countries and recalculating stock shares for each country. The analysis evaluates how changes in
    country registrations affect stock projections, with comparisons across different countries.

    Parameters:
        - registrations (pd.DataFrame): A DataFrame containing registration data by year, powertrain, and country.
        - stock_shares (pd.DataFrame): Stock share data calculated over time, country and powertrain.
        - survival_rates (pd.DataFrame): Fitted survival rates for each country and vehicle age.
        - optimal_distribution_dict (dict): A dictionary containing the optimal CSP (Country-Specific Parameter)
          distribution for each country, used to calculate the stock shares.
        - config (dict): A configuration dictionary that contains settings for the sensitivity analysis, including:
          - `plot_params` (dict): Parameters related to plotting and analysis settings, including:
            - `countries_selected` (list of str): The list of countries for which vehicle registrations are modified.
            - `simulation_stock_years_label` (list of int): The range of years over which the stock calculation is done.
            - `historical_csp_label` (str): Indicator to use historical CSP data or not.
            - `powertrain_to_plot_label` (str): The type of powertrain (e.g., 'BEV') for which stock shares are plotted.

    Returns:
        None: The function updates the stock shares DataFrame and generates a plot comparing stock shares for the
        selected countries, showing how the modified registrations impact the stock projections.

    Description:
    1. **Modified Registrations**:
       - For each country in the `countries_selected` list, the function replaces the country-specific registration
         data with a modified version that reflects the selected country's share of registrations.

    2. **Stock Calculation**:
       - For each modified set of registrations, the function calculates the stock values and stock shares using
         the `calculate_stock` function, based on the survival rates and optimal CSP distribution.

    3. **Stock Shares Update**:
       - The function updates the stock shares DataFrame with the recalculated stock shares for each country.

    4. **Plot Generation**:
       - The stock shares for the selected powertrain (e.g., BEV) are filtered from the stock shares DataFrame.
       - The `generate_columns_to_plot` function is used to generate the column names and labels for the plot legend.
       - The results are plotted using the `plot_all_countries` function, visualizing the impact of modified registrations
         on stock shares across different countries.

    This analysis provides insights into how changes in BEV vehicle registration share across countries can affect
    the stock shares of different powertrain types, helping to assess the sensitivity of stock projections to
    country-specific registration data.
    """
    plot_params = config[plot_params_dim]
    columns_to_plot = {share_dim: share_dim.capitalize()}
    stock_shares_df = stock_shares
    for country in plot_params[countries_selected_label]:
        updated_registrations = replace_powertrain_share_registrations_with_country(registrations, country, plot_params)
        stock_values, stock_shares = calculate_stock(updated_registrations, survival_rates, optimal_distribution_dict,
                                                     plot_params[simulation_stock_years_label],
                                                     plot_params[historical_csp_label])
        stock_shares_df = update_stock_shares(stock_shares_df, stock_shares, country)
        columns_to_plot = generate_columns_to_plot(columns_to_plot, plot_params[countries_selected_label],
                                                   country_adjectives)
    bev_stock_shares = stock_shares_df[stock_shares_df[powertrain_dim] == plot_params[powertrain_to_plot_label]]
    plot_all_countries(bev_stock_shares, config, columns_to_plot, None)
