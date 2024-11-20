import pandas as pd


def replace_survival_rates_with_country_specific_csp(survival_rates, country_label):
    # Selecting rows for the specific country label
    country_data = survival_rates[survival_rates['geo country'] == country_label]
    # Selecting survival rates for the specified country
    country_survival_rates = country_data[['vehicle age', 'survival rate Weibull', 'survival rate WG', 'distribution']]
    # Merge survival rates of the specified country with the original DataFrame for all countries
    survival_rates_merged = pd.merge(survival_rates, country_survival_rates, on='vehicle age', suffixes=(f'_{country_label}', ''))
    # Drop redundant columns
    survival_rates_merged.drop(columns=[f'survival rate Weibull_{country_label}', f'survival rate WG_{country_label}', f'distribution_{country_label}'], inplace=True)

    return survival_rates_merged