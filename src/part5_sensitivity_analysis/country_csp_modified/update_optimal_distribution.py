from src.load_data_and_prepare_inputs.dimension_names import weibull_label, weibull_gaussian_label


def update_optimal_distribution_based_on_country_csp(country, opt_dist):
    weibull_countries = opt_dist[weibull_label]
    wg_countries = opt_dist[weibull_gaussian_label]
    # Checking if the provided country is present in weibull_countries and wg_countries
    if country in weibull_countries:
        weibull_countries.extend(wg_countries)
        wg_countries = []
    elif country in wg_countries:
        wg_countries.extend(weibull_countries)
        weibull_countries = []
    else:
        weibull_countries = []
        wg_countries = []
    # Combine the two lists into a single dictionary variable
    combined_countries = {
        weibull_label: weibull_countries,
        weibull_gaussian_label: wg_countries
    }
    return combined_countries
