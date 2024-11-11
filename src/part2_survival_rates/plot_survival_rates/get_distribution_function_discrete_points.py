import pandas as pd


def get_distribution_function_discrete_points(survival_rate_distribution_function, survival_rates_country,
                                              predicted_function_value):
    survival_rates_country = survival_rates_country.reset_index()  # for reseting the index
    survival_rates_country = survival_rates_country.drop(['index'], axis=1)  # deleting the new column of index
    survival_rates_country['survival rate'] = predicted_function_value
    survival_rate_distribution_function = pd.concat([survival_rate_distribution_function, survival_rates_country],
                                                    ignore_index=True)
    survival_rate_distribution_function.to_excel(f'outputs/test_survival_rate_distribution_function.xlsx', index=False)
    return survival_rate_distribution_function
