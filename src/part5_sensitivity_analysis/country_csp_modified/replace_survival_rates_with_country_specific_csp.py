import pandas as pd

from src.load_data_and_prepare_inputs.dimension_names import *


def replace_survival_rates_with_country_specific_csp(survival_rates, country_label):
    """
    Replaces the survival rates for a specified country in the DataFrame with its country-specific CSP values.

    Parameters:
        - survival_rates (pd.DataFrame):
            A DataFrame containing survival rates for multiple countries, with the following columns:
              - country_dim (str): Identifier for each country (e.g., 'geo country').
              - age_dim (str): Age of vehicles (e.g., 'vehicle age').
              - survival_rate_weibull_dim (str): Weibull survival rates.
              - survival_rate_weibull_gaussian_dim (str): Weibull-Gaussian survival rates.
              - distribution_dim (str): Type of distribution used.

        - country_label (str):
            The specific country for which survival rates should be replaced.

    Returns:
        - pd.DataFrame: Updated DataFrame where the survival rates for `country_label` replace the general survival
        rates for all countries.
    """
    # Selecting rows for the specific country label
    country_data = survival_rates[survival_rates[country_dim] == country_label]
    # Selecting survival rates for the specified country
    country_survival_rates = country_data[[age_dim, survival_rate_weibull_dim, survival_rate_weibull_gaussian_dim,
                                           distribution_dim]]
    # Merge survival rates of the specified country with the original DataFrame for all countries
    survival_rates_updated = pd.merge(survival_rates, country_survival_rates, on=age_dim, suffixes=(f'_{country_label}', ''))
    # Drop redundant columns
    survival_rates_updated.drop(columns=[f'{survival_rate_weibull_dim}_{country_label}',
                                        f'{survival_rate_weibull_gaussian_dim}_{country_label}',
                                        f'{distribution_dim}_{country_label}'], inplace=True)
    return survival_rates_updated

