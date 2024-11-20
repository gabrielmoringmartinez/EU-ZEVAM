def update_optimal_distribution_based_on_country_csp(country, opt_dist):
    weibull_countries = opt_dist['Weibull']
    wg_countries = opt_dist['WG']
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
        'Weibull': weibull_countries,
        'WG': wg_countries
    }
    return combined_countries
