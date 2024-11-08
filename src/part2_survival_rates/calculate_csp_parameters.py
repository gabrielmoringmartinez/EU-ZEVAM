from src.part2_survival_rates.csp_parameters_optimization_algorithms import run_diff_evol_algorithm_weibull, \
    run_diff_evol_algorithm_weibull_gaussian


def calculate_csp_parameters(survival_rates, year):
    """
        Calculates optimal CSP parameters for country-specific Weibull and Weibull-Gaussian survival curves. Bounds
        selected for the optimization based on the conclusion extracted in Held, 2021 and described in Appendix F

        Args:
            survival_rates (DataFrame): Contains 'country label' and 'survival rate' columns.
            year (int): The year of the data of empirical survival rates.

        Returns:
            DataFrame: Optimized CSP parameters per country.
        """
    bounds_weibull = [(5, 50), (1, 6)]
    k = [2, 100]
    mu = [5, 30]
    sigma = [5, 30]
    bounds_gaussian = [k, mu, sigma]
    country_names = survival_rates['country label'].unique()
    optimum_parameters_weibull = run_diff_evol_algorithm_weibull(bounds_weibull, country_names, survival_rates)
    optimum_parameters_weibull_gaussian = run_diff_evol_algorithm_weibull_gaussian(bounds_gaussian, country_names,
                                                                                   survival_rates,
                                                                                   optimum_parameters_weibull)
    optimum_parameters_weibull_gaussian.to_csv(f'outputs/2_1_optimum_parameters_csp_curves.csv', sep=';', index=False, decimal=',')
    return optimum_parameters_weibull_gaussian
