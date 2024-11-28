# Functions
from src.part5_sensitivity_analysis.country_csp_modified import do_sensitivity_analysis_with_modified_country_csps
from src.part5_sensitivity_analysis.country_registrations_modified import do_sensitivity_analysis_with_modified_country_registrations
from src.part5_sensitivity_analysis.historical_csp_modified import do_sensitivity_analysis_with_historical_country_csps
from src.part5_sensitivity_analysis.relative_increase_decrease_csp_modified import do_sensitivity_analysis_with_increased_decreased_csps
from src.part3_stock_calculation.calculate_stock.input_data import simulation_stock_years

from src.load_data_and_prepare_inputs.dimension_names import *


def perform_sensitivity_analysis(data, calculated_data, inputs):
    """
    Performs sensitivity analysis with various country-specific CSP modifcations and registration data to assess
    the impact of different scenarios on stock shares and CSP values.

    Parameters:
    - data (dict):
        Dictionary containing input data such as survival rates and optimal parameters for past years.
        Keys should include:
            - `survival_rates_2016_label` (pd.DataFrame): Survival rates for 2016.
            - `optimum_parameters_2008_label` (dict): Optimal parameters from 2008 CSP analysis. Extracted from
            (Oguchi, 2014).
    - calculated_data (dict):
        Dictionary containing calculated data from previous computations.
        Keys should include:
            - `registrations_label` (pd.DataFrame): Registration data by year, powertrain and country.
            - `stock_shares_label` (pd.DataFrame): Stock share data calculated over time, country and powertrain.
            - `fitted_csp_values_label` (pd.DataFrame): Fitted CSP values for each country and vehicle age.
            - `optimal_distribution_dict_label` (dict): Dictionary specifying the optimal distribution per country
              (Weibull or Weibull-Gaussian).
            - `optimum_parameters_wg_label` (pd.DataFrame): Optimized CSP parameters for each country, including
            distribution type.
            - `survival_rates_2021_label` (pd.DataFrame): 2021 empirical survival rates for vehicles by country.
    - inputs (dict):
        Configuration and input parameters for sensitivity analysis.
        Keys should include:
            - `config_sensitivity_1_label` (dict): Config for modified country CSPs sensitivity analysis.
            - `config_sensitivity_2_label` (dict): Config for historical CSP sensitivity analysis.
            - `config_sensitivity_3_label` (dict): Config for increased/decreased CSPs analysis.
            - `config_sensitivity_4_label` (dict): Config for modified country registrations analysis.
            - `distribution_bounds_label` (tuple): Bounds for CSP parameter distribution.
            - `csp_available_years_label` (list): List of years for which CSP data is available (e.g 45 years).

    Returns:
        - None: Outputs plots comparing results with different CSP values and registrations
        Description:
        The function calls several sensitivity analysis routines to:
        1. **Modified CSPs Analysis**: Assesses impact of altered CSPs by country.
        2. **Historical CSP Analysis**: Compares using older empirical CSP values (e.g., from 2016 or 2008).
        3. **Increase/Decrease CSP Analysis**: Simulates effects of increasing or decreasing CSPs by a certain
        percentage.
        4. **Modified Registrations Analysis**: Analyzes how changing country registration data impacts stock.

        Each sensitivity analysis adjusts inputs or scenarios and reruns stock/share calculations based on
        preconfigured settings in the `inputs` dictionary.
        """
    # Extract the values from the calculated_data dictionary
    registrations = calculated_data[registrations_label]
    stock_shares = calculated_data[stock_shares_label]
    fitted_csp_values = calculated_data[fitted_csp_values_label]
    optimal_distribution_dict = calculated_data[optimal_distribution_dict_label]
    optimum_parameters_wg = calculated_data[optimum_parameters_wg_label]
    survival_rates_2021 = calculated_data[survival_rates_2021_label]
    do_sensitivity_analysis_with_modified_country_csps(registrations, stock_shares, fitted_csp_values,
                                                       optimal_distribution_dict, inputs[config_sensitivity_1_label])
    do_sensitivity_analysis_with_historical_country_csps(registrations, survival_rates_2021,
                                                         data[survival_rates_2016_label],
                                                         data[optimum_parameters_2008_label],
                                                         optimal_distribution_dict,
                                                         inputs[config_sensitivity_2_label])
    do_sensitivity_analysis_with_increased_decreased_csps(registrations, survival_rates_2021, optimum_parameters_wg,
                                                          optimal_distribution_dict, inputs[config_sensitivity_3_label],
                                                          inputs[csp_available_years_label])
    do_sensitivity_analysis_with_modified_country_registrations(registrations, stock_shares, fitted_csp_values,
                                                                optimal_distribution_dict,
                                                                inputs[config_sensitivity_4_label])
